---
title: Convert a HTML finding aid to JSON
description: This notebook scrapes data from the HTML of a finding aid, saving the hierarchy of series, sub-series, and items as a list of nested objects. The results can be saved as a JSON file.
repo_url: https://github.com/GLAM-Workbench/trove-unpublished
repo_name: trove-unpublished
zenodo_concept_id: 3549343
notebook: convert-fa-to-json.ipynb
tags:
  - finding aids
  - manuscripts
hide:
  - toc
---

While I think the finding aids are created and stored as [EAD](https://www.loc.gov/ead/) encoded XML files, they are delivered as HTML. This means that to reassemble the finding aid hierarchy in a way that facilitates analysis, we have to scrape the HTML and make a few assumptions about the content.

{{ description }}

[Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab%2Ftree%2F{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}