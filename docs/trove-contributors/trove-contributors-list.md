---
title: List of organisations contributing metadata to Trove
description: This is a flattened version of the contributors data available from the Trove API.
repo_url: https://github.com/GLAM-Workbench/trove-contributors
repo_name: trove-contributors
zenodo_concept_id: 7736765
file_url: "https://github.com/wragge/trove-contributor-totals/blob/main/data/trove-contributors.csv"
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
| `id` | Trove identifier for organisation/project
| `nuc` | NUC (National Union Catalogue) identifier for this organisation/project
| `name` | name of the organisation/project
| `parent` | identifier of parent organisation
| `total` | number of records contributed by this organisation/project


[Download from Github]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Create a flat list of organisations contributing metadata to Trove](get_contributors.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}