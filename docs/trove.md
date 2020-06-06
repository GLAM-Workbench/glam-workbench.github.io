---
title: Trove API introduction
repo_url: https://github.com/GLAM-Workbench/trove-api-intro
repo_name: trove-api-intro
---

Trove provides access to much of it's data through an API (Application Programming Interface). The notebooks in this section provide many examples of using the API to harvest data and analyse the contents of Trove.

Before you can use the API you need to obtain a key — it's free and quick. Just [follow these instructions](http://help.nla.gov.au/trove/building-with-trove/api).

## What's an API?

An API is an Application Programming Interface. It's a set of predefined requests and responses that enables computer programs talk to each other.

Web APIs are generally used to deliver data. While humans can easily interpret information on a web page, computers need more help. APIs provide data in a form that computers can understand and use (we call this machine-readable data).

The Trove API works much like the Trove website. You make queries and you get back results. But instead of going through a nicely-designed web interface, requests to the API are just URLs, and the results are just structured data.

While you can just type an API request into the location box of your web browser, most of the time requests and responses will be handled by a computer script or program. APIs don't care what programming language you use as long as you structure requests in the way they expect.

In these notebooks we'll be using the programming language Python. No prior knowledge of Python is expected or required -- just follow along! The examples and approaches used could be easily translated into any another programming language.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-api-intro/master)

## Tools, tips, examples

### [Your first API request](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-api-intro/blob/master/Your-first-API-request.ipynb)  
In this notebook we're going to learn how to send a request for information to the Trove API. API requests are just like normal urls. However, instead of sending us back a web page, they deliver data in a form that computers can understand. We can then use that data in our own programs.

### [Working with zones](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-api-intro/blob/master/Working-with-zones.ipynb)  
Trove's zones are important in constructing API requests and interpreting the results. So let's explore them a bit.

### [Exploring facets](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-api-intro/blob/master/Exploring-facets.ipynb)  
Facets aggregate collection data in interesting and useful ways, allowing us to build pictures of the collection. This notebook shows you how to get facet data from Trove.)

## Useful links

*   [Trove API Documentation](http://help.nla.gov.au/trove/building-with-trove/api-version-2-technical-guide)
*   [Trove API console](http://troveconsole.herokuapp.com/)
*   [Introduction to using APIs](https://github.com/staplegun/using-apis)

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/trove-api-intro (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549551>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549551.svg)](https://doi.org/10.5281/zenodo.3549551)
