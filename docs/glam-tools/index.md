---
title: Useful tools for working with GLAM collections
description: This repository helps you make use of a number of tools and services that can be useful in working with GLAM collections.
repo_url: https://github.com/GLAM-Workbench/glam-tools
repo_name: glam-tools
---


## CloudStor

[CloudStor](https://support.aarnet.edu.au/hc/en-us/categories/200217608-CloudStor) is a data storage service provided by AARNet. Individual researchers in AARNet connected institutions get 1TB of storage space for free, and research projects can apply for additional space.

A number of GLAM Workbench repositories use CloudStor to share harvested datasets. See, for example, [Trove journals](https://glam-workbench.net/trove-journals/), [Trove books](https://glam-workbench.net/trove-books/), and [Trove newspapers](https://glam-workbench.net/trove-newspapers/).

You can easily share folders in CloudStor, but it's not always obvious how to access files within shared folders. These notebooks document some methods for accessing files in publicly-shared folders.

### [:material-notebook-outline: Creating and sharing public links to nested resources in CloudStor](cloudstor-share-nested-links.md) 

It's easy to create a public link to a file or folder in the CloudStor interface. But what if you have lots of files in nested folders that you want to make publicly accessible? Yes, you can share the parent folder, but how do you create direct public links to files and folders inside the parent folder without generating new share links for every resource.

This notebook demonstrates how to create links to resources nested within a shared folder. The code cells run some simple tests to try and make sure that the example links go where they're supposed to.

### [:material-notebook-outline: Cloudstor access to a public share via WebDAV](cloudstor-access-via-webdav.md) 

An alternative to manually constructing links is to use a WebDAV client. It takes a bit of effort to configure, but once it's set up you can access information about, and download, publicly shared files and folders.

<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/glam-tools/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/glam-tools/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name glam-tools -v "$PWD":/home/jovyan/work quay.io/glamworkbench/glam-tools repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

