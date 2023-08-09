---
title: Harvesting the complete set of data from the People and Organisations zone
description: There are two methods of harvesting the complete set of data from the People and Organisations zone – using the OAI-PMH API, or using the main Trove API in conjunction with the SRU interface. The OAI-PMH method is much faster, but includes duplicate records that you'll need to filter out afterwards. This notebook demonstrates the API/SRU method.
repo_url: https://github.com/GLAM-Workbench/trove-people
repo_name: trove-people
zenodo_concept_id: 7645058
notebook: complete_harvest.ipynb
tags:
  - data harvesting
  - API
  - SRU
  - EAC-CPF
hide:
  - toc
---

{{ description }}

[Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab%2Ftree%2F{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Related resources

* [Complete harvest of People and Organisations data](complete_harvest_dataset.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}

