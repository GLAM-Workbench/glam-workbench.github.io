---
title: Newspaper titles harvested from web archives
description: CSV formatted dataset containing details of the first appearance of newspaper titles in web archive captures, indicating when the titles were (approximately) added to Trove. The complete list of captures has been filtered to include only the first appearance of each title / place / date range combination.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
file_url: https://github.com/GLAM-Workbench/trove-newspapers/blob/master/trove_newspaper_titles_first_appearance_2009_2021.csv
tags:
  - web archives
  - dataset
  - CSV
hide:
  - toc
---
*Harvested 21 January 2022*

{{ description }}

The dataset contains the following columns:

| Column | Contents |
|--------|----------|
`title_id` | title identifier
`full_title` | full title (including location and dates)
`title` | newspaper title
`place` | place of publication
`dates` | date range in Trove
`capture_date` | date of web archive capture
`capture_timestamp` | timestamp of web archive capture

[Download from GitHub]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

### Related resources

* [Gathering historical data about the addition of newspaper titles to Trove](historical-data-newspaper-titles.md) 
* [Newspaper titles harvested from web archives](csv-newspaper-titles-from-web-archives.md)
* [Alphabetical list of newspaper titles showing approximately when they first appeared in Trove](https://gist.github.com/wragge/7d80507c3e7957e271c572b8f664031a)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}