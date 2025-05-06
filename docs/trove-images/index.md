---
title: Trove images
description: This section includes information on finding, understanding, and using images in Trove.
repo_url: https://github.com/GLAM-Workbench/trove-images
repo_name: trove-images
zenodo_concept_id: 6339873
page_type: repo
rocrate: "https://github.com/GLAM-Workbench/trove-images/raw/master/ro-crate-metadata.json"
---

{{ git_latest_tag() }}

{{ page.meta.description}}

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Notebooks

{% for nb in page.meta.notebooks %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description.split("\n\n")[0] }}

{% endfor %}


## Datasets

{% for ds in page.meta.datasets|sort(attribute="position") %}

### [:material-database-outline: {{ ds.name }}]({{ ds.url.strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ ds.description }}

{% endfor %}

{% include "nb-run-info.md" %}

{% if page.meta.zenodo_concept_id %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

{% endif %}
