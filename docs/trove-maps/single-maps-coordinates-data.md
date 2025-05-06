---
title: Trove digitised maps – coordinates
description: This dataset was generated from the harvest of digitised maps metadata. Coordinate strings in the metadata (points and bounding boxes) were parsed and converted to decimal values.
repo_url: https://github.com/GLAM-Workbench/trove-maps-data
repo_name: trove-maps-data
tags:
  - maps
  - metadata
  - dataset
hide:
  - toc
---

*Harvested 6 June 2024*

{{ description }}

The dataset is formatted as a CSV file and contains the following columns:

| Column | Contents |
|--------|----------|
`title` | title of the map
`url` | url to the map in the digitised file viewer
`coordinates` | map coordinates as a string, either a point or a bounding box (format is 'W--E/N--S', eg: 'E 130⁰50'--E 131⁰00'/S 12⁰30'--S 12⁰40')
`latitude` | point from coordinates or centre of box
`longitude` | point from coordinates or centre of box
`north` | north bounds of box
`south` | south bounds of box
`east` | east bounds of box
`west` | west bounds of box

[Download from GitHub](https://raw.githubusercontent.com/GLAM-Workbench/trove-maps-data/main/single_maps_coordinates.csv){ .md-button .md-button--primary }

### Related resources

* [Parse map coordinates from metadata](parse-coordinates.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}