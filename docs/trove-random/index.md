---
title: Random items from Trove
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
zenodo_concept_id: 3549403
---

{{ git_latest_tag() }}

Changes to the Trove API mean that the techniques I've previously used to select resources at random [will no longer work](https://updates.timsherratt.org/2019/10/09/creators-and-users.html). This repository includes some alternative ways of retrieving *random-ish* works and newspaper articles from Trove. While I've tried to mix things up and get as deep into the results set as possible, it's likely that some items are still inaccessible. So while the results will appear random, they may in fact be filtered due to the way facets are applied and delivered through the API. I hope that in the future Trove will provide a random sort option to avoid these problems.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Get an random newspaper article from Trove](random_newspaper_article.md) {: data-toc-omit }

This method searches for a random stop word, letter, or digit, then filters the results by randomly applying facets until the result set is less that 100 (or as near as possible).

### [:material-notebook-outline: Get a random work from Trove by generating random `id`s](random_work_by_id.md) {: data-toc-omit }

Here's a way you can get a random work from Trove's book, article, picture, map, music, or collection zones. It generates random work id prefixes and performs a wildcard search using the id index.

### [:material-notebook-outline: Get a random work from Trove using queries and facets](random_work_by_facets.md) {: data-toc-omit }

Here's another way you can get a random work from Trove's book, article, picture, map, music, or collection zones. Basically this method gets all the available facets for a particular search. If the search has more than 100 results, it chooses one of the facets at random and applies it.

<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-random/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name trove-random -v "$PWD":/home/jovyan/work quay.io/glamworkbench/trove-random repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-random`
* Open the new directory" `cd trove-random`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-random.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer) for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
