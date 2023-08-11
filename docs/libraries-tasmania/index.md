---
title: Libraries Tasmania
description: This repository provides a collection of tools and examples for working with data from Libraries Tasmania. 
repo_url: https://github.com/GLAM-Workbench/libraries-tasmania
repo_name: libraries-tasmania
zenodo_concept_id: 7080836
---

{{ git_latest_tag() }}

A collection of tools and examples for working with data from [Libraries Tasmania](https://www.libraries.tas.gov.au/).

You might also find the [Zotero translator for the Libraries Tasmania catalogue](https://updates.timsherratt.org/2022/07/14/calling-all-tasmanian.html) useful.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/HEAD?urlpath=lab/tree/index.ipynb)

## Tasmanian Post Office Directories

The [Tasmanian Post Office Directories from 1890 to 1948](https://stors.tas.gov.au/ILS/SD_ILS-981598) have been digitised and made available by Libraries Tasmania for download as PDFs. These notebooks document a workflow that extracts text and images from the PDFs to build a [searchable database of their contents](https://glam-workbench.net/tasmanian-post-office-directories/).

![Screenshot of the Tasmanian Post Office Directories Search Interface](../images/tas-pod-interface.png)
[**Search for people and places in Tasmania**](https://glam-workbench.net/tasmanian-post-office-directories/)

### [:material-notebook-outline: Download and process Tasmanian Post Office Directory PDFs](tas-pod-save-text-images.md) 
This notebook downloads all 48 Tasmanian Post Office Directory PDFs, then extracts images and text from the PDFs using PyMuPDF.

### [:material-notebook-outline: Upload Tasmanian Post Office Directory images to Amazon s3 for IIIF](tas-pod-upload-images.md) 
This notebook converts the images extracted from the Post Office Directory PDFs into pyramidal TIFFs using pyvips and then uploads them to an Amazon s3 bucket for delivery via IIIF.

### [:material-notebook-outline: Extract text from PDF images using Tesseract](tas-pod-ocr-with-tesseract.md) 
This notebook uses Tesseract (OCR) to extract text directly from the images in the Tasmanian Post Office Directory PDFs.

### [:material-notebook-outline: Add content from the Tasmanian Post Office Directories to an SQLite database](tas-pod-add-to-datasette.md)  
This notebook brings everything together text and images from the Tasmanian Post Office Directories in an SQLite database ready for delivery through Datasette.

See the [GLAM Workbench for more details](https://glam-workbench.github.io/libraries-tasmania/).

<!-- START RUN INFO -->


## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using ARDC Binder

[![Launch on ARDC Binder](../images/launch-ARDC-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [ARDC Binder](https://mybinder.org/) service. This is a free service available to researchers in Australian universities. You'll be asked to log in with your university credentials. Note that sessions will close if you stop using the notebooks, and no data will be preserved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using ARDC Binder](https://glam-workbench.net/using-ardc-binder/) for more details.

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/libraries-tasmania/master/?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [mybinder.org](https://mybinder.org/) service (it might take a little while to load). This is a free service that doesn't require any authentication, but note that sessions will close if you stop using the notebooks, and no data will be preserved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/libraries-tasmania/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name libraries-tasmania -v "$PWD":/home/jovyan/work quay.io/glamworkbench/libraries-tasmania repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv libraries-tasmania`
* Open the new directory" `cd libraries-tasmania`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/libraries-tasmania.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer) for more details.

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}