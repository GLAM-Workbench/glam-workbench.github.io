---
title: Trove lists and tags
description: Trove lists and tags are created by Trove users to organise and describe resources. The details of public lists and tags are available through the Trove API. The notebooks in this repository demonstrate how to harvest and analyse list and tag data.
repo_url: https://github.com/GLAM-Workbench/trove-lists
repo_name: trove-lists
zenodo_concept_id: 3549453
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/trove-lists/master/ro-crate-metadata.json
page_type: repo
categories:
    - Lists
    - Tags
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

{{ page.meta.description}}

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Notebooks

{% for category in page.meta.categories %}

### {{category}}

{% for nb in page.meta.notebooks|selectattr("category", "equalto", category)|sort(attribute="position") %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description.split("\n\n")[0] }}

{% endfor %}

{% endfor %}


## Datasets

### [:material-folder-text-outline: Trove lists metadata](trove-lists-metadata.md) {: data-toc-omit }

*Harvested: 29 May 2024*. CSV formatted file containing a complete harvest of metadata describing user-created Trove lists.

### [:material-folder-text-outline: Trove public tags](trove-public-tags.md) {: data-toc-omit }

*Harvested: 6 June 2024*. CSV formatted file containing a complete harvest of public tags added to Trove resources.

### [:material-folder-text-outline: Trove tag counts](trove-tag-counts.md) {: data-toc-omit }

*Harvested: 6 June 2024*. CSV formatted file containing the total number of times each tag in Trove has been applied to resources.

{% include "nb-run-info.md" %}

{% if page.meta.zenodo_concept_id %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

{% endif %}
