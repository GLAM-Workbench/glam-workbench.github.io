---
title: Trove images
repo_url: https://github.com/GLAM-Workbench/trove-images
repo_name: trove-images
zenodo_concept_id: 6339873
---

{{ git_latest_tag() }}


Trove's 'picture' zone includes photographs, posters, artworks, and artefacts. You can access metadata from the 'picture' zone through the Trove API.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: The use of standard licences and rights statements in Trove image records](use-of-rights-statements.md) {: data-toc-omit }

Version 2.1 of the Trove API introduced a new rights index that you can use to limit your search results to records that include one of a list of standard licences and rights statements. We can also use this index to build a picture of which rights statements are currently being used, and by who. Let's give it a try...

## Datasets

### [:material-database-outline: Rights applied to images by each Trove contributor](csv-image-rights-by-institution.md) {: data-toc-omit }

This CSV-formatted dataset lists the number of images with each rights statement from organisations contributing to Trove.

### [:material-database-outline: Rights applied to out-of-copyright photographs by each Trove contributor](csv-out-of-copyright-photos-rights-by-institution.md) {: data-toc-omit }

This CSV-formatted dataset lists the number of out-of-copyright photographs (created before 1955) with each rights statement from organisations contributing to Trove.

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using ARDC Binder

[![Launch on ARDC Binder](../images/launch-ARDC-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [ARDC Binder](https://mybinder.org/) service. This is a free service available to researchers in Australian universities. You'll be asked to log in with your university credentials. Note that sessions will close if you stop using the notebooks, and no data will be preserved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using ARDC Binder](https://glam-workbench.net/using-ardc-binder/) for more details.

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-images/master?urlpath=lab/tree/index.md)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-images/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name trove-newspaper-harvester -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-images repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}