---
title: Trove public tags
description: CSV formatted file containing a complete harvest of public tags added to Trove resources.
repo_url: https://github.com/GLAM-Workbench/trove-lists
repo_name: trove-lists
zenodo_concept_id: 5094313
tags:
  - dataset
  - metadata
  - CSV
hide:
  - toc
---

*Harvested: 6 June 2024*

This dataset contains details of 2,495,958 unique public tags added to 10,403,650 resources in Trove between August 2008 and June 2024. It is saved as a CSV file with the following columns:

| Column | Contents |
|--------|----------|
`tag` | lower-cased text tag
`date` | date the tag was added
`zone` | API zone containing the tagged resource
`record_id` | the identifier of the tagged resource

Using the `zone` and `record_id` you can find more information about a tagged item. To create urls to the resources in Trove:

- for resources in the 'book', 'article', 'picture', 'music', 'map', and 'collection' zones add the `record_id` to `https://trove.nla.gov.au/work/`
- for resources in the 'newspaper' and 'gazette' zones add the `record_id` to `https://trove.nla.gov.au/article/`
- for resources in the 'list' zone add the `record_id` to `https://trove.nla.gov.au/list/`

Notes:

- Works (such as books) in Trove can have tags attached at either work or version level. This dataset aggregates all tags at the work level, removing any duplicates.
- A single resource in Trove can appear in multiple zones – for example, a book that includes maps and illustrations might appear in the 'book', 'picture', and 'map' zones. This means that some of the tags will essentially be duplicates – harvested from different zones, but relating to the same resource. Depending on your needs, you might want to remove these duplicates.
- While most of the tags were added by Trove users, more than 500,000 tags were added by Trove itself in November 2009. I think these tags were automatically generated from related Wikipedia pages. Depending on your needs, you might want to exclude these by limiting the date range or zones.
- User content added to Trove, including tags, is available for reuse under a CC-BY-NC licence.

[Download from Zenodo](https://zenodo.org/doi/10.5281/zenodo.5094313){ .md-button .md-button--primary }

### Related resources

* [Harvest public tags from Trove zones ](harvest-tags.md)
* [Analyse public tags added to Trove](analyse_tags.md)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}