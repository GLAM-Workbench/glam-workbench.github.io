---
title: Trove digitised maps metadata
description: This dataset contains metadata describing digitised maps in Trove, harvested from the Trove API and other sources.
repo_url: https://github.com/GLAM-Workbench/trove-maps
repo_name: trove-maps
zenodo_concept_id: 7591970
notebook: parse-coordinates.ipynb
tags:
  - maps
  - metadata
  - dataset
hide:
  - toc
---

*Harvested 31 January 2023*

{{ description }}

The dataset is formatted as a CSV file and contains the following columns:

| Column | Contents |
|--------|----------|
`title` | title of the map
`url` | url to the map in the digitised file viewer
`work_url` | url to the work in the Trove map category
`identifier` | NLA identifier
`date` | date published or created
`creators` | creators of the map
`publication` | publication place, publisher, and publication date (if available)
`extent` | physical description of map
`copyright_status` | copyright status based on available metadata (scraped from web page)
`scale` | map scale
`coordinates` | map coordinates, either a point or a bounding box (format is 'W--E/N--S', eg: 'E 130⁰50'--E 131⁰00'/S 12⁰30'--S 12⁰40')
`filesize_string` | filesize string in MB
`filesize` | size of TIFF file in bytes
`width` | width of TIFF in pixels
`height` | height of TIFF in pixels

[Download from GitHub](https://raw.githubusercontent.com/GLAM-Workbench/trove-maps-data/main/single_maps_20230131.csv){ .md-button .md-button--primary }

### Related resources

* [Exploring digitised maps in Trove](exploring-digitised-maps.md) (dataset)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}