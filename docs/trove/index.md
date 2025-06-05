---
title: Trove API introduction
description: The notebooks in this section provide examples of using the main Trove API to harvest data and analyse the contents of Trove resources.
repo_url: https://github.com/GLAM-Workbench/trove-api-intro
repo_name: trove-api-intro
zenodo_concept_id: 3549550
---

{% include "trove-notice.md" %}

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

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab/)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab/)

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

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

