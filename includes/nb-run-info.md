<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

{% if page.meta.jlite_repo %}

### Using Jupyter Lite

[![Jupyter Lite](../images/jlite-badge.svg)](http://glam-workbench.net/{{ page.meta.jlite_repo }}/)

Click on the button above to launch notebooks from this repository using [Jupyter Lite](https://jupyterlite.readthedocs.io/en/stable/). Unlike other methods that rely on cloud services or require you to install software, Jupyter Lite automatically builds the necessary computing environment within your browser. Although the notebooks are running on your local computer, changes may not be saved. Make sure you download any changed notebooks or harvested data that you want to save.

{% endif %}

### Using ARDC Binder

[![Launch on ARDC Binder](../images/launch-ARDC-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [ARDC Binder](https://mybinder.org/) service. This is a free service available to researchers in Australian universities. You'll be asked to log in with your university credentials. Note that sessions will close if you stop using the notebooks, and no data will be preserved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using ARDC Binder](https://glam-workbench.net/using-ardc-binder/) for more details.

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-contributors/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/{{repo_name}}/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See [Using Reclaim Cloud](/using-reclaim-cloud/) for more details.

### Running in a container on your own computer

GLAM Workbench repositories are stored as pre-built container images on [quay.io](https://quay.io/organization/glamworkbench). You can run these containers on your own computer to set up a virtual machine with everything you need to use the notebooks. This is free, but requires more technical knowledge – you'll have to install [Podman](https://podman.io/) on your computer, and be able to use the command line.

* Install [Podman](https://podman.io/docs/installation).
* In a terminal, run the following command:  
  ```
  podman run --rm -p 8888:8888 quay.io/glamworkbench/{{repo_name}} jupyter lab --ip=0.0.0.0 --port=8888 --ServerApp.token="" --LabApp.default_url="/lab/tree/index.ipynb"
  ```
* It will take a while to download and configure the container image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`
* When you've finished, download any files or data you want to keep from Jupyter Lab, and enter ++ctrl+c++ int the terminal.

See [Running in a container on your own computer](/using-containers/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks. You'll need to have recent versions of Python and Git installed. I use [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv), and [pip-tools](https://github.com/jazzband/pip-tools) to create and manage Python versions and environments.

In a terminal:

* Create a Python virtual environment (Python >= 3.10 should be ok): `pyenv virtualenv 3.10.12 {{repo_name}}`
* Activate the virtual environment: `pyenv local {{repo_name}}`
* Use `git clone` to create a local version of the GLAM Workbench repository: `git clone https://github.com/GLAM-Workbench/{{repo_name}}.git`
* Use `cd` to move into the newly-cloned folder: `cd {{repo_name}}`
* Run `pip install pip-tools` to install `pip-tools`.
* Run `pip-sync requirements.txt dev-requirements.txt` to install the required Python packages.
* Start Jupyter with `jupyter lab` – a browser window should open automatically. If not, copy and paste the url from the command line to your web browser.
* To shut down your Jupyter Lab session enter ++ctrl+c++ in the terminal.

See [Using Python on your own computer](/using-python/) for more details.

<!-- END RUN INFO -->


