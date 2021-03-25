---
title: Random items from Trove
repo_url: https://github.com/GLAM-Workbench/trove-random
repo_name: trove-random
---

Changes to the Trove API mean that the techniques I've previously used to select resources at random [will no longer work](https://updates.timsherratt.org/2019/10/09/creators-and-users.html). This repository includes some alternative ways of retrieving *random-ish* works and newspaper articles from Trove. While I've tried to mix things up and get as deep into the results set as possible, it's likely that some items are still inaccessible. So while the results will appear random, they may in fact be filtered due to the way facets are applied and delivered through the API. I hope that in the future Trove will provide a random sort option to avoid these problems.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master?urlpath=lab)

## Tips, tools, and examples

### Get an random newspaper article from Trove

This method searches for a random stop word, letter, or digit, then filters the results by randomly applying facets until the result set is less that 100 (or as near as possible). It then randomly selects one of the results. You can supply your own queries, or specific facet values to limit the result set.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-random/blob/master/random_newspaper_article.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-random/blob/master/random_newspaper_article.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master?urlpath=lab/tree/random_newspaper_article.ipynb)

### Get a random work from Trove by generating random `id`s

Here's a way you can get a random work from Trove's book, article, picture, map, music, or collection zones. It generates random work id prefixes and performs a wildcard search using the id index. If the prefix returns no results, a digit is sliced off the end. If a prefix returns more than 100 results, a digit is added to the end. This continues until the result set hits the sweet spot between 0 and 100. You can apply values for top-level facets like `Format`, but going too deep into the facet hierarchy will mean the `id` search will generate more misses. If you want to apply your own queries or facets, try the method below.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-random/blob/master/random_work_by_id.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-random/blob/master/random_work_by_id.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master?urlpath=lab/tree/random_work_by_id.ipynb)

### Get a random work from Trove using queries and facets

Here's another way you can get a random work from Trove's book, article, picture, map, music, or collection zones. This approach is particularly useful if you want to get a random result from a search, or want to apply a variety of facets. It's not as quick as pinging random work ids at Trove, but it's more flexible. Basically this method gets all the available facets for a particular search. If the search has more than 100 results, it chooses one of the facets at random and applies it. It keeps doing this until the search returns less that 100 results. Then it chooses a work at random from the results. If you don't supply a query, it uses a random stop word to mix things up a bit.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-random/blob/master/random_work_by_facets.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-random/blob/master/random_work_by_facets.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-random/master?urlpath=lab/tree/random_work_by_facets.ipynb)

## Cite as

Sherratt, Tim. (2019, November 21). GLAM-Workbench/trove-random (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3549404>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3549404.svg)](https://doi.org/10.5281/zenodo.3549404)
