---
title: Get an random newspaper article from Trove
description: This method searches for a random stop word, letter, or digit, then filters the results by randomly applying facets until the result set is less that 100 (or as near as possible). It then randomly selects one of the results. You can supply your own queries, or specific facet values to limit the result set.
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
zenodo_concept_id: 3549403
notebook: random_newspaper_article.ipynb
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