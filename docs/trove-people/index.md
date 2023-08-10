---
title: Trove People & Organisations
description: Trove's People and Organisations zone aggregates information about individuals and organisations, bringing multiple sources together under a single identifier. Data is available through a number of APIs.
repo_url: https://github.com/GLAM-Workbench/trove-people
repo_name: trove-people
zenodo_concept_id: 7645058
---

{{ git_latest_tag() }}

Trove's People and Organisations zone aggregates information about individuals and organisations, bringing multiple sources together under a single identifier.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Harvesting data

There are two methods of harvesting the complete set of data from the People and Organisations zone – using the [OAI-PMH API](http://www.nla.gov.au/apps/peopleaustralia-oai/), or using the main Trove API in conjunction with the [SRU interface](http://www.nla.gov.au/apps/srw/search/peopleaustralia). The OAI-PMH method is *much* faster, but includes duplicate records that you'll need to filter out afterwards.

### [:material-notebook-outline: Harvesting the complete set of data from the People and Organisations zone](complete_harvest.md) {: data-toc-omit }

This notebook demonstrates the API/SRU method for creating a complete data harvest.

### [:material-notebook-outline: Harvesting the complete set of data from the People and Organisations zone using OAI-PMH](complete_harvest_oai.md) {: data-toc-omit }

This notebook demonstrates the OAI-PMH method for creating a complete data harvest.

## Analysing data

### [:material-notebook-outline: Extract some aggregated data from the complete harvest](extract_aggregated_data_from_harvest.md) {: data-toc-omit }

The complete harvest of records in the Trove People & Organisations zone is very large – more than 1.3 million records, almost 9gb of data. To do some analysis of its content, we'll extract some aggregate totals by looping through all the EAC-CPF records.

### [:material-notebook-outline: Harvest SRU API results as JSON](get_sru_results_as_json.md) {: data-toc-omit }

You can query the People & Organisations data using the SRU (Search/Retrieve via URL) API, and retrieve data in a number of XML formats, the richest and most complex of which is EAC-CPF. However, the XML records are not easy to work with, so to simplify further processing, this notebook queries the SRU interface and then converts the EAC-CPF XML results into JSON.

### [:material-notebook-outline: Visualising intersections and overlaps between data sources](intersections.md) {: data-toc-omit }

The People & Organisations zone aggregates information from a range of data sources into individual records. In this notebook we'll explore connections between the data sources.

### [:material-notebook-outline: Get VIAF links relating to Trove People & Organisation records](viaf.md) {: data-toc-omit }

VIAF, the Virtual International Authority File, aggregates identifiers for people and organisations from a wide range of name authority systems, including Libraries Australia. Many records in Trove's People & Organisations zone have Libraries Australia identifiers attached to them. Using these LA identifers it's possible to query VIAF for links related to a Trove record in other name authority systems.

## Data

### [:material-folder-outline: Complete harvest of People and Organisations data](complete_harvest_dataset.md) {: data-toc-omit }

This is a complete harvest of the EAC-CPF records in Trove's People & Organisations zone.

### [:material-folder-outline: Aggregated data extracted from People and Organisations data](aggregated_datasets.md) {: data-toc-omit }

These datasets provide aggregated data extracted from the complete harvest of data from Trove's People and Organisations zone.

<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-people/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-people/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name trove-people -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-people repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-people`
* Open the new directory" `cd trove-people`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-people.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}