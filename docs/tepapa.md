---
title: Te Papa
repo_url: https://github.com/GLAM-Workbench/te-papa-api
repo_name: te-papa-api
zenodo_concept_id: 3549094
---

# Te Papa collections

{{ git_latest_tag() }}

Te Papa has a [very well-documented API](https://data.tepapa.govt.nz/docs/index.html) that provides rich information about its collection and the relationships between collection items and other entities, including people and places.

You'll need [an API key](https://data.tepapa.govt.nz/docs/register.html) for serious exploration.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### Exploring the Te Papa collection API  
This notebook is just a preliminary exploration of the API. It drills down through some of the facets to try and get a picture of what data is available.

* [Download from GitHub](https://github.com/GLAM-Workbench/te-papa-api/blob/master/Exploring-the-Te-Papa-collection-API.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/te-papa-api/blob/master/Exploring-the-Te-Papa-collection-API.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab%2Ftree%2FExploring-the-Te-Papa-collection-API.ipynb)

### Mapping Te Papa's collections
This notebook creates some simple maps using the `production.spatial` facet of the Te Papa API to identify places where collection objects were created.

* [Download from GitHub](https://github.com/GLAM-Workbench/te-papa-api/blob/master/Mapping-Te-Papa-collections.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/te-papa-api/blob/master/Mapping-Te-Papa-collections.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab%2Ftree%2FMapping-Te-Papa-collections.ipynb)

![Screen capture](images/tepapa-map.png)

<!-- START RUN INFO -->


## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/te-papa-api/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See [Using Reclaim Cloud](https://glam-workbench.net/using-reclaim-cloud/) for more details.

### Using the Nectar Cloud

![Screenshot of GLAM Workbench applicatsion](images/nectar-gw-app.png){width="600"}

The [Nectar Research Cloud](https://ardc.edu.au/services/nectar-research-cloud/) (part of the Australian Research Data Commons) provides cloud computing services to researchers in Australian and New Zealand universities. University-affiliated researchers can log on to Nectar and receive [up to 6 months of free cloud computing time](https://tutorials.rc.nectar.org.au/allocation-management/03-account-and-trial). And if you need more, you can [apply for a specific project allocation](https://tutorials.rc.nectar.org.au/allocation-management/04-allocation-and-projects).

The GLAM Workbench is available in the Nectar Cloud as a pre-configured application. This means you can get it up and going without worrying about the technical infrastructure – just fill in a few details and you're away! To create an instance of this repository in the Nectar Cloud:

* Log in to the [Nectar Dashboard](https://dashboard.rc.nectar.org.au/) using your university credentials.
* From the Dashboard choose **Applications -> Browse Local**.
* Enter 'GLAM' in the filter box and hit Enter, you should see the GLAM Workbench application.
* Click on the GLAM Workbench application's  **Quick Deploy** button.
* Step through the various [configuration options](https://glam-workbench.net/using-nectar/#setting-up-your-own-glam-workbench-repository). Some options are only available if you have a dedicated project allocation.
* When asked to select a GLAM Workbench repository, choose 'Te Papa collections' from the dropdown list.
* Complete the configuration and deploy your GLAM Workbench instance.
* The url to access your instance will be displayed once it's ready. Click on the url!

See [Using Nectar](https://glam-workbench.net/using-nectar/) for more information.

### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name tepapa -v "$PWD":/home/jovyan/work quay.io/glamworkbench/te-papa-api repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv tepapa`
* Open the new directory" `cd tepapa`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/te-papa-api.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See the [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer) for more details.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
