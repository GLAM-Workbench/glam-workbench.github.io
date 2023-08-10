---
title: Get a random work from Trove by generating random ids
description: Here's a way you can get a random work from Trove's book, article, picture, map, music, or collection zones. It generates random work id prefixes and performs a wildcard search using the id index. If the prefix returns no results, a digit is sliced off the end. If a prefix returns more than 100 results, a digit is added to the end. This continues until the result set hits the sweet spot between 0 and 100. You can apply values for top-level facets like `Format`, but going too deep into the facet hierarchy will mean the `id` search will generate more misses. If you want to apply your own queries or facets, try the method below.
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
zenodo_concept_id: 3549403
notebook: random_work_by_id.ipynb
tags:
  - random
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