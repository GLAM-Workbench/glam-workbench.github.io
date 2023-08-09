---
title: "NLA digitised finding aids: list of urls"
description: A list of urls pointing to the National Library of Australia's digitised manuscript finding aids, harvested from Trove.
repo_url: https://github.com/GLAM-Workbench/trove-unpublished
repo_name: trove-unpublished
zenodo_concept_id: 3549343
file_url: "https://github.com/GLAM-Workbench/nla-finding-aids-data/blob/main/finding-aids.csv"
tags:
  - public domain
  - manuscripts
  - metadata
  - dataset
hide:
  - toc
---

*Harvested 1 March 2023*

{{ description }}

The dataset is formatted as a CSV file and contains the following columns:

| Column | Contents |
|--------|----------|
`url` | URL pointing to digitised finding aid in Trove


[Download from GitHub]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Find urls of digitised finding aids](find-finding-aids.md) 

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}