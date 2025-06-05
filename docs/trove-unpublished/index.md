---
title: Trove unpublished works (diaries, letters, and archives)
repo_url: https://github.com/GLAM-Workbench/trove-unpublished
repo_name: trove-unpublished
zenodo_concept_id: 3549343
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

Experiments and examples relating to Trove's 'Diaries, letters, and archives' zone.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Finding unpublished works that might be entering the public domain on 1 January 2019](Finding-unpublished-works-entering-public-domain.md) {: data-toc-omit }

Changes to Australian copyright legislation mean that many unpublished resources will be entering the public domain on 1 January 2019. This notebook attempts to harvest the details of some of these resources from Trove.

### [:material-notebook-outline: Exploring unpublished works that might be entering the public domain on 1 January 2019](Exploring-unpublished-works-entering-public-domain.md) {: data-toc-omit }

This notebook demonstrates some ways of exploring the data harvested about unpublished resources that might be entering the public domain on 1 January 2019.

### [:material-notebook-outline: Find urls of digitised finding aids](find-finding-aids.md) {: data-toc-omit }

This notebook uses the Trove API to harvest urls of NLA digitised finding aids from a search in the `collection` zone.

### [:material-notebook-outline: Collect information about digitised finding aids](get-info-finding-aids.md) {: data-toc-omit }

This notebook works through a list of urls pointing to NLA's digitised finding aids, extracting additional information about each one.

### [:material-notebook-outline: Convert a HTML finding aid to JSON](convert-fa-to-json.md) {: data-toc-omit }

This notebook scrapes data from the HTML of a finding aid, saving the hierarchy of series, sub-series, and items as a list of nested objects. The results can be saved as a JSON file.

## Datasets

### [:material-folder-outline: Unpublished works that might be entering the public domain on 1 January 2019](unpublished-entering-pd.md) {: data-toc-omit }

This dataset contains metadata describing unpublished works that might be entering the public domain on 1 January 2019.

### [:material-folder-outline: NLA digitised finding aids: list of urls](finding-aids-urls.md) {: data-toc-omit }

A list of urls pointing to the National Library of Australia's digitised manuscript finding aids, harvested from Trove.

### [:material-folder-outline: NLA digitised finding aids: summary information](finding-aids-summary.md) {: data-toc-omit }

This dataset includes summary information describing each finding aid. 

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
