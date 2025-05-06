---
title: Harvest of ABC Radio National metadata
description: The full harvest of ABC Radio National program metadata, containing more than 400,000 records.
repo_url: https://github.com/GLAM-Workbench/trove-abcrn-data
repo_name: trove-abcrn-data
zenodo_concept_id: 7659567
tags:
  - dataset
  - metadata
hide:
  - toc
---

*Harvested: December 2023*

The full harvest of ABC Radio National program metadata, containing more than 400,000 records. is available for download from GitHub in the following formats:

* [350mb NDJSON file](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-metadata.ndjson) – each record is saved as a JSON object, separated by line breaks
* [226mb CSV file](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-metadata.csv)

You can also download CSVs for individual programs:

* [RN Breakfast](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-breakfast-metadata.csv)
* [RN Drive](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-drive-metadata.csv)
* [AM](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-am-metadata.csv)
* [PM](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-pm-metadata.csv)
* [The World Today](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-worldtoday-metadata.csv)
* [Late Night Live](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-latenight-metadata.csv)
* [Life Matters](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-lifematters-metadata.csv)
* [The Science Show](https://github.com/GLAM-Workbench/trove-abcrn-data/blob/main/abcrn-scienceshow-metadata.csv)

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
`type` | list of types (not sure how this differa from `format`)
`format` | list of formats (not sure how this differs from `type`)
`abstract` | text providing a summary of the program or segment (may incude multiple values)
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
