---
title: Trove lists and tags
repo_url: https://github.com/GLAM-Workbench/trove-lists
repo_name: trove-lists
---

Trove lists and tags are created by Trove users to organise and describe resources. The details of public lists and tags are available through the Trove API.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab)

## Lists

### Convert a Trove list into a CSV file  
This notebook converts Trove lists into CSV files (spreadsheets). Separate CSV files are created for newspaper articles and works from Trove's other zones. You can also save the OCRd text, a PDF, and an image of each newspaper article.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/Convert-a-Trove-list-into-a-CSV-file.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/Convert-a-Trove-list-into-a-CSV-file.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/Convert-a-Trove-list-into-a-CSV-file.ipynb)

### Convert a Trove list into a CollectionBuilder exhibition  
This notebook converts Trove lists into a series of files that can be uploaded to a [CollectionBuilder-GH](https://github.com/CollectionBuilder/collectionbuilder-gh) repository to create an instant exhibition. See the [CollectionBuilder site](https://collectionbuilder.github.io/) for more information on how CollectionBuilder works and what it can do.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/convert-list-to-cb-exhibition.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/convert-list-to-cb-exhibition.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/convert-list-to-cb-exhibition.ipynb)
* [Demonstration exhibition](https://wragge.github.io/trove-wragge-list-demo/) generated from this [Trove list](https://trove.nla.gov.au/list/83777)

### Harvest summary data from Trove lists
Use the Trove API to harvest data about all public lists, then extract some summary data and explore a few different techniques to analyse the complete dataset.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/Harvest-summary-data-from-lists.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/Harvest-summary-data-from-lists.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/Harvest-summary-data-from-lists.ipynb)

![Screen shot of word cloud](images/trove-lists.png)

## Tags

### Harvest public tags from Trove zones  
This notebook uses the Trove API to assemble a dataset containing all public tags added to Trove.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/harvest-tags.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/harvest-tags.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/harvest-tags.ipynb)

### Analyse public tags added to Trove  
This notebook loads the complete dataset of Trove tags and explores some ways of analysing and visualising the tag data.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-lists/blob/master/analyse_tags.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-lists/blob/master/analyse_tags.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-lists/master?urlpath=lab/tree/analyse_tags.ipynb)

## Data

### Trove lists metadata

Harvested: 22 September 2020

[CSV formatted file](https://github.com/GLAM-Workbench/trove-lists/blob/master/data/trove-lists-2020-09-22.csv) containing the following fields:  

+ `created` – date list created
+ `id` – list identifier
+ `number_items` – number of items in list
+ `title` – title of list
+ `updated` – date last updated

### Trove public tags

Harvested: 10 July 2021

Zipped CSV file (123mb) [available from Zenodo](https://doi.org/10.5281/zenodo.5094314).

### Trove tag counts

Harvested: 10 July 2021

[CSV file](https://github.com/GLAM-Workbench/trove-lists/blob/master/trove_tag_counts_20210710.csv) containing the total number of times each tag in Trove has been applied to resources.

## Contributors

{{ repo_contributors() }}

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/trove-lists (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549453>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549454.svg)](https://doi.org/10.5281/zenodo.3549454)
