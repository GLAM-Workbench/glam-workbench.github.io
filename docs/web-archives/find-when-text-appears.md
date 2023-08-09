---
title: Find when a piece of text appears in an archived web page
description: This notebook helps you find when a particular piece of text appears in, or disappears from, a web page.
repo_url: https://github.com/GLAM-Workbench/web-archives
repo_name: web-archives
zenodo_concept_id: 3894078
tags:
  - API
  - web archives
  - text analysis
hide:
  - toc
---

*Works with AWA, IA, NLNZ, UKWA, & UKGWA*

![Animated gif showing notebook in action](../images/web-archives-text-appearance.gif)

This notebook helps you find when a particular piece of text appears in, or disappears from, a web page. Using Memento Timemaps, it gets a list of available captures from the selected web archive. It then searches each capture for the desired text, displaying the results. You can select the direction in which the notebook searches:

* First occurrence – find the first capture in which the text appears (start from the first capture and come forward in time)
* Last occurrence – find the last capture in which the text appears (start from present and go backwards in time)
* All occurrences – find all matches (start from the first capture and continue until the last)

If you select 'All occurrences' the notebook will generate a simple chart showing how the number of matches changes over time.

[Run live in Voila on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/web-archives/master?urlpath=/voila/render/find-text-in-page-from-timemap.ipynb){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/web-archives/blob/master/find-text-in-page-from-timemap.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/web-archives/blob/master/find-text-in-page-from-timemap.ipynb)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}

--8<-- "web-archives-sponsor.md"