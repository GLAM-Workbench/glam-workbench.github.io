---
title: Trove lists and tags
description: Trove lists and tags are created by Trove users to organise and describe resources. The details of public lists and tags are available through the Trove API. The notebooks in this repository demonstrate how to harvest and analyse list and tag data.
repo_url: https://github.com/GLAM-Workbench/trove-lists
repo_name: trove-lists
zenodo_concept_id: 3549453
---

{{ git_latest_tag() }}

Trove lists and tags are created by Trove users to organise and describe resources. The details of public lists and tags are available through the Trove API. The notebooks in this repository demonstrate how to harvest and analyse list and tag data.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/index.ipynb)

## Lists

### [:material-notebook-outline: Convert a Trove list into a CSV file](convert-a-trove-list-into-a-csv-file.md)  

This notebook converts Trove lists into CSV files (spreadsheets). Separate CSV files are created for newspaper articles and works from Trove's other zones. You can also save the OCRd text, a PDF, and an image of each newspaper article.

### [:material-notebook-outline: Convert a Trove list into a CollectionBuilder exhibition](convert-list-to-cb-exhibition.md)

This notebook converts a Trove list into a series of files that can be uploaded to a [CollectionBuilder-GH](https://github.com/CollectionBuilder/collectionbuilder-gh) repository to create an instant exhibition. 

### [:material-notebook-outline: Harvest summary data from Trove lists](harvest-summary-data-from-lists.md)
Use the Trove API to harvest data about all public lists, then extract some summary data and explore a few different techniques to analyse the complete dataset.

## Tags

### [:material-notebook-outline: Harvest public tags from Trove zones](harvest-tags.md)

This notebook uses the Trove API to assemble a dataset containing all public tags added to Trove.

### [:material-notebook-outline: Analyse public tags added to Trove](analyse_tags.md)

This notebook loads the complete dataset of Trove tags and explores some ways of analysing and visualising the tag data.

## Data

### [:material-folder-text-outline: Trove lists metadata](trove-lists-metadata.md)

*Harvested: 5 July 2022*. CSV formatted file containing a complete harvest of metadata describing user-created Trove lists.

### [:material-folder-text-outline: Trove public tags](trove-public-tags.md)

*Harvested: 6 July 2022*. CSV formatted file containing a complete harvest of public tags added to Trove resources.

### [:material-folder-text-outline: Trove tag counts](trove-tag-counts.md)

*Harvested: 6 July 2022*. CSV formatted file containing the total number of times each tag in Trove has been applied to resources.

<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See the [Using Binder](https://glam-workbench.net/using-binder/) section of the GLAM Workbench for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](../images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-lists/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See the [Using Reclaim Cloud](https://glam-workbench.net/using-reclaim-cloud/) section GLAM Workbench for more details.

### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name trove-lists -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-lists repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See the [Using Docker](https://glam-workbench.net/using-docker/) section of the GLAM Workbench for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-lists`
* Open the new directory" `cd trove-lists`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-lists.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See the [GLAM Workbench](https://glam-workbench.net/using-python/) for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

