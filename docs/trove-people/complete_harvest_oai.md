---
title: Harvesting the complete set of data from the People and Organisations zone using OAI-PMH
description: There are two methods of harvesting the complete set of data from the People and Organisations zone – using the OAI-PMH API, or using the main Trove API in conjunction with the SRU interface. The OAI-PMH method is much faster, but includes duplicate records that you'll need to filter out afterwards. This notebook demonstrates the OAI-PMH method.
repo_url: https://github.com/GLAM-Workbench/trove-people
repo_name: trove-people
zenodo_concept_id: 7645058
notebook: complete_harvest_oai.ipynb
tags:
  - data harvesting
  - OAI-PMH
  - EAC-CPF
hide:
  - toc
---

{{ description }}

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}