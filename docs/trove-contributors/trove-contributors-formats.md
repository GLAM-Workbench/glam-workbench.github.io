---
title: Count of records by contributor, zone, and format
description: This dataset was created by searching for contributor's NUC codes in each Trove zone and requesting the format facet. This gives a count of records by contributor, zone, and format. It is harvested weekly.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
file_url: https://github.com/wragge/trove-contributor-totals/blob/main/data/trove-contributors-formats.csv
tags:
  - metadata
hide:
  - toc
---

*Harvested weekly*

{{ description }}

 The dataset is saved as a CSV file containing the following columns:

| Column | Contents |
|--------|----------|
| `nuc` | NUC (National Union Catalogue) identifier for this organisation/project
| `name` | name of the organisation/project
| `zone` | name of the Trove zone
| `format` | format type (see Trove's [list of formats](https://trove.nla.gov.au/about/create-something/using-api/api-technical-guide#formats))
| `total` | number of records contributed by this organisation/project


[Download from Github]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Create a flat list of organisations contributing metadata to Trove](get_contributors.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}