---
title: Gov data portals
repo_name: OzGLAM data
repo_url: https://github.com/GLAM-Workbench/ozglam-data
---

# GLAM data from government portals

This is an attempt to assemble some useful information about Australian GLAM (Galleries, Libraries, Archives, Museums) datasets.

As a first step, I've harvested GLAM-related datasets from the various national and state data portals.

You can [browse a list of datasets](/glam-datasets-from-gov-portals/), or [download a CSV](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv) containing all the harvested data or [just the CSVs](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv). You can also [search the harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets-from-gov-portals) using Datasette on Glitch.

To start exploring the *contents* of the datasets, give the [GLAM CSV Explorer](https://glam-workbench.github.io/csv-explorer/) a spin.

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

### Results (30 March 2020)

* Browse a [list of all GLAM datasets harvested from government data portals](/glam-datasets-from-gov-portals/)
* Search the [harvested data](https://ozglam-datasets.glitch.me/data/glam-datasets-from-gov-portals) using Datasette on Glitch.
* Download [GLAM datasets from government data portals – all formats (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals.csv)
* Download [GLAM datasets from government data portals – CSVs only (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam-datasets-from-gov-portals-csvs.csv)

#### Summary

Number of datasets: 369 (datasets can contain multiple files)  
Number of files: 983

Files by organisation:

```
State Library of Queensland                                                        240
Queensland State Archives                                                          166
State Library of South Australia                                                   134
Libraries Tasmania                                                                  83
South Australian Museum                                                             74
State Library of Western Australia                                                  72
Public Records Office Victoria                                                      46
Queensland Museum                                                                   46
State Records South Australia                                                       30
History Trust of South Australia                                                    20
NSW State Archives                                                                  19
Western Australian Museum                                                           13
State Records Office of Western Australia                                            7
National Library of Australia                                                        5
State Library of Victoria                                                            5
State Library of NSW                                                                 5
Australian Museum                                                                    4
National Archives of Australia                                                       3
Museum of Applied Arts and Sciences                                                  3
Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS)      3
Mount Gambier Library                                                                2
National Portrait Gallery                                                            2
Museums Victoria                                                                     1
```

Files by format:

```
CSV                              628
JSON                              78
XML                               60
XLSX                              51
JPG                               17
ZIP                               17
JPEG                              15
HTML                              12
RTF                               11
DOC                               10
API                               10
TXT                                9
DOCX                               8
website link                       7
OBJ                                7
MTL                                5
GeoJSON                            4
Mixed Formats                      4
KML                                3
PDF                                3
GEOJSON                            3
RSS                                2
API ArcGIS Server Map Service      2
api                                2
plain                              1
WFS                                1
                                   1
.txt                               1
Website                            1
CSS, Java, PHP, JavaScript         1
MUSEUM                             1
PHP                                1
XSD                                1
JS                                 1
WMS                                1
RDF                                1
MPK                                1
page                               1
app                                1
```

Files by licence:

```
Creative Commons Attribution 4.0                   527
Creative Commons Attribution                       278
Creative Commons Attribution 4.0 International     113
Creative Commons Attribution 2.5 Australia          24
Creative Commons Attribution-NonCommercial           9
Creative Commons Attribution 3.0 Australia           8
Creative Commons Attribution 3.0                     7
Other (Open)                                         4
                                                     4
Creative Commons Attribution Share-Alike 4.0         3
notspecified                                         3
Creative Commons Attribution Non-Commercial 4.0      2
Custom (Other)                                       1
```

### Results (July 2019)

* [Human readable list of all GLAM datasets harvested from data.gov.au](https://github.com/GLAM-Workbench/glam-data-list/blob/master/glam_datasets_from_datagovau.md)
* [GLAM datasets from data.gov.au – all formats (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam_datasets_all_formats_from_datagovau.csv)
* [GLAM datasets from data.gov.au – CSVs only (CSV)](https://github.com/GLAM-Workbench/ozglam-data/blob/master/glam_datasets_csvs_from_datagovau.csv)

Files by format:

```
CSV           586
XML            81
JSON           74
XLSX           61
DOCX           34
HTML           33
PLAIN          14
ZIP            14
API             9
GEOJSON         8
DATA            6
OTHER           4
PDF             4
KML             3
RSS             2
JPEG            2
RDF             1
HMTL            1
WFS             1
TXT             1
APP             1
JAVASCRIPT      1
CSS             1
WMS             1
PAGE            1
```

Files by organisation:

```
State Library of Queensland                                                        204
Queensland State Archives                                                          172
State Library of Western Australia                                                 147
State Library of South Australia                                                   140
Libraries Tasmania                                                                  71
State Records                                                                       41
PROV Public Record Office                                                           33
South Australian Museum                                                             33
State Library of New South Wales                                                    21
NSW State Archives                                                                  19
History Trust of South Australia                                                    19
State Records Office of Western Australia                                            7
State Library of NSW                                                                 6
Western Australian Museum                                                            6
National Library of Australia                                                        5
State Library of Victoria                                                            5
Australian Museum                                                                    4
Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS)      3
National Archives of Australia                                                       3
Museum of Applied Arts and Sciences                                                  3
Mount Gambier Library                                                                2
Tasmanian Museum and Art Gallery                                                     2
National Portrait Gallery                                                            2
```

Files by licence:

```
Creative Commons Attribution                       250
Creative Commons Attribution 3.0 Australia         244
Creative Commons Attribution 4.0                   237
Creative Commons Attribution 4.0 International     146
Creative Commons Attribution 2.5 Australia          32
Creative Commons Attribution-NonCommercial          10
Other (Open)                                         5
notspecified                                         5
Creative Commons Attribution Share-Alike 4.0         3
Creative Commons Attribution 3.0                     3
Creative Commons Attribution Non-Commercial 4.0      2
Custom (Other)                                       1
```

### Results (April 2018)

Here's a [CSV containing details of **all** the datasets](https://github.com/GLAM-Workbench/ozglam-data/blob/master/gov-glam-datasets-all-formats.csv) I found. I've also [uploaded it](https://docs.google.com/spreadsheets/d/1OUbgQPRWnDLOvr8Wes0E-UAno1mk_8f12PFd08pVGGo/edit?usp=sharing) to Google Sheets.

There are duplicates in the data because some datasets are listed on more than one portal. While my interest is in datasets containing collection data, the list also includes datasets created by the operations of GLAM organisations, such as borrowing data or FOI reports. I might filter these out later on.

There are currently 790 files in this list.

Here's the number of files by data portal:

```
data.gov.au        271
data.qld.gov.au    214
data.sa.gov.au     173
data.wa.gov.au      96
data.nsw.gov.au     30
data.vic.gov.au      6
```

And the number of files by organisation:

```
State Library of South Australia                      121
Housing and Public Works                              117
State Library of Western Australia                    114
Natural Resources, Mines and Energy                    79
State Library of Queensland                            78
LINC Tasmania                                          74
State Records                                          41
State Records Office of Western Australia              41
South Australian Governments                           26
State Library of New South Wales                       21
State Archives NSW                                     19
Environment and Science                                14
History Trust of South Australia                       12
State Library of NSW                                    6
State Library of Victoria                               6
National Library of Australia                           5
Aboriginal and Torres Strait Islander Partnerships      4
Museum of Applied Arts and Sciences                     3
National Archives of Australia                          3
National Portrait Gallery                               2
Mount Gambier Library                                   2
Australian Museum                                       1
City of Sydney                                          1
```

I've attempted to identify the format of each file by checking the file extension. If there's no file extension I use the `format` value in the package metadata. These values don't always seem reliable. Here's the number of datasets by format:

```
csv                           499
xml                            66
wms                            35
xlsx                           27
json                           25
docx                           17
xls                            16
txt                            15
zip                            14
doc                            12
api                            12
geojson                         8
other                           7
data                            6
pdf                             4
jpg                             2
html                            2
rss                             2
website link                    2
kml                             2
rtf                             2
kmz                             1
css, java, php, javascript      1
php                             1
xsd                             1
csv, json, web services         1
mp3                             1
js                              1
museum                          1
website                         1
app                             1
jpeg                            1
url                             1
.txt                            1
wfs                             1
plain                           1
```

For each dataset, I've fired off a `HEAD` request for the url to see if the link still works. Here's the number of datasets by HTTP status code  (`200` is ok, `404` is not found):

```
200    746
404     39
400      3
403      2
```

I've created [a CSV of **just the CSV-formatted** datasets](https://github.com/GLAM-Workbench/ozglam-data/blob/master/gov-glam-datasets.csv). I've also [uploaded it](https://docs.google.com/spreadsheets/d/1gCcLZEe-pdYEn8DfLrhM9WwfJ2jgfPV39ZRiodzhm78/edit?usp=sharing) to Google Sheets.

There are 499 CSV-formatted datasets in this list.

Here are results of the HEAD requests for CSV-formatted datasets:

```
200    493
404      4
400      2
```

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/ozglam-data (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549113>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549113.svg)](https://doi.org/10.5281/zenodo.3549113)
