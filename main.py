import requests
from datetime import date, timedelta
import requests_cache
from requests_cache import CachedSession
import re
import github
import os
from dotenv import load_dotenv
from pathlib import Path
from rocrate.rocrate import ROCrate
from humanize import naturalsize
import pandas as pd
import markdown

load_dotenv()

requests_cache.install_cache('gh_cache', expire_after=timedelta(days=7))

s = CachedSession(expire_after=timedelta(days=7))

def get_create_action(crate, id, property="instrument"):
    actions = crate.get_by_type("CreateAction")
    related_actions = []
    for action in actions:
        props = action.properties()
        # print(props)
        value = props.get(property)
        if isinstance(value, list):
            for prop in value:
                if prop["@id"] == id:
                    related_actions.append(props)
        elif value:
            if value["@id"] == id:
                related_actions.append(props)
    return related_actions

def dataset_includes_file(root, file):
    for part in root.properties().get("hasPart", []):
        print(part["@id"])
        if part["@id"] == file.strip("#"):
            return True

def on_pre_page_macros(env):
    html = ''
    repo_name = env.page.meta.get('repo_name')
    contributors = env.page.meta.get('contributors', [])
    contributors_exclude = env.page.meta.get('contributors_exclude', [])
    rocrate_url = env.page.meta.get('rocrate')
    page_type = env.page.meta.get('page_type')
    # print(repo_name)
    headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
    if repo_name:
        g = github.Github(auth=github.Auth.Token(os.getenv("GITHUB_TOKEN")))
        repo = g.get_repo(f'GLAM-Workbench/{repo_name}')
        for user in repo.get_contributors():
            user_name = None
            if user.name:
                user_name = user.name
            elif not user.login.startswith('github-'):
                user_name = user.login
            if user_name and user_name not in contributors_exclude:
                contributors.append({"name": user_name, "url": user.html_url})
            env.page.meta['contributors'] = contributors
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
                link = releases[0]['html_url']
            except (KeyError, IndexError):
                # print(releases)
                tag = ''
                link = ''
        if tag:
            html += f'<li class="md-source__fact md-source__fact--version">{tag}</li>'
        if stars:
            html += f'<li class="md-source__fact md-source__fact--stars">{stars}</li>'
        if forks:
            html += f'<li class="md-source__fact md-source__fact--forks">{forks}</li>'
        env.page.meta['repo_stats'] = html
        env.page.meta['version'] = tag
        env.page.meta['version_url'] = link

    zenodo_id = env.page.meta.get('zenodo_concept_id')
    if zenodo_id:
        try:
            r = s.get(f'https://zenodo.org/api/records/{zenodo_id}', timeout=30)
        except requests.exceptions.RequestException:
            print('Could not get data from Zenodo!')
        else:
            details = r.json()
            try:
                doi = details['links']['doi']
            except KeyError:
                print(zenodo_id)
            badge = f"https://zenodo.org/badge/DOI/{details['doi']}.svg"
            #badge = details['links']['badge']
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
            env.page.meta["doi"] = doi
            env.page.meta["badge"] = badge
            env.page.meta["pub_date"] = details['metadata']['publication_date']
            env.page.meta["zenodo_title"] = title
            env.page.meta["version"] = version
            env.page.meta["authors"] = authors
            env.page.meta["citation"] = f'{author_str}. ({fdate}). {title} (version {version}). Zenodo. [{doi}]({doi})' + '  \n\n' + f'[![]({badge})]({doi})'
    if rocrate_url:
        response = s.get(rocrate_url, refresh=True)
        data = response.json()["@graph"]
        crate = ROCrate()
        for d in data:
            crate.add_or_update_jsonld(d)
        root = crate.get("./")
        if page_type == "dataset":
            datasets = []
            
            for datafile in crate.get_by_type("Dataset"):
                if dataset_includes_file(root, datafile["@id"]):
                    props = datafile.properties()
                    if "conformsTo" in props:
                        # print(props["conformsTo"]["@id"])
                        #schema = crate.get("#" + props["conformsTo"]["@id"]).properties()
                        schema = crate.get(props["conformsTo"]["@id"]).properties()
                        if "url" in schema:
                            response = requests.get(schema["url"])
                            schema_data = response.json()
                            props["columns"] = schema_data["fields"]
                    if "license" in props:
                        props["license"] = crate.get(props["license"]["@id"].lstrip("#"))
                    datasets.append(props)
            action = crate.get_by_type("CreateAction")[0]
            action["nb"] = crate.get(action["instrument"]["@id"].lstrip("#"))
            
            examples = []
            if "workExample" in root:
                for example_id in root["workExample"]:
                    example = crate.get(example_id["@id"]).properties()
                    if example_id["@id"].startswith("https://glam-workbench.net/datasette-lite/"):
                        env.page.meta["datasette"] = example
                    else:    
                        examples.append(example)
            env.page.meta["datasets"] = datasets
            env.page.meta["rocrate_description"] = root["description"]
            if not env.page.meta.get("description"):
                try:
                    env.page.meta["description"] = root["description"].split("\n\n")[1]
                except IndexError:
                    env.page.meta["description"] = root["description"]
            env.page.meta["action"] = action
            env.page.meta["examples"] = examples
            if "distribution" in root:
                env.page.meta["distribution"] = root["distribution"]["@id"]
        if page_type == "repo":
            nbs = []
            ds_docs = []
            for nb in crate.get_by_type(["File", "SoftwareSourceCode"]):
                # print(nb)
                # Only include nbs that have a GW page
                if nb.get("mainEntityOfPage"):
                    nbs.append(nb.properties())
            print(nbs)
            for action in crate.get_by_type("CreateAction"):
                print(action.properties())
                for result in action["result"]:
                    dataset = crate.get(result["@id"])
                    if source_link := dataset.get("isPartOf"):
                        print("source")
                        source = crate.get(source_link["@id"])
                        ds_doc = crate.get(source["mainEntityOfPage"]["@id"])
                        ds_doc["description"] = source.get("description", "").split("\n\n")[0]
                    elif gw_link := dataset.get("mainEntityOfPage"):
                        print("gw_link")
                        ds_doc = crate.get(gw_link["@id"])
                        if not ds_doc.get("description"):
                            ds_doc["description"] = dataset.get("description", "").split("\n\n")[0]
                    else:
                        print("neither")
                        ds_doc = dataset
                    ds_docs.append(ds_doc)
            env.page.meta["rocrate_description"] = root["description"]
            env.page.meta["notebooks"] = nbs
            env.page.meta["datasets"] = list(set(ds_docs))
        if page_type == "datafile":
            df_name = env.page.meta.get('datafile')
            dataset = crate.get(df_name)
            nbs = []
            examples = []
            action = get_create_action(crate, df_name, "result")[0]
            print(action)
            action["nb"] = crate.get("#" + action["instrument"]["@id"])
            # actions += get_create_action(crate, df_name, "object")
            # print(actions)
            if "workExample" in dataset:
                for example_id in dataset["workExample"]:
                    example = crate.get(example_id["@id"]).properties()
                    if example_id["@id"].startswith("https://glam-workbench.net/datasette-lite/"):
                        env.page.meta["datasette"] = example
                    else:    
                        examples.append(example)
            """
            for action in actions:
                nb = crate.get("#" + action["instrument"]["@id"])
                nbs.append(crate.get(nb["mainEntityOfPage"]["@id"]))
            """
            env.page.meta["action"] = action
            env.page.meta["datasets"] = [dataset]
            env.page.meta["examples"] = examples
            env.page.meta["rocrate_description"] = dataset["description"]
            try:
                env.page.meta["description"] = dataset["description"].split("\n\n")[1]
            except IndexError:
                env.page.meta["description"] = dataset["description"]
        if page_type == "notebook":
            datasets = []
            nb_name = env.page.meta.get('notebook')
            nb = crate.get("#" + nb_name)
            if not nb:
                nb = crate.get(nb_name)
            actions = get_create_action(crate, nb_name)
            print(actions)
            for action in actions:
                for result in action["result"]:
                    dataset = crate.get(result["@id"])
                    # print(dataset.properties())
                    if source_link := dataset.get("isPartOf"):
                        print("source")
                        source = crate.get(source_link["@id"])
                        ds_doc = crate.get(source["mainEntityOfPage"]["@id"])
                        ds_doc["description"] = source.get("description", "").split("\n\n")[0]
                    elif gw_link := dataset.get("mainEntityOfPage"):
                        print("gw_link")
                        ds_doc = crate.get(gw_link["@id"])
                        ds_doc["description"] = dataset.get("description", "").split("\n\n")[0]
                    else:
                        print("neither")
                        ds_doc = dataset
                    datasets.append(ds_doc)
            env.page.meta["nb"] = nb
            env.page.meta["datasets"] = list(set(datasets))
            env.page.meta["rocrate_description"] = nb.get("description", "")
            try:
                env.page.meta["description"] = nb.get("description", "").split("\n\n")[1]
            except IndexError:
                env.page.meta["description"] = nb.get("description", "")





def define_env(env):
    "Hook function"

    @env.macro
    def zenodo_citation():
        return env.page.meta.get("citation", "")

    @env.macro
    def git_latest_tag():
        version = ''
        version_tag = env.page.meta.get('version')
        version_link = env.page.meta.get('version_url')
        if version_tag and version_link:
            version = f'##### Current version: [{version_tag}]({version_link}) {{: data-toc-omit }}'
        elif version_tag:
            version = f'##### Current version: {version_tag} {{: data-toc-omit }}'
        return version

    @env.macro
    def set_repo_stats():
        return env.page.meta.get("repo_stats", "")

    @env.macro
    def repo_contributors():
        md = ''
        g = github.Github(auth=github.Auth.Token(os.getenv("GITHUB_TOKEN")))
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
        g = github.Github(auth=github.Auth.Token(os.getenv("GITHUB_TOKEN")))
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
        g = github.Github(auth=github.Auth.Token(os.getenv("GITHUB_TOKEN")))
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
        g = github.Github(auth=github.Auth.Token(os.getenv("GITHUB_TOKEN")))
        repo = g.get_repo(repository)
        f = repo.get_contents(file)
        content = f.decoded_content.decode("utf-8")
        if section:
            content = get_markdown_section(content, section)
        return content
    
    @env.macro
    def nb_preview():
        nb = env.page.meta.get("notebook", "")
        preview_url = Path(Path(env.page.url).parts[0], "previews", nb.replace(".ipynb", ".html"))
        preview_path = Path(env.conf["docs_dir"], preview_url)
        print(preview_path)
        if preview_path.exists():
            return f"!!! preview\n    <iframe class='nb-preview' loading='lazy' src='/{str(preview_url)}'></iframe>\n    [:material-circle-expand: Expand](/{str(preview_url)})"
        return ""
    
    @env.filter
    def htmlify(md):
        return markdown.markdown(md)

            
