---
title: Harvest of ABC Radio National metadata
description: The full harvest of ABC Radio National program metadata, containing more than 400,000 records.
repo_url: https://github.com/GLAM-Workbench/trove-music
repo_name: trove-music
zenodo_concept_id: 7659567
tags:
  - dataset
  - metadata
hide:
  - toc
---

*Harvested: 21 February 2023*

The full harvest of ABC Radio National program metadata, containing more than 400,000 records. is available for download from CloudStor in the following formats:

* [576mb NDJSON file](https://cloudstor.aarnet.edu.au/plus/s/z4nPOvifevfnjDI/download) – each record is saved as a JSON object, separated by line breaks
* [334mb CSV file](https://cloudstor.aarnet.edu.au/plus/s/ry50ZpoSjOFbb8b/download)

You can also download CSVs for individual programs:

* [RN Breakfast](https://cloudstor.aarnet.edu.au/plus/s/IdElCP4ayKaGSE3/download)
* [RN Drive](https://cloudstor.aarnet.edu.au/plus/s/FMxUxCQMF5tiVZ9/download)
* [AM](https://cloudstor.aarnet.edu.au/plus/s/14zqZJUdQxW4tUU/download)
* [PM](https://cloudstor.aarnet.edu.au/plus/s/ou19G6YnCy08vxM/download)
* [The World Today](https://cloudstor.aarnet.edu.au/plus/s/IMB7vmpbosCpjJJ/download)
* [Late Night Live](https://cloudstor.aarnet.edu.au/plus/s/N0wyVk6U9GebUrA/download)
* [Life Matters](https://cloudstor.aarnet.edu.au/plus/s/rasQDezpeRM0J9W/download)
* [The Science Show](https://cloudstor.aarnet.edu.au/plus/s/eGl1jGIa5A1fgP1/download)

#### Data fields

Any of the fields other than `work_id` and `version_id` might be empty, though in most cases there should at least be values for `title`, `date`, `creator`, `contributor` and `isPartOf`.

| Column | Contents |
|--------|----------|
`work_id` | identifier for the containing work in Trove (you can use this to create a url to the item)
`version_id` | an identifier for the version within the work
`title` | title for the program or segment
`isPartOf` | name of the program this is a part of
`date` | ISO formatted date
`creator` | usually just the ABC
`contributor` | a list of names of those involved, such as the host, reporter or guest
`publisher` | usually just the ABC
`rights` | copyright information
`type` | list of types (not sure how this differa from `format`)
`format` | list of formats (not sure how this differs from `type`)
`abstract` | text providing a summary of the program or segment (may incude multiple values)
`subject` | list of subject tags (uncontrolled and very messy)
`description` | truncated text fragment from the start of the transcript (may include multiple values)
`fulltext_url` | link to the page on the ABC website where you can find more information
`thumbnail_url` | link to a related thumbnail image on the ABC website
`notonline_url` | not sure...

### Related resources

* [Harvest ABC Radio National records from Trove](harvest-abcrn.md)


### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}
