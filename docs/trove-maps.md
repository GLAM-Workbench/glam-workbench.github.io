---
title: Trove maps
repo_url: https://github.com/GLAM-Workbench/trove-maps
repo_name: trove-maps
---

The Trove 'map' zone includes single maps, as well as map series, atlases, and aerial photographs. You can access metadata from the map zone through the Trove API.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-maps/master)

## Tips, tools, and examples

### Exploring digitised maps in Trove
If you've ever poked around in Trove's 'map' zone, you might have noticed the beautiful deep-zoomable images available for many of the NLA's digitised maps. Even better, in many cases the high-resolution TIFF versions of the digitised maps are available for download. I knew there were lots of great maps you could download from Trove, but how many? And how big were the files? I thought I'd try to quantify this a bit by harvesting and analysing the metadata.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-maps/blob/master/Exploring-digitised-maps.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-maps/blob/master/Exploring-digitised-maps.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-maps/master?filepath=Exploring-digitised-maps.ipynb)

## Data

### CSV formatted list of maps with high-resolution downloads

Harvested: 26 April 2019

This file provides metadata of 20,158 maps in Trove that have high-resolution downloads. You can [download the CSV file](https://github.com/GLAM-Workbench/trove-maps/blob/master/single_maps.csv), or [browse the metadata using Google Sheets](https://docs.google.com/spreadsheets/d/1yBPcCk9wIRovRacKbfrlyThWrzGXLF79Lr0GIQbaO9Y/edit?usp=sharing).

This file includes the following columns:

+ `copyright_status` - a string indicating the copyright status of the map
+ `creators` – pipe-separated list of contributors/creators
+ `date` – date of the map (format varies)
+ `filesize` – size in bytes
+ `filesize_string` – size as a human-readable string with unit
+ `fulltext_url` – link to the landing page of the digital version
+ `height` – height in pixels
+ `title` – title of the map
+ `trove_id` – digital object identifier
+ `trove_url` – link to the metadata record in Trove
+ `width` – width in pixels

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/trove-maps (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549427>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549427.svg)](https://doi.org/10.5281/zenodo.3549427)
