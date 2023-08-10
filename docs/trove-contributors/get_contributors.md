---
title: Create a flat list of organisations contributing metadata to Trove
description: The Trove API includes the `contributor` endpoint for retrieving information about organisations whose metadata is aggregated into Trove. However, the data can be difficult to use because of its nested structure, with some organisations having several levels of subsidiaries. There's also some inconsistency in the way nested records are named. This notebook aims to work around these problems by converting the nested data into a single flat list of organisations.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
notebook: get_contributors.ipynb
tags:
  - harvest
  - metadata
hide:
  - toc
---

{{ description }}

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Related resources

* [List of organisations contributing metadata to Trove](trove-contributors-list.md)  (dataset)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}