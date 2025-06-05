---
title: Random items from Trove
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
zenodo_concept_id: 3549403
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

Changes to the Trove API mean that the techniques I've previously used to select resources at random [will no longer work](https://updates.timsherratt.org/2019/10/09/creators-and-users.html). This repository includes some alternative ways of retrieving *random-ish* works and newspaper articles from Trove. While I've tried to mix things up and get as deep into the results set as possible, it's likely that some items are still inaccessible. So while the results will appear random, they may in fact be filtered due to the way facets are applied and delivered through the API. I hope that in the future Trove will provide a random sort option to avoid these problems.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Get an random newspaper article from Trove](random_newspaper_article.md) {: data-toc-omit }

This method searches for a random stop word, letter, or digit, then filters the results by randomly applying facets until the result set is less that 100 (or as near as possible).

### [:material-notebook-outline: Get a random work from Trove by generating random `id`s](random_work_by_id.md) {: data-toc-omit }

Here's a way you can get a random work from Trove's book, article, picture, map, music, or collection zones. It generates random work id prefixes and performs a wildcard search using the id index.

### [:material-notebook-outline: Get a random work from Trove using queries and facets](random_work_by_facets.md) {: data-toc-omit }

Here's another way you can get a random work from Trove's book, article, picture, map, music, or collection zones. Basically this method gets all the available facets for a particular search. If the search has more than 100 results, it chooses one of the facets at random and applies it.

<!-- START RUN INFO -->

{% include "nb-run-info.md" %}


<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
