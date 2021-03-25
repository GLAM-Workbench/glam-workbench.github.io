---
title: Trove lists
repo_url: https://github.com/GLAM-Workbench/trove-lists
repo_name: trove-lists
---

Trove lists are user created collections of items. The details of public lists are available through the Trove API.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab)

## Tips, tools, and examples

### Convert a Trove list into a CSV file  
This notebook converts Trove lists into CSV files (spreadsheets). Separate CSV files are created for newspaper articles and works from Trove's other zones. You can also save the OCRd text, a PDF, and an image of each newspaper article.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/Convert-a-Trove-list-into-a-CSV-file.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/Convert-a-Trove-list-into-a-CSV-file.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/Convert-a-Trove-list-into-a-CSV-file.ipynb)

### Harvest summary data from Trove lists
Use the Trove API to harvest data about all public lists, then extract some summary data and explore a few different techniques to analyse the complete dataset.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/Harvest-summary-data-from-lists.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/Harvest-summary-data-from-lists.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/Harvest-summary-data-from-lists.ipynb)

![Screen shot of word cloud](images/trove-lists.png)

## Data

### Trove lists metadata

Harvested: 20 September 2018

[CSV formatted file](https://github.com/GLAM-Workbench/trove-lists/blob/master/data/trove-lists-2018-09-20.csv) containing the following fields:  

+ `created` – date list created
+ `id` – list identifier
+ `number_items` – number of items in list
+ `title` – title of list
+ `updated` – date last updated

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/trove-lists (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549454>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549454.svg)](https://doi.org/10.5281/zenodo.3549454)
