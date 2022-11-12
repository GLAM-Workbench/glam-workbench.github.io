---
title: Visualise the connections of a single Australian government agency
description: This notebook provides a simple app for exploring connections between departments. Select a department from the dropdown list to view its predecessors and successors as a network graph.
repo_url: https://github.com/GLAM-Workbench/wikidata
repo_name: wikidata
tags:
  - visualisation
  - National Archives of Australia
  - Wikidata
hide:
  - toc
zenodo_concept_id: 7264897
---

This notebook provides a simple app for exploring connections between departments. Select a department from the dropdown list to view its predecessors and successors as a network graph. Each agency is represented as a node whose position and colour is determined by the decade in which the agency was created. The size of the node indicates how long the agency was in existence, while edges between nodes connect agencies to their successors.

[Run live in Voila on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/wikidata/master?urlpath=/voila/render/single-agency-network.ipynb){ .md-button .md-button--primary }

### Other options

* [Run live as a notebook on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/wikidata/master?urlpath=lab/tree/single-agency-network.ipynb)
* [Download from GitHub](https://github.com/GLAM-Workbench/wikidata/blob/master/single-agency-network.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/wikidata/blob/master/single-agency-network.ipynb)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}

