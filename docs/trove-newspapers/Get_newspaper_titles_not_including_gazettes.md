---
title: Get a list of Trove newspapers that doesn't include government gazettes
description: The Trove API includes an option to retrieve details of digitised newspaper titles. Version 2 of the API added a separate option to get details of government gazettes. However the original `newspaper/titles` requests actually returns both the newspaper and gazette titles, so there's no way of getting just the newspaper titles. This notebook explains the problem and provides a simple workaround.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
notebook: Get_newspaper_titles_not_including_gazettes.ipynb
tags:
  - newspaper titles
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