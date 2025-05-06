---
title: Public Record Office Victoria
description: Tools and resources for working with the Public Record Office Victoria's collection API.
repo_url: https://github.com/GLAM-Workbench/prov
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/prov/refs/heads/master/ro-crate-metadata.json
repo_name: prov
jlite_repo: prov-jlite
page_type: repo
zenodo_concept_id: 15289178
---


{{ git_latest_tag() }}

{{ page.meta.description}}

The Public Record Office Victoria's Public API provides data about its archival holdings in a machine readable format. This makes it possible to use, analyse, and visualise the collection in new ways. You can read more about the API in [this blog post](https://prov.vic.gov.au/about-us/our-blog/new-prov-public-api).

For an overview of the data currently available though the PROV API, see the [PROV Data Dashboard](https://wragge.github.io/prov-dashboard/).

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

## Related projects

- [PROV Data Dashboard](https://wragge.github.io/prov-dashboard/) – updated every Sunday
- [PROVBot](https://updates.timsherratt.org/2025/04/09/introducing-provbot-sharing-photos-from.html) – a Fediverse bot sharing photos from the PROV collection
- Data downloaded from the PROV API has also been [added to the GLAM Name Index Search](https://updates.timsherratt.org/2025/04/09/more-than-million-rows-of.html)

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}


{% endif %}
