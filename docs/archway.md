---
repo_name: archway-harvesting
repo_url: https://github.com/GLAM-Workbench/archway-harvesting
---

# Archway

!!! error "Archway is no longer accessible"

    Archives New Zealand have replaced Archway with a new collections database, so the notebooks in this repository **will not work**. I was hoping that the new system would include a public API, but that doesn't seem the case. I will update this section as more information becomes available.

[Archway](https://www.archway.archives.govt.nz/) is the collections database of [Archives New Zealand](http://archives.govt.nz/) and provides rich, contextual information about records, series, agencies, and functions.

Unfortunately Archway doesn't provide access to machine-readable data through an API, so we have to resort to screen scraping.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3544700.svg)](https://doi.org/10.5281/zenodo.3544700)


## Tools, tips, and examples

### Harvesting a records search  
This notebook includes code that will enable you to harvest individual record details from a search in Archway. There's a limit of 10,000 results returned for any search, so if you want to harvest more records than this, you'll need to break your search up into chunks of less than 10,000 — the notebook provides some examples of how you might do this.

* [Download from GitHub](https://github.com/GLAM-Workbench/archway-harvesting/blob/master/archway-records-harvest.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/archway-harvesting/blob/master/archway-records-harvest.ipynb)

### Harvesting functions  
Functions provide an alternative way of finding relevant series and records — zooming out from the records to focus on the government activities you're interested in. Functions also provide an interesting data point to analyse and visualise. This notebook lets you download the functions used by Archway as a dataset.

* [Download from GitHub](https://github.com/GLAM-Workbench/archway-harvesting/blob/master/harvesting_functions_from_archway.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/archway-harvesting/blob/master/harvesting_functions_from_archway.ipynb)

### Who's responsible?
Archives New Zealand divides government activities up into 303 functions. Over time, different agencies have been made responsible for these functions, and it can be interesting to track how these responsibilities have shifted. This notebook uses data about functions harvested from Archway to create a a simple visualisation of the agencies responsible for a selected function.

* [Download from GitHub](https://github.com/GLAM-Workbench/archway-harvesting/blob/master/display_agencies_responsible_for_function.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/archway-harvesting/blob/master/display_agencies_responsible_for_function.ipynb)


![Screen capture](images/nz-agencies-function.gif)

## Contributors

{{ repo_contributors() }}

## Cite as

Sherratt, Tim. (2019, November 17). GLAM-Workbench/archway-harvesting (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3544700>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3544700.svg)](https://doi.org/10.5281/zenodo.3544700)
