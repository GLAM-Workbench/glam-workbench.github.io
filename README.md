# GLAM Workbench documentation

This repository contains the main documentation files for the GLAM Workbench and is used to build the site at: [glam-workbench.net](https://glam-workbench.net/).

I also use this repository to bring together [issues](https://github.com/GLAM-Workbench/glam-workbench.github.io/issues) and [discussions](https://github.com/GLAM-Workbench/glam-workbench.github.io/discussions) relating to the GLAM Workbench in general – feel free to contribute!

Here's a [complete list of GLAM Workbench repositories](https://github.com/GLAM-Workbench).

## Contributing

### Minor changes

For minor edits and corrections:

* [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository.
* [Make changes](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) using the GitHub file editor.
* [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to share your changes back with the main repository.

### Major changes

If you're making major changes, such as adding a new section, you'll want to set up your own local version of the documentation for editing and testing:

* [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository
* [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the forked repository to your own computer.
* Create and activate a Python virtual environment. I use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create and manage Python versions and environments.
* Move to the `site` directory: `cd glam-workbench.github.io/site`
* Install `pip-tools`: `pip install pip tools`
* Install requirements: `pip-sync`
* Run the documentation site: `mkdocs serve`. The site will be available at http://127.0.0.1:8000/.
* Create or edit pages in the `docs` directory. See mkdocs and mkdocs-material documentation for more information.

Any changes to markdown files in the `docs` directory should trigger a rebuild and reload of the site. If you make changes to templates, or to the `mkdocs.yml` config file, you'll probably need to stop and restart the server. Once you've finished you can `git push` the changes back to your fork, and [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

### Cite as

Tim Sherratt, GLAM Workbench, 2021, https://doi.org/10.5281/zenodo.5603059

---
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
