---
title: Extract text from PDF images using Tesseract
description: This notebook uses Tesseract (OCR) to extract text directly from the images in the Tasmanian Post Office Directory PDFs.
repo_url: https://github.com/GLAM-Workbench/libraries-tasmania
repo_name: libraries-tasmania
notebook: tas-pod-ocr-with-tesseract.ipynb
tags:
  - Tesseract
  - OCR
hide:
  - toc
zenodo_concept_id: 7080836
---

This notebook uses Tesseract (OCR) to extract text directly from the images in the Tasmanian Post Office Directory PDFs.

Although I was able to [extract text from the PDFs directly](tas-pod-save-text-images.md), I wasn't happy with the quality. In particular, column layout detection was quite variable, munging values from different columns together. After a few tests, I decided that re-OCRing the images using [Tesseract](https://pypi.org/project/pytesseract/) would produce better results. Tesseract's automatic page layout detection does a pretty good job of identifying the columns, and the OCR quality in general seems better. There's still some munging of values across columns and various other errors, but I think the quality is good enough for searching.

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