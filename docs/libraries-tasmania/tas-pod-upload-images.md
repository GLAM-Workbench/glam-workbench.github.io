---
title: Upload Tasmanian Post Office Directory images to Amazon s3 for IIIF
description: This notebook converts the images extracted from the Post Office Directory PDFs into pyramidal TIFFs using pyvips and then uploads them to an Amazon s3 bucket for delivery via IIIF.
repo_url: https://github.com/GLAM-Workbench/libraries-tasmania
repo_name: libraries-tasmania
notebook: tas-pod-upload-images.ipynb
tags:
  - pyvips
  - IIIF
  - Amazon s3
hide:
  - toc
zenodo_concept_id: 7080836
---

This notebook converts the images extracted from the Post Office Directory PDFs into pyramidal TIFFs using pyvips and then uploads them to an Amazon s3 bucket for delivery via IIIF.

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}