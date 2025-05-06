---
title: NLA oral histories metadata
description: This dataset contains metadata describing oral histories held by the National Library of Australia. The metadata was harvested from Trove and includes details of both digitised, and not digitised, oral histories.
repo_url: https://github.com/GLAM-Workbench/trove-oral-histories-data
repo_name: trove-oral-histories-data
zenodo_concept_id: 
tags:
  - dataset
  - metadata
hide:
  - toc
file_url: https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-histories.csv
---

*Harvested: December 2023*

{{ description }}

[Download from GitHub]({{file_url}}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{file_url}}&fts=title,contributor,is_part_of&drop=publisher,work_type,fulltext_url_text){ .md-button .md-button--info }

#### Data fields

| Column | Contents |
|--------|----------|
`title`| title of the oral history
`contributor`| includes both interviewers and interviewees
`publisher`| mostly empty but can include some publication details
`date`| date the oral history was recorded
`type`| for example `performed music`, `spoken word`
`format`| for example `Sound recording`, `online resource`
`extent`| usually number of files/reels/tapes, sometimes includes duration
`language`| language of the recording
`subject`| subjects of interview
`spatial`| associated places (mostly using [Library of Congress geographic area codes](https://www.loc.gov/marc/geoareas/gacs_code.html))
`is_part_of`| collections or projects that this interview belongs to
`identifier`| library identifiers
`rights`| copyright and licensing information
`work_url`| link to work record in Trove
`work_type`| Trove work format, for example `Sound/Interview, lecture, talk`
`fulltext_url`| link to audio player (if digitised)
`fulltext_url_text`| text of link to audio player
`catalogue_url`| link to NLA catalogue entry
`summary`| text summary is available for download – `0` for no, `1` for yes
`transcript`| text transcript is available for download – `0` for no, `1` for yes
`sessions`| number of recording sessions
`duration`| total duration of recordings (in seconds)

### Related resources

* [Harvest oral histories metadata](harvest-oral-histories.md)
* The [Overview of oral histories](https://tdg.glam-workbench.net/other-digitised-resources/oral-histories/overview.html) in the *Trove Data Guide* uses this dataset to explore the contents of the NLA's oral history collection.


### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}
