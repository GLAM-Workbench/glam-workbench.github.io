import requests
from datetime import date, timedelta
from requests_cache import CachedSession
import re
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

s = CachedSession(expire_after=timedelta(days=1))

def on_post_page_macros(env):
    html = ''
    repo_name = env.page.meta.get('repo_name')
    headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
    if repo_name:
        try:
            r = s.get(f'https://api.github.com/repos/glam-workbench/{repo_name}', timeout=30, headers=headers)
        except requests.exceptions.RequestException:
            print('Could not get data from GitHub!')
            data = {}
        else:
            data = r.json()
        stars = data.get('stargazers_count')
        forks = data.get('forks_count')
        try:
            r = s.get(f'https://api.github.com/repos/glam-workbench/{repo_name}/releases', timeout=30, headers=headers)
        except requests.exceptions.RequestException:
            print('Could not get data from GitHub!')
        else:
            releases = r.json()
            try:
                tag = releases[0]['tag_name']
            except (KeyError, IndexError):
                # print(releases)
                tag = ''
        if tag:
            html += f'<li class="md-source__fact md-source__fact--version">{tag}</li>'
        if stars:
            html += f'<li class="md-source__fact md-source__fact--stars">{stars}</li>'
        if forks:
            html += f'<li class="md-source__fact md-source__fact--forks">{forks}</li>'
        env.page.meta['repo_stats'] = html


def define_env(env):
    "Hook function"

    @env.macro
    def zenodo_citation():
        zenodo_id = env.page.meta.get('zenodo_concept_id')
        if zenodo_id:
            try:
                r = s.get(f'https://zenodo.org/api/records/{zenodo_id}', timeout=30)
            except requests.exceptions.RequestException:
                print('Could not get data from Zenodo!')
                return ''
            else:
                details = r.json()
                doi = details['links']['doi']
                badge = details['links']['badge']
                # fdate = date.fromisoformat(details['metadata']['publication_date']).strftime('%-d %B %Y')
                fdate = date.fromisoformat(details['metadata']['publication_date']).strftime('%Y')
                title = details['metadata']['title']
                version = details['metadata']['version']
                authors = [c['name'] for c in details['metadata']['creators']]
                if len(authors) == 2:
                    author_str = f'{authors[0]} & {authors[1]}'
                elif len(authors) > 2:
                    author_str = f'{"; ".join(authors[:-1])} & {authors[-1]}'
                else:
                    author_str = authors[0]
                citation = f'{author_str}. ({fdate}). {title} (version {version}). Zenodo. [{doi}]({doi})' + '  \n\n' + f'[![]({badge})]({doi})'
                return citation
        else:
            return ''

    @env.macro
    def git_latest_tag(tag_only=False):
        """
        Function to get the latest tag from the git repository which matches
        the configured regex for the version tag format.
        :param page_path:
        :return: String with the highest semver tag, returns "unknown" if not found.
        """
        version = ''
        repo_name = env.page.meta.get('repo_name')
        if repo_name:
            try:
                headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
                r = s.get(f'https://api.github.com/repos/glam-workbench/{repo_name}/releases', timeout=30, headers=headers)
            except requests.exceptions.RequestException:
                print('Could not get data from GitHub!')
                return ''
            else:
                releases = r.json()
                try:
                    tag = releases[0]['tag_name']
                    link = releases[0]['html_url']
                except (KeyError, IndexError):
                    # print(releases)
                    pass
                else:
                    if tag_only:
                        version = tag
                    else:
                        version = f'##### Current version: [{tag}]({link})  {{: data-toc-omit }}'
        return version

    @env.macro
    def set_repo_stats():
        html = ''
        repo_name = env.page.meta.get('repo_name')
        headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
        if not repo_name:
            repo_name = env.conf['repo_name']
            try:
                r = s.get(f'https://api.github.com/orgs/{repo_name}', timeout=30, headers=headers)
            except requests.exceptions.RequestException:
                print('Could not get data from GitHub!')
            else:
                data = r.json()
                repos = data.get('public_repos')
                if repos:
                    html += f'<li class="md-source__fact md-source__fact--repositories">{repos}</li>'
        elif repo_name:
            try:
                r = s.get(f'https://api.github.com/repos/glam-workbench/{repo_name}', timeout=30, headers=headers)
            except requests.exceptions.RequestException:
                print('Could not get data from GitHub!')
            else:
                data = r.json()
                stars = data.get('stargazers_count')
                forks = data.get('forks_count')
                version = git_latest_tag(tag_only=True)
                if version:
                    html += f'<li class="md-source__fact md-source__fact--version">{version}</li>'
                if stars:
                    html += f'<li class="md-source__fact md-source__fact--stars">{stars}</li>'
                if forks:
                    html += f'<li class="md-source__fact md-source__fact--forks">{forks}</li>'
        return html

    @env.macro
    def repo_contributors():
        md = ''
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo(f'GLAM-Workbench/{env.page.meta.get("repo_name")}')
        for user in repo.get_contributors():
            if user.name:
                md += f'* [{user.name}]({user.html_url})\n'
            elif not user.login.startswith('github-'):
                md += f'* [{user.login}]({user.html_url})\n'
        return md

    @env.macro
    def documentation_contributors():
        md = ''
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo(f'GLAM-Workbench/{env.conf["repo_name"]}')
        for user in repo.get_contributors():
            if user.name:
                md += f'* [{user.name}]({user.html_url})\n'
            elif not user.login.startswith('github-'):
                md += f'* [{user.login}]({user.html_url})\n'
        return md

    @env.macro
    def code_contributors():
        users = []
        g = Github(os.getenv("GITHUB_TOKEN"))
        org = g.get_organization(f'GLAM-Workbench')
        for repo in org.get_repos(type='public'):
            if not repo.fork:
                for user in repo.get_contributors():
                    if user.name:
                        users.append(f'* [{user.name}]({user.html_url})')
                    elif not user.login.startswith('github-'):
                        users.append(f'* [{user.login}]({user.html_url})')
        return ('\n').join(list(set(users)))


    # Code below modified from https://github.com/mercari/mkdocs-git-snippet

    def get_markdown_section(content: str, section: str) -> str:
        section_pattern = re.compile("^#+ ")
        match = section_pattern.search(section)
        if not match:
            raise ValueError(f"Invalid section name: {section}")
        section_level = match.span()[1] - 1
        target = re.compile("^" + section + "$", re.MULTILINE)
        start = target.search(content)
        if not start:
            raise ValueError(f"Not found: {section}")
        start_index = start.span()[1]

        end_target = re.compile("^#{1," + str(section_level) + "} ", re.MULTILINE)
        end = end_target.search(content[start_index:])
        if end:
            end_index = end.span()[0]
            content = content[start_index : end_index + start_index]
        else:
            content = content[start_index:]
        return content

    @env.macro
    def gitsnippet(repository: str, file: str, section: str) -> str:
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo(repository)
        f = repo.get_contents(file)
        content = f.decoded_content.decode("utf-8")
        if section:
            content = get_markdown_section(content, section)
        return content
