---
title: Display the results of a harvest as a searchable database using Datasette
description: This notebook shows you how to load the newspaper data you've harvested into Datasette, and start it up.
repo_name: trove-newspaper-harvester
notebook: display_harvest_results_using_datasette.ipynb
repo_url: https://github.com/glam-workbench/trove-newspaper-harvester
zenodo_concept_id: 3545044
tags:
  - Datasette
hide:
  - toc
---

![Screen capture of Datasette](../images/datasette-row.png)

[Datasette](https://github.com/simonw/datasette) is 'a tool for exploring and publishing data'. Give it a CSV file and it turns it into a fully-searchable database, running in your browser. It supports facets, full-text search, and, with a bit of tweaking, can even present images. Although Datasette is a command-line tool, we can run from within a Jupyter notebook, and open a new window to display the results. This notebook shows you how to load the newspaper data you've harvested into Datasette, and start it up. If you've also harvested full-text and images from the newspaper articles, you can add these to your database as well!

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/display_harvest_results_using_datasette.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/display_harvest_results_using_datasette.ipynb)

### Additional documentation

* [Understanding your harvested data](../#your-harvested-data)
* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}

