---
title: Trove government
description: Resources generated or collected by the Australian Commonwealth Government are available in a number of different locations and formats across Trove. This repository contains tools and examples to work with digitised government publications available through Trove.
repo_url: https://github.com/GLAM-Workbench/trove-government
repo_name: trove-government
page_type: repo
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/trove-government/master/ro-crate-metadata.json
zenodo_concept_id: 15354169
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

{{ page.meta.description}}

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)


## Notebooks
{% for nb in page.meta.notebooks %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description }}

{% endfor %}

## Datasets

{% for ds in page.meta.datasets %}

### [:material-database-outline: {{ ds.name }}]({{ ds.url.strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ ds.description }}

{% endfor %}

{% include "nb-run-info.md" %}


## Contributors

{{ repo_contributors() }}

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}


{% endif %}





