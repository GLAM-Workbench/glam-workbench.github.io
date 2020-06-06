---
title: DigitalNZ
repo_url: https://github.com/GLAM-Workbench/digitalnz
repo_name: digitalnz
---

[DigitalNZ](https://digitalnz.org/) aggregates collections from across New Zealand and makes the aggregated metadata available [through an API](https://digitalnz.org/developers).

You'll need an [API key](https://digitalnz.org/developers/getting-started) to work with DigitalNZ data.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/digitalnz/master)

## Tips, tools, and examples

### Getting some top-level data from the DigitalNZ API  
This notebook pokes around at the top-level of DigitalNZ, mainly using facets to generate some collection overviews and summaries.

* [Download from GitHub](https://github.com/GLAM-Workbench/digitalnz/blob/master/Top-level-data-in-DigitalNZ.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/digitalnz/blob/master/Top-level-data-in-DigitalNZ.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/digitalnz/master?filepath=Top-level-data-in-DigitalNZ.ipynb)

### Find results by country in DigitalNZ
Many items in DigtalNZ include location information. This can include a country, but as far as I can see there's no direct way to search for results relating to a particular country using the API. You can, however, search for geocoded locations using bounding boxes. This notebook shows how you can use this to search for countries.

* [Download from GitHub](https://github.com/GLAM-Workbench/digitalnz/blob/master/Results-by-country-in-DigitalNZ.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/digitalnz/blob/master/Results-by-country-in-DigitalNZ.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/digitalnz/master?filepath=Results-by-country-in-DigitalNZ.ipynb)

![Map showing frequency of DigitalNZ locations](images/digitalnz_map.png)

### Visualise a search in Papers Past
Start with some keywords you want to search for in [Papers Past](https://paperspast.natlib.govt.nz/), then create a simple visualisation showing the distribution over time and by newspaper.  

* [Download from GitHub](https://github.com/GLAM-Workbench/digitalnz/blob/master/Visualise-a-search-in-PapersPast.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/digitalnz/blob/master/Visualise-a-search-in-PapersPast.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/digitalnz/master?filepath=Visualise-a-search-in-PapersPast.ipynb)

![Chart visualising Papers Past results](images/digitalnz.png)

### Harvest data from Papers Past  
This notebooks lets you harvest large amounts of data for [Papers Past](https://paperspast.natlib.govt.nz/) (via DigitalNZ) for further analysis. It saves the results as a CSV file that you can open in any spreadsheet program. It currently includes the OCRd text of all the newspaper articles.

* [Download from GitHub](https://github.com/GLAM-Workbench/digitalnz/blob/master/Harvest-data-from-PapersPast.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/digitalnz/blob/master/Harvest-data-from-PapersPast.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/digitalnz/master?filepath=Harvest-data-from-PapersPast.ipynb)


# Cite as

Sherratt, Tim. (2019, November 17). GLAM-Workbench/digitalnz (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3544729>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3544729.svg)](https://doi.org/10.5281/zenodo.3544729)
