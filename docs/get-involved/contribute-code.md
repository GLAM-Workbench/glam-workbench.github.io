# Contribute code to a GLAM Workbench repository

If you want to improve the GLAM Workbench's Jupyter notebooks, or add new notebooks to an existing repository, you can contribute your code by setting up a local development environment.

## Setting up your local environment

1. Create and activate a Python virtual environment (Python >= 3.8 should be ok). I use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create and manage Python versions and environments.
2. Create your own [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the GLAM Workbench repository.
3. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) **your newly-forked** GLAM Workbench repository to your own computer, eg. `git clone https://github.com/mygithubuser/trove-newspapers.git`
4. On the command line, use `cd` to move into the `notebooks` folder of the newly-cloned repository, eg. `cd trove-newspapers/notebooks`
5. On the command line, run `pip install -r requirements.txt` to install the required Python packages.

## Running Jupyter Lab

1. On the command line, run `jupyter lab` – to start Jupyter.
2. A browser window should open automatically. If not, copy and paste the url from the command line to your web browser.
3. Make your changes!
4. To shut down your Jupyter Lab session hit ++ctrl+c++.

## Uploading your changes

1. Don't forget to add your  details to the `creators` section of the `.zenodo.json` file. This will ensure you're added as an author to the next released version uploaded to Zenodo. (I'm planning to automate this process in the future.)
2. On the command line, use `git` to add and commit your changes.
3. On the command line, use `git push` to upload your changes to your forked repository.
4. Use the GitHub web interface to [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) from your forked repository to the original GLAM Workbench repository.

Creating a pull request will run a GitHub action that tries to build and cache the repository on Binder. If it works, a comment will be added to the pull request with a button to run your updated version on Binder. This lets you test to make sure things will run as expected on Binder and other cloud services.

Your pull request will be reviewed, and if it all looks good it will be merged into the main repository.

## Testing and formatting

I've started adding additional configuration files to repositories to help developers set up semi-automated formatting and testing of notebooks. If the repository you're working with includes files named `requirements-dev.txt`, `pyproject.toml`, and `.pre-commit-config.yaml` then you can follow the steps below to set things up. If the files aren't present, then skip this section.

1. On the command line, run `pip install pip-tools` to install [pip tools](https://github.com/jazzband/pip-tools).
1. On the command line, run `pip-sync requirements.txt requirements-dev.txt` – to install the latest versions of required packages
2. On the command line, run `pre-commit install` to set up the Git pre-commit hooks.

For information on how to use these tools, see [testing and testing notebooks](developing-repositories.md/#testing-and-formatting-notebooks) on the [Developing a new repository](developing-repositories.md) page.

## Adding new Python packages

If you're creating a new notebook, you might need to install some additional Python packages. The process for this is described in the [Adding new Python packages](developing-repositories.md/#adding-new-python-packages) section of [Developing a new repository](developing-repositories.md). However, not all repositories currently have a `requirements.in` file, as I'm still updating them to use pip-tools. If this is the case, [raise an issue](https://github.com/GLAM-Workbench/glam-workbench.github.io/issues) and I'll help you set it up.

## Contributors

Contributors will be listed on the site's [contributors](../contributors.md) page.