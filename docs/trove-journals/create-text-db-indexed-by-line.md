---
title: Create a database to search across each line of text in a series of volumes
description: Using this notebook you can index any publication where it would be useful to search by line (rather than Trove's default 'article') – for example, lists, directories and gazetteers – turning them into searchable databases.
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
zenodo_concept_id: 3545215
tags:
  - data harvesting
  - Datasette
hide:
  - toc
---

The code in this notebook was used to create the [NSW Post Office Directories search interface](https://nsw-post-office-directories-yajhxrvxsa-ts.a.run.app/) which lets you search across 54 volumes from 1886 to 1950. The same code, with minor modifications, could be used to index any series of publication where it would be useful to search by line (rather than Trove's default 'article') – for example, lists, directories and gazetteers – turning them into searchable databases.

The notebook assembles information about each volume in a series. It downloads OCRd text for each volume page by page, and matches it with a page identifier so that you can construct links back to Trove. The text and metadata are loaded into a SQLite database and the text is indexed. This database can be viewed using [Datasette](https://datasette.io/).


[Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?urlpath=lab/tree/index-each-line-in-series.ipynb){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/index-each-line-in-series.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/index-each-line-in-series.ipynb)

### Related resources

* [NSW Post Office Directories, 1886 to 1950](../../nsw-post-office-directories/)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}