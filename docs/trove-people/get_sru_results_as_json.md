---
title: Harvest SRU API results as JSON
description: You can query the People & Organisations data using the SRU (Search/Retrieve via URL) API, and retrieve data in a number of XML formats, the richest and most complex of which is EAC-CPF. However, the XML records are not easy to work with, so to simplify further processing, this notebook queries the SRU interface and then converts the EAC-CPF XML results into JSON.
repo_url: https://github.com/GLAM-Workbench/trove-people
repo_name: trove-people
zenodo_concept_id: 7645058
notebook: get_sru_results_as_json.ipynb
tags:
  - SRU
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