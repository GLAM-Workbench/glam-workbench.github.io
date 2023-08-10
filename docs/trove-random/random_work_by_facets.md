---
title: Get a random work from Trove using queries and facets
description: Here's another way you can get a random work from Trove's book, article, picture, map, music, or collection zones. This approach is particularly useful if you want to get a random result from a search, or want to apply a variety of facets. It's not as quick as pinging random work ids at Trove, but it's more flexible. Basically this method gets all the available facets for a particular search. If the search has more than 100 results, it chooses one of the facets at random and applies it. It keeps doing this until the search returns less that 100 results. Then it chooses a work at random from the results. If you don't supply a query, it uses a random stop word to mix things up a bit.
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
zenodo_concept_id: 3549403
notebook: random_work_by_facets.ipynb
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