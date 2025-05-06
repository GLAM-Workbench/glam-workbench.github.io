---
title: Te Papa
repo_url: https://github.com/GLAM-Workbench/te-papa-api
repo_name: te-papa-api
zenodo_concept_id: 3549094
---

# Te Papa collections

{{ git_latest_tag() }}

Te Papa has a [very well-documented API](https://data.tepapa.govt.nz/docs/index.html) that provides rich information about its collection and the relationships between collection items and other entities, including people and places.

You'll need [an API key](https://data.tepapa.govt.nz/docs/register.html) for serious exploration.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### Exploring the Te Papa collection API  
This notebook is just a preliminary exploration of the API. It drills down through some of the facets to try and get a picture of what data is available.

* [Download from GitHub](https://github.com/GLAM-Workbench/te-papa-api/blob/master/Exploring-the-Te-Papa-collection-API.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/te-papa-api/blob/master/Exploring-the-Te-Papa-collection-API.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab%2Ftree%2FExploring-the-Te-Papa-collection-API.ipynb)

### Mapping Te Papa's collections
This notebook creates some simple maps using the `production.spatial` facet of the Te Papa API to identify places where collection objects were created.

* [Download from GitHub](https://github.com/GLAM-Workbench/te-papa-api/blob/master/Mapping-Te-Papa-collections.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/te-papa-api/blob/master/Mapping-Te-Papa-collections.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/te-papa-api/master?urlpath=lab%2Ftree%2FMapping-Te-Papa-collections.ipynb)

![Screen capture](images/tepapa-map.png)

<!-- START RUN INFO -->

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
