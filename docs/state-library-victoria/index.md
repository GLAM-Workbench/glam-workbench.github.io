---
title: State Library of Victoria
description: Tools and resources for working with data from the State Library of Victoria.
repo_url: https://github.com/GLAM-Workbench/state-library-victoria
repo_name: state-library-victoria
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/state-library-victoria/refs/heads/master/ro-crate-metadata.json
page_type: repo
jlite_repo: state-library-victoria-jlite
zenodo_concept_id: 15321602
---

{{ git_latest_tag() }}

{{ page.meta.description}}

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Jupyter Lite or Binder.

[![Jupyter Lite](../images/jlite-badge.svg)](http://glam-workbench.net/{{ page.meta.jlite_repo }}/) [![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Notebooks
{% for nb in page.meta.notebooks %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description }}

{% endfor %}

{% if page.meta.datasets %}

## Datasets

{% for ds in page.meta.datasets %}

### [:material-database-outline: {{ ds.name }}]({{ ds.url.strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ ds.description }}

{% endfor %}

{% endif %}

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}


{% endif %}
