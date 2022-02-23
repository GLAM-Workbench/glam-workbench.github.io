---
repo_name: australian-commonwealth-hansard
repo_url: https://github.com/GLAM-Workbench/australian-commonwealth-hansard
title: Commonwealth Hansard
---

The proceedings of Australia's Commonwealth Parliament are recorded in Hansard, which is available online through the Parliamentary Library's [ParlInfo](https://parlinfo.aph.gov.au/parlInfo/search/summary/summary.w3p;adv=yes;orderBy=_fragment_number,doc_date-rev;query=Dataset:hansardr,hansardr80;resCount=Default) database. This repository includes Jupyter notebooks to harvest and explore XML formatted versions of Hansard.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/australian-commonwealth-hansard/master?urlpath=lab)

You can access a [harvest of the XML files for both houses from 1901 to 1980 and 1998 to 2005](https://github.com/wragge/hansard-xml) from this repository. No XML files are currently available for 1981 to 1997. Open Australia provides access to [Hansard XML files from 2006 onwards](http://data.openaustralia.org.au/).

The XML files are made available on the Australian Parliament website under a CC-BY-NC-ND licence.

## Tools, tips, and examples

### Convert a year's worth of Historic Hansard into a dataframe for analysis
This notebook analyses Commonwealth Hansard XML files. Give it a year (between 1901 and 1980), and a house (either 'hofreps' or 'senate'), and it will download all the proceedings of that year and house, extract some basic data about debates and speeches, and provide the results as a dataframe for exploration.

* [Download from GitHub](https://github.com/GLAM-Workbench/australian-commonwealth-hansard/blob/master/convert-a-year-to-dataframe.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/australian-commonwealth-hansard/blob/master/convert-a-year-to-dataframe.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/australian-commonwealth-hansard/master?urlpath=lab/tree/convert-a-year-to-dataframe.ipynb)

### Harvesting Commonwealth Hansard
Results in ParlInfo are generated from well-structured XML files which can be downloaded individually from the web interface – one XML file for each sitting day. This notebook shows you how to download all the XML files for large scale analysis. It's an updated version of the code I used to harvest Hansard in 2016.

* [Download from GitHub](https://github.com/GLAM-Workbench/australian-commonwealth-hansard/blob/master/Harvesting-Commonwealth-Hansard.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/australian-commonwealth-hansard/blob/master/Harvesting-Commonwealth-Hansard.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/australian-commonwealth-hansard/master?urlpath=lab/tree/Harvesting-Commonwealth-Hansard.ipynb)

## Data

### List of sitting days, 1901 to 2005

The harvesting process documented in the notebook above, extracts a list of sitting days and XML files from searches in ParlInfo. This [CSV file combines this data for all years and both houses](https://github.com/GLAM-Workbench/australian-commonwealth-hansard/blob/master/data/all-sitting-days.csv). It contains the following fields:

* `date` – date of sitting day in YYYY-MM-DD format
* `url` – url for XML file (where available)
* `year`
* `house` – 'hofreps' or 'senate'

## Contributors

{{ repo_contributors() }}

## Cite as

Sherratt, Tim. (2019, November 17). GLAM-Workbench/australian-commonwealth-hansard (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3544706>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3544706.svg)](https://doi.org/10.5281/zenodo.3544706)
