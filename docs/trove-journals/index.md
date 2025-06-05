---
title: Trove periodicals
description: There are hundreds of digitised periodicals in Trove (not including newspapers). Information about them is spread across a number of categories, and it's not always easy to find what's available. The notebooks in this repository help you harvest metadata, text, and images from digitised periodicals in Trove. There are also a number of pre-harvested datasets.
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
zenodo_concept_id: 3545215
page_type: repo
rocrate: "https://github.com/GLAM-Workbench/trove-journals/raw/master/ro-crate-metadata.json"
categories:
    - Harvesting metadata
    - Harvesting text
    - Harvesting images
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

{{ page.meta.description}}

If you just want to explore the range of digitised periodicals available, a good place to start is this [database of titles and issues](https://glam-workbench.net/datasette-lite/?url=https://github.com/GLAM-Workbench/trove-periodicals-data/blob/main/periodicals.db&install=datasette-json-html&install=datasette-template-sql&metadata=https://github.com/GLAM-Workbench/trove-periodicals-data/blob/main/metadata.json).

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

{% for ds in page.meta.datasets|sort(attribute="position") %}

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
