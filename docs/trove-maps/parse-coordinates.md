---
title: Parse map coordinates from metadata
description: The harvest of digitised maps metadata includes a coordinates column that provides a string representation of either a point or a bounding box. This notebook attempts to parse the coordinate string and convert the values to decimals. It then uses the decimal values to explore the geographical context of Trove's digitised map collection.
repo_url: https://github.com/GLAM-Workbench/trove-maps
repo_name: trove-maps
zenodo_concept_id: 3549426
notebook: parse-coordinates.ipynb
tags:
  - maps
  - metadata
  - coordinates
hide:
  - toc
---

{{ description }}

![](../images/trove-map-overlay.png)

[Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab%2Ftree%2F{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/{{repo_name}}/blob/master/{{notebook}})

### Related resources

* [Coordinates of digitised maps from Trove](single-maps-coordinates-data.md) (dataset)
* [Locations of Trove digitised maps](https://glam-workbench.net/trove-maps/trove-map-clusters.html) – browse Trove's digitised maps by location, using a standalone HTML version of the Folium cluster map created by this notebook

[![](../images/trove-maps-folium-cluster.png)](https://glam-workbench.net/trove-maps/trove-map-clusters.html)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}