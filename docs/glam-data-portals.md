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

You can [browse a list of datasets](/glam-datasets-from-gov-portals/), or [download a CSV](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv) containing all the harvested data or [just the CSVs](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv). You can also [search the harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets) using Datasette on Glitch.

To start exploring the *contents* of the datasets, give the [GLAM CSV Explorer](https://glam-workbench.github.io/csv-explorer/) a spin.

To search across 253 datasets containing names, try the [GLAM Name Index Search](https://glam-workbench.net/name-search/).

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master)

## Tools, tips, and examples

### Harvesting GLAM data from government portals
This notebook attempts to harvest the details of GLAM datasets from state and national data portals. I did this by identifying relevant organisations, tags, and queries, and then harvesting all the packages associated with them. It also attempts some analysis of the results.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam_data_from_gov_portals.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/glam_data_from_gov_portals.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/glam_data_from_gov_portals.ipynb)

### Harvest GLAM datasets from data.gov.au
This is a quick attempt to harvest datasets published by GLAM institutions using the new [data.gov.au](https://data.gov.au/) API. To create the list of organisations, I searched the organisations on the data.gov.au site for 'library', 'archives', 'records', and 'museum'. **Note** that due to a problem with duplicates on data.gov.au, I'm no longer using this notebook to harvest the data.

* [Download from GitHub](https://github.com/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/ozglam-data/blob/master/harvest_glam_datasets_from_datagovau.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/ozglam-data/master?urlpath=lab/tree/harvest_glam_datasets_from_datagovau.ipynb)

## Data

### Results (14 August 2022)

* Browse a [list of all GLAM datasets harvested from government data portals](/glam-datasets-from-gov-portals/)
* Search the [harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets) using Datasette on Glitch.
* Download [GLAM datasets from government data portals – all formats (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv)
* Download [GLAM datasets from government data portals – CSVs only (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv)

#### Summary

Number of datasets: 463 (datasets can contain multiple files)  
Number of files: 1192

Files by organisation:

```
State Library of Queensland                                                        304
Queensland State Archives                                                          204
State Library of South Australia                                                   136
State Records Office of Western Australia                                           86
Libraries Tasmania                                                                  85
South Australian Museum                                                             74
State Library of Western Australia                                                  73
Public Records Office Victoria                                                      62
Queensland Museum                                                                   51
State Records South Australia                                                       30
History Trust of South Australia                                                    20
NSW State Archives                                                                  19
Western Australian Museum                                                           18
State Library of NSW                                                                 5
National Library of Australia                                                        5
State Library of Victoria                                                            5
Museum of Applied Arts and Sciences                                                  4
National Archives of Australia                                                       3
Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS)      3
Mount Gambier Library                                                                2
National Portrait Gallery                                                            2
Museums Victoria                                                                     1
```

Files by format:

```
CSV                              752
JSON                              78
XML                               61
JPG                               53
XLSX                              51
IMG                               37
RTF                               16
JPEG                              15
HTML                              12
website link                      10
DOC                               10
API                               10
ZIP                               10
DOCX                               9
TXT                                9
GeoJSON                            7
OBJ                                7
MTL                                5
API ArcGIS Server Map Service      4
Mixed Formats                      4
GeoPackage                         3
SHP                                3
FGDB                               3
KML                                2
WMS                                2
PDF                                2
                                   2
GEOJSON                            2
Website                            1
TIF                                1
app                                1
JS                                 1
MUSEUM                             1
api                                1
RSS                                1
CSS, Java, PHP, JavaScript         1
.txt                               1
XSD                                1
plain                              1
page                               1
WFS                                1                              
```

Files by licence:

```
Creative Commons Attribution 4.0                                      646
Creative Commons Attribution                                          277
Creative Commons Attribution 4.0 International                        127
                                                                       77
Creative Commons Attribution 2.5 Australia                             27
Creative Commons Attribution-NonCommercial                              9
Creative Commons Attribution 3.0 Australia                              8
Creative Commons Attribution 3.0                                        7
Other (Open)                                                            4
notspecified                                                            3
Creative Commons Attribution Share-Alike 4.0                            3
Creative Commons Attribution Non-Commercial 4.0                         2
Custom (Other)                                                          1
Creative Commons Attribution No Derivative Works 4.0 International      1                                                          1
```

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
