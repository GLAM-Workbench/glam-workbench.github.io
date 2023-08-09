---
title: Count of records by contributor and zone
description: This dataset was created by searching for contributor's NUC codes in each Trove zone. This gives a count of records by contributor and zone.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
file_url: "https://github.com/wragge/trove-contributor-totals/blob/main/data/trove-contributors-zones.csv"
tags:
  - metadata
  - dataset
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
| `total` | number of records contributed by this organisation/project


[Download from Github]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Get the number of records from each contributor by zone and format](get_contributors_totals_zone_format.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}