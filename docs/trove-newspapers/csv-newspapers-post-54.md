---
title: List of Trove newspapers with non-English language content
description: CSV formatted dataset containing a list of digitised newspapers in Trove with articles published after 1954 (the copyright cliff of death).
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
file_url: https://github.com/GLAM-Workbench/trove-newspapers-data-post-54/blob/v1.5/newspapers_post_54.csv
tags:
  - CSV
  - dataset
  - copyright
hide:
  - toc
---
*Updated: 21 January 2022*

{{ description }}

The dataset contains the following columns:

| Column | Contents |
|--------|----------|
`title` | the full title of the newspaper
`state` | the state in which the newspaper was published
`id` | Trove's unique identifier for this newspaper
`startDate` | the earliest date of articles from this newspaper available in Trove
`endDate` | the latest date of articles from this newspaper available in Trove
`issn` | ISSN
`number_of_articles` | the number of articles from this newspaper published after 1954 available in Trove
`troveUrl` | link to more information about this newspaper


[Download from Zenodo](https://doi.org/10.5281/zenodo.6812811){ .md-button .md-button--primary }  [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Beyond the copyright cliff of death](Beyond_the_copyright_cliff_of_death.md) 

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}