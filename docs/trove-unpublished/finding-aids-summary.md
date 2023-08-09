---
title: "NLA digitised finding aids: summary information"
description: This dataset includes summary information describing each finding aid. 
repo_url: https://github.com/GLAM-Workbench/trove-unpublished
repo_name: trove-unpublished
zenodo_concept_id: 3549343
file_url: "https://github.com/GLAM-Workbench/nla-finding-aids-data/blob/main/finding-aids-totals.csv"
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
`url` | 
`collection_number` | 
`title` | 
`creator` | 
`date_range` | 
`extent` | 
`language_of_materials` |   
`repository` | 
`sponsor` | 
`abstract` | 
`physical_description` |   
`total_elements` | number of headings or sections within the finding aid, this includes both containers (like series and boxes) and individual items (like letters and diaries)
`total_items` | number of elements at the bottom of the hierarchy (so they have no children), they include things like documents and diaries
`total_digitised_items` | number of items that have been digitised
`total_searchable` | number of elements that can be found by a search in Trove's 'Diaries, Letters, and Archives' category

[Download from GitHub]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Collect information about digitised finding aids](get-info-finding-aids.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}