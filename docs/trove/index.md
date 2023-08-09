---
title: Trove API introduction
description: The notebooks in this section provide examples of using the main Trove API to harvest data and analyse the contents of Trove resources.
repo_url: https://github.com/GLAM-Workbench/trove-api-intro
repo_name: trove-api-intro
zenodo_concept_id: 3549550
---

Trove provides access to much of its data through APIs (Application Programming Interfaces). These include:

* the main Trove API delivers data from aggregated collections, digitised resources (including newspapers), and user activity (such as lists and tags)
* OAI-PMH and SRU APIs deliver data from the Trove People and organisations zone
* [Memento and CDX APIs](/web-archives/) deliver data from the Australian Web Archive

The notebooks in this section provide examples of using the main Trove API to harvest data and analyse the contents of Trove resources. You'll find more examples throughout the Trove sections of the GLAM Workbench. For help building your own Trove API requests, try the [Trove API Console](http://troveconsole.herokuapp.com/).

Before you can use the API you need to obtain a key — it's free and quick. Just [follow these instructions](https://trove.nla.gov.au/about/create-something/using-api).

## What's an API?

An API is an Application Programming Interface. It's a set of predefined requests and responses that enables computer programs talk to each other.

Web APIs are generally used to deliver data. While humans can easily interpret information on a web page, computers need more help. APIs provide data in a form that computers can understand and use (we call this machine-readable data).

The Trove API works much like the Trove website. You make queries and you get back results. But instead of going through a nicely-designed web interface, requests to the API are just URLs, and the results are just structured data.

While you can just type an API request into the location box of your web browser, most of the time requests and responses will be handled by a computer script or program. APIs don't care what programming language you use as long as you structure requests in the way they expect.

In these notebooks we'll be using the programming language Python. No prior knowledge of Python is expected or required – just follow along! The examples and approaches used could be easily translated into any another programming language.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-api-intro/master)

## Tools, tips, examples

### [:material-notebook-outline: Your first Trove API request](your-first-api-request.md) {: data-toc-omit }
In this notebook we're going to learn how to send a request for information to the Trove API. API requests are just like normal urls. However, instead of sending us back a web page, they deliver data in a form that computers can understand. We can then use that data in our own programs.

### [:material-notebook-outline: Working with Trove zones](working-with-zones.md) {: data-toc-omit }
Trove's zones are important in constructing API requests and interpreting the results. So let's explore them a bit.

### [:material-notebook-outline: Exploring Trove facets](exploring-facets.md) {: data-toc-omit }
Facets aggregate collection data in interesting and useful ways, allowing us to build pictures of the collection. This notebook shows you how to get facet data from Trove.

## Useful links

*   [Trove API Documentation](http://help.nla.gov.au/trove/building-with-trove/api-version-2-technical-guide)
*   [Trove API console](http://troveconsole.herokuapp.com/)
*   [Introduction to using APIs](https://github.com/staplegun/using-apis)

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-api-intro/master/)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-api-intro/master/reclaim-manifest.jps)

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
  docker run -p 8888:8888 --name trove-api-intro quay.io/glamworkbench/trove-api-intro repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='''
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv trove-api-intro`
* Open the new directory" `cd trove-api-intro`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/trove-api-intro.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See [Getting started](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer) for more details.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

