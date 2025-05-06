---
title: Trove maps
repo_url: https://github.com/GLAM-Workbench/trove-maps
repo_name: trove-maps
zenodo_concept_id: 3549426
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/trove-maps/master/ro-crate-metadata.json
page_type: repo
---

{{ git_latest_tag() }}

The Trove 'map' zone includes single maps, as well as map series, atlases, and aerial photographs. You can access metadata from the map zone through the Trove API.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)


## Notebooks

{% for nb in page.meta.notebooks|sort(attribute="position") %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description.split("\n\n")[0] }}

{% endfor %}



## Data

### [:material-folder-text-outline: Trove digitised maps metadata](single-maps-data.md) {: data-toc-omit }

*Harvested: 6 June 2024*

This dataset contains metadata describing digitised maps in Trove, harvested from the Trove API and other sources.

### [:material-folder-text-outline: Trove digitised maps – coordinates](single-maps-coordinates-data.md) {: data-toc-omit }

*Harvested: 6 June 2024*

This dataset was generated from the harvest of digitised maps metadata. Coordinate strings in the metadata (points and bounding boxes) were parsed and converted to decimal values.

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
