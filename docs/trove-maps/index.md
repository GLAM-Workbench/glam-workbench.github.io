---
title: Trove maps
repo_url: https://github.com/GLAM-Workbench/trove-maps
repo_name: trove-maps
zenodo_concept_id: 3549426
---

{{ git_latest_tag() }}

The Trove 'map' zone includes single maps, as well as map series, atlases, and aerial photographs. You can access metadata from the map zone through the Trove API.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-maps/master)

## Tips, tools, and examples

### [:material-notebook-outline: Exploring digitised maps in Trove](exploring-digitised-maps.md)

I knew there were lots of great maps you could download from Trove, but how many? And how big were the files? I thought I'd try to quantify this a bit by harvesting and analysing the metadata.

### [:material-notebook-outline: Parse map coordinates from metadata](parse-coordinates.md)

This notebook attempts to parse coordinate strings from the metadata and convert the values to decimals. It then uses the values to explore the geographical context of Trove's digitised map collection.

## Data

### [:material-folder-text-outline: Trove digitised maps metadata](single-maps-data.md)

*Harvested: 31 January 2023*

This dataset contains metadata describing digitised maps in Trove, harvested from the Trove API and other sources.

### [:material-folder-text-outline: Trove digitised maps – coordinates](single-maps-coordinates-data.md)

*Harvested: 31 January 2023*

This dataset was generated from the harvest of digitised maps metadata. Coordinate strings in the metadata (points and bounding boxes) were parsed and converted to decimal values.


## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-maps/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-maps/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See [Using Reclaim Cloud](https://glam-workbench.net/using-reclaim-cloud/) for more details.

### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name trove-maps -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-maps repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-maps`
* Open the new directory" `cd trove-maps`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-maps.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer) for more details.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
