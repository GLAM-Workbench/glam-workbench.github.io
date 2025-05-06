---
title: NSW State Archives
description: A collection of notebooks for working with collection data from the NSW State Archives.
repo_name: nsw-state-archives
repo_url: https://github.com/GLAM-Workbench/nsw-state-archives
zenodo_concept_id: 3549128
---

{{ git_latest_tag() }}

A collection of notebooks for working with collection data from the [NSW State Archives](https://mhnsw.au/collections/state-archives-collection/).

NSW State Archives content in copyright was previously licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0) licence](http://creativecommons.org/licenses/by/4.0/). See their archived [copyright page](https://web.archive.org/web/20220303172132/https://www.records.nsw.gov.au/about-state-records/copyright-policy) for more information.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/HEAD?urlpath=lab/tree/index.ipynb)

## Tools, tips, and examples

### [:material-notebook-outline: Get details of online indexes](get-list-of-indexes.md) {: data-toc-omit }
This notebook scrapes details of available indexes from the [NSW State Archives A to Z list of online indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z). It saves the results as a CSV formatted file.

### [:material-notebook-outline: Harvest online indexes](harvest-indexes.md) {: data-toc-omit }
This notebook harvests data from all of [NSW State Archives online indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z), saving the data as a collection of easily downloadable CSV files.

### [:material-notebook-outline: Summarise index details](summarise-index-details.md) {: data-toc-omit }
This notebook counts the number of rows in each index and calculates the total for the whole repository. It formats the results in nice HTML and Markdown tables for easy browsing.

### [:material-notebook-outline: NSW State Archives Index Explorer](index-explorer.md) {: data-toc-omit }
NSW State Archives provides a lot of rich descriptive data in its online indexes. But there's so much data it can be hard to understand what's actually in each index. This notebook tries to help by generating an overview of an index, summarising the contents of each field.

## Data

### [:material-folder-outline: CSV list of indexes](index-list.md) {: data-toc-omit }

*Harvested May 2023*

### [:material-folder-outline: Repository of harvested indexes](index-repository.md) {: data-toc-omit }

**Currently: 75 indexes harvested with 2,481,881 rows of data.**  
*Harvested May 2023*

<!-- START RUN INFO -->

{% include "nb-run-info.md" %}

<!-- END RUN INFO -->


## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
