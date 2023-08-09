---
title: CSV list of indexes
description: This is a a CSV-formatted list of online indexes available from the NSW State Archives A to Z subject list.
repo_url: https://github.com/GLAM-Workbench/nsw-state-archives
repo_name: nsw-state-archives
zenodo_concept_id: 3549128
file_url: "https://media.githubusercontent.com/media/wragge/srnsw-indexes/master/indexes.csv"
tags:
  - CSV dataset
hide:
  - toc
---

*Harvested May 2023*

{{ description }}

[Download from Github]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

Columns include:

| Column | Description |
|--------|-------------|
`title` | the full title of the index
`url` | the address of the index on the NSW State Archives website
`description` | a brief description of the index
`category` | the category to which this index belongs (eg: "Convicts")

### Related resources

* [Get details of online indexes](get-list-of-indexes.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}