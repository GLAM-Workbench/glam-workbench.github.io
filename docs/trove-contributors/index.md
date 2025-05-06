---
title: Trove contributors
description: Trove aggregates metadata from thousands of organisations and projects around Australia. Data about contributors is available from the `/contributor` endpoint of the Trove API. Here you'll find some examples of harvesting and exploring data about Trove's metadata contributors.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
---

{{ git_latest_tag() }}


Trove aggregates metadata from thousands of organisations and projects around Australia. Data about contributors is available from the `/contributor` endpoint of the Trove API. Here you'll find some examples of harvesting and exploring data about Trove's metadata contributors.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Create a flat list of organisations contributing metadata to Trove](get_contributors.md) {: data-toc-omit }

This notebook converts the nested data available from the `/contributor` endpoint into a single flat list of contributors

### [:material-notebook-outline: Get the number of records from each contributor by zone and format](get_contributors_totals_zone_format.md) {: data-toc-omit }

This notebook gets the number of records contributed by each organisation, aggregated by zone and format

## Datasets

### [:material-database-outline: List of organisations contributing metadata to Trove](trove-contributors-list.md) {: data-toc-omit }

This is a flattened version of the contributors data available from the Trove API. It is harvested weekly.

### [:material-database-outline: Count of records by contributor and zone](trove-contributors-zones.md) {: data-toc-omit }

This dataset was created by searching for contributor's NUC codes in each Trove zone. This gives a count of records by contributor and zone. It is harvested weekly.

### [:material-database-outline: Count of records by contributor, zone, and format](trove-contributors-formats.md) {: data-toc-omit }

This dataset was created by searching for contributor's NUC codes in each Trove zone and requesting the format facet. This gives a count of records by contributor, zone, and format. It is harvested weekly.


<!-- START RUN INFO -->

{% include "nb-run-info.md" %}

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}