---
title: Find and explore Powerpoint presentations from a specific domain
description: This notebook helps you find, download, and explore all the presentation files captured from a particular domain, like `defence.gov.au`.
repo_url: https://github.com/GLAM-Workbench/web-archives
repo_name: web-archives
zenodo_concept_id: 3894078
tags:
  - API
  - data harvesting
  - web archives
hide:
  - toc
---

*Works with IA*

![Title slide from presentation](../images/au-gov-defence-army-hna-docs-hna-20general-20presentation-ppt-20070911062046.png)![Title slide from presentation](../images/au-gov-defence-army-hna-docs-ncw-20model-ppt-20070911061846.png)

This notebook helps you find, download, and explore all the presentation files captured from a particular domain, like `defence.gov.au`. It includes a series of processing steps to: harvest capture data; remove duplicates from capture data and download files; convert Powerpoint files to PDFs; extract screenshots and text from the PDFs; save metadata, screenshots, and text into an SQLite database; open the SQLite db in Datasette for exploration. Here's an [example of the SQLite database](https://defencegovau-powerpoints.glitch.me/) created by harvesting Powerpoint files from the `defence.gov.au` domain, running in Datasette on Glitch.

[Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/web-archives/master?urlpath=/lab/tree/explore_presentations.ipynb){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/web-archives/blob/master/explore_presentations.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/web-archives/blob/master/explore_presentations.ipynb)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}