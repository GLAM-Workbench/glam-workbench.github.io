---
title: Complete list of issues for every newspaper in Trove
description: CSV formatted dataset containing a complete list of newspaper issues available on Trove.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 12547036
tags:
  - metadata
  - dataset
  - CSV
hide:
  - toc
---
*Harvested 26 June 2024*

{{ description }}

The dataset contains the following columns:

| Column | Contents |
|--------|----------|
`title` | newspaper title
`title_id` | newspaper id
`state` | place of publication
`issue_id` | issue identifier
`issue_date` | date of publication (YYYY-MM-DD)

[Download from Zenodo](https://doi.org/10.5281/zenodo.12547036){ .md-button .md-button--primary }

To keep the file size down, I haven't included an `issue_url` in this dataset, but these are easily generated from the `issue_id`. Just add the `issue_id` to the end of `http://nla.gov.au/nla.news-issue`. For example: http://nla.gov.au/nla.news-issue495426. Note that when you follow an issue url, you actually get redirected to the url of the first page in the issue.

### Related resources

* [Harvest information about newspaper issues](harvest_newspaper_issues.md)
* [Visualisation of the number of newspaper issues per day, 1803 to 2021](/examples/trove_newspaper_issues_per_day.html)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}