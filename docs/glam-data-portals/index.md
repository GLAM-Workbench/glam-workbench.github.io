---
title: Gov data portals
repo_name: ozglam-data
repo_url: https://github.com/GLAM-Workbench/ozglam-data
zenodo_concept_id: 3549112
---

# GLAM data from government portals

{{ git_latest_tag() }}

This is an attempt to assemble some useful information about Australian GLAM (Galleries, Libraries, Archives, Museums) datasets.

As a first step, I've harvested GLAM-related datasets from the various national and state data portals.

- [Browse the list of datasets, grouped by organisation](/glam-datasets-from-gov-portals/)
- [Download the harvested metadata](gov-portals-data.md)
- [Search the harvested metadata using Datasette](https://glam-workbench.net/datasette-lite/?csv=https%3A%2F%2Fgithub.com%2FGLAM-Workbench%2Fgov-portals-data%2Fblob%2Fmain%2Fglam-datasets-from-gov-portals.csv&install=datasette-homepage-table&fts=dataset_title%2Cdataset_description%2Cfile_title%2Cfile_description)
- Explore the *contents* of the CSV-formatted datasets using the [GLAM CSV Explorer](https://glam-workbench.github.io/csv-explorer/)
- Search across 279 datasets containing names using the [GLAM Name Index Search](https://glam-workbench.net/name-search/)

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}h/HEAD?urlpath=lab/tree/index.ipynb)

## Notebooks

### Harvesting GLAM data from government portals
This notebook attempts to harvest the details of GLAM datasets from state and national data portals. I did this by identifying relevant organisations, tags, and queries, and then harvesting all the packages associated with them. It also attempts some analysis of the results.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam_data_from_gov_portals.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/glam_data_from_gov_portals.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/glam_data_from_gov_portals.ipynb)

### Harvest GLAM datasets from data.gov.au (deprecated)
This is a quick attempt to harvest datasets published by GLAM institutions using the new [data.gov.au](https://data.gov.au/) API. To create the list of organisations, I searched the organisations on the data.gov.au site for 'library', 'archives', 'records', and 'museum'. **Note** that due to a problem with duplicates on data.gov.au, I'm no longer using this notebook to harvest the data.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/harvest_glam_datasets_from_datagovau.ipynb)

## Data

### [:material-folder-outline: GLAM datasets in government data portals](gov-portals-data.md) {: data-toc-omit }

*Harvested 21 October 2024*

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
