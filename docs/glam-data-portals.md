---
title: Gov data portals
repo_name: ozglam-data
repo_url: https://github.com/GLAM-Workbench/ozglam-data
---

# GLAM data from government portals

This is an attempt to assemble some useful information about Australian GLAM (Galleries, Libraries, Archives, Museums) datasets.

As a first step, I've harvested GLAM-related datasets from the various national and state data portals.

You can [browse a list of datasets](/glam-datasets-from-gov-portals/), or [download a CSV](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv) containing all the harvested data or [just the CSVs](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv). You can also [search the harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets) using Datasette on Glitch.

To start exploring the *contents* of the datasets, give the [GLAM CSV Explorer](https://glam-workbench.github.io/csv-explorer/) a spin.

To search across 195 datasets containing names, try the [GLAM Name Index Search](https://glam-workbench.net/name-search/).

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master)

## Tools, tips, and examples

### Harvesting GLAM data from government portals
This notebook attempts to harvest the details of GLAM datasets from state and national data portals. I did this by identifying relevant organisations, tags, and queries, and then harvesting all the packages associated with them. It also attempts some analysis of the results.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/GLAM%20data%20from%20gov%20portals.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/GLAM%20data%20from%20gov%20portals.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/GLAM%20data%20from%20gov%20portals.ipynb)

### Harvest GLAM datasets from data.gov.au
This is a quick attempt to harvest datasets published by GLAM institutions using the new [data.gov.au](https://data.gov.au/) API. To create the list of organisations, I searched the organisations on the data.gov.au site for 'library', 'archives', 'records', and 'museum'. **Note** that due to a problem with duplicates on data.gov.au, I'm no longer using this notebook to harvest the data.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/harvest_glam_datasets_from_datagovau.ipynb)

## Data

### Results (16 October 2021)

* Browse a [list of all GLAM datasets harvested from government data portals](/glam-datasets-from-gov-portals/)
* Search the [harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets) using Datasette on Glitch.
* Download [GLAM datasets from government data portals – all formats (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv)
* Download [GLAM datasets from government data portals – CSVs only (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv)

#### Summary

Number of datasets: 413 (datasets can contain multiple files)  
Number of files: 1076

Files by organisation:

```
State Library of Queensland                                                   277
Queensland State Archives                                                     197
State Library of South Australia                                              135
Libraries Tasmania                                                             85
South Australian Museum                                                        74
State Library of Western Australia                                             73
Public Records Office Victoria                                                 56
Queensland Museum                                                              49
State Records South Australia                                                  30
History Trust of South Australia                                               20
NSW State Archives                                                             19
Western Australian Museum                                                      19
State Records Office of Western Australia                                      13
State Library of NSW                                                            5
State Library of Victoria                                                       5
National Library of Australia                                                   5
National Archives of Australia                                                  3
Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS) 3
Museum of Applied Arts and Sciences                                             3
Mount Gambier Library                                                           2
National Portrait Gallery                                                       2
Museums Victoria                                                                1
```

Files by format:

```
CSV                              711
JSON                              78
XML                               61
XLSX                              50
ZIP                               22
JPG                               17
JPEG                              15
RTF                               15
HTML                              12
API                               10
DOC                               10
TXT                                9
DOCX                               8
website link                       7
OBJ                                7
MTL                                5
API ArcGIS Server Map Service      4
GeoJSON                            4
Mixed Formats                      4
KML                                2
WMS                                2
RSS                                2
GEOJSON                            2
                                   2
PDF                                2
TIF                                1
JS                                 1
MPK                                1
plain                              1
WFS                                1
.txt                               1
api                                1
PHP                                1
page                               1
CSS, Java, PHP, JavaScript         1
Website                            1
RDF                                1
XSD                                1
MUSEUM                             1
app                                
```

Files by licence:

```
Creative Commons Attribution 4.0                                      611
Creative Commons Attribution                                          275
Creative Commons Attribution 4.0 International                        121
Creative Commons Attribution 2.5 Australia                             27
Creative Commons Attribution-NonCommercial                              9
Creative Commons Attribution 3.0 Australia                              8
Creative Commons Attribution 3.0                                        7
                                                                        4
Other (Open)                                                            4
notspecified                                                            3
Creative Commons Attribution Share-Alike 4.0                            3
Creative Commons Attribution Non-Commercial 4.0                         2
Creative Commons Attribution No Derivative Works 4.0 International      1
Custom (Other)                                                          1
```


## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/ozglam-data (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549113>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549113.svg)](https://doi.org/10.5281/zenodo.3549113)
