---
title: NSW State Archives
description: A collection of notebooks for working with collection data from the NSW State Archives.
repo_name: nsw-state-archives
repo_url: https://github.com/GLAM-Workbench/nsw-state-archives
zenodo_concept_id: 3549128
---

{{ git_latest_tag() }}

A collection of notebooks for working with collection data from the [NSW State Archives](https://mhnsw.au/collections/state-archives-collection/).

NSW State Archives content in copyright was previously licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0) licence](http://creativecommons.org/licenses/by/4.0/). See their archived [copyright page](https://web.archive.org/web/20220303172132/https://www.records.nsw.gov.au/about-state-records/copyright-policy) for more information.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/HEAD?urlpath=lab/tree/index.ipynb)

## Tools, tips, and examples

### [:material-notebook-outline: Get details of online indexes](get-list-of-indexes.md) {: data-toc-omit }
This notebook scrapes details of available indexes from the [NSW State Archives A to Z list of online indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z). It saves the results as a CSV formatted file.

### [:material-notebook-outline: Harvest online indexes](harvest-indexes.md) {: data-toc-omit }
This notebook harvests data from all of [NSW State Archives online indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z), saving the data as a collection of easily downloadable CSV files.

### [:material-notebook-outline: Summarise index details](summarise-index-details.md) {: data-toc-omit }
This notebook counts the number of rows in each index and calculates the total for the whole repository. It formats the results in nice HTML and Markdown tables for easy browsing.

### [:material-notebook-outline: NSW State Archives Index Explorer](index-explorer.md) {: data-toc-omit }
NSW State Archives provides a lot of rich descriptive data in its online indexes. But there's so much data it can be hard to understand what's actually in each index. This notebook tries to help by generating an overview of an index, summarising the contents of each field.

## Data

### [:material-folder-outline: CSV list of indexes](index-list.md) {: data-toc-omit }

*Harvested May 2023*

### [:material-folder-outline: Repository of harvested indexes](index-repository.md) {: data-toc-omit }

**Currently: 75 indexes harvested with 2,481,881 rows of data.**  
*Harvested May 2023*

<!-- START RUN INFO -->


## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/nsw-state-archives/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/nsw-state-archives/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name nsw-state-archives -v "$PWD":/home/jovyan/work quay.io/glamworkbench/nsw-state-archives repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv nsw-state-archives`
* Open the new directory" `cd nsw-state-archives`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/nsw-state-archives.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer for more details.

<!-- END RUN INFO -->


## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
