---
title: Trove contributors
description: Trove aggregates metadata from thousands of organisations and projects around Australia. Data about contributors is available from the `/contributor` endpoint of the Trove API. Here you'll find some examples of harvesting and exploring data about Trove's metadata contributors.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
---

{{ git_latest_tag() }}


Trove aggregates metadata from thousands of organisations and projects around Australia. Data about contributors is available from the `/contributor` endpoint of the Trove API. Here you'll find some examples of harvesting and exploring data about Trove's metadata contributors.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-contributors/master?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Create a flat list of organisations contributing metadata to Trove](get_contributors.md) {: data-toc-omit }

This notebook converts the nested data available from the `/contributor` endpoint into a single flat list of contributors

### [:material-notebook-outline: Get the number of records from each contributor by zone and format](get_contributors_totals_zone_format.md) {: data-toc-omit }

This notebook gets the number of records contributed by each organisation, aggregated by zone and format

## Datasets

### [:material-database-outline: List of organisations contributing metadata to Trove](trove-contributors-list.md) {: data-toc-omit }

This is a flattened version of the contributors data available from the Trove API. It is harvested weekly.

### [:material-database-outline: Count of records by contributor and zone](trove-contributors-zones.md) {: data-toc-omit }

This dataset was created by searching for contributor's NUC codes in each Trove zone. This gives a count of records by contributor and zone. It is harvested weekly.

### [:material-database-outline: Count of records by contributor, zone, and format](trove-contributors-formats.md) {: data-toc-omit }

This dataset was created by searching for contributor's NUC codes in each Trove zone and requesting the format facet. This gives a count of records by contributor, zone, and format. It is harvested weekly.


<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-contributors/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-contributors/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name trove-contributors -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-contributors repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-contributors`
* Open the new directory" `cd trove-contributors`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-contributors.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}