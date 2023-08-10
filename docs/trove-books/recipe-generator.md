---
title: Recipe generator
description: In this notebook we use TextBlob to extract nouns, verbs, and sentences from the OCRd text of a 19th century cookery book. Then we recombine the various parts in random combinations to create delicious recipes for all occasions.
repo_url: https://github.com/GLAM-Workbench/trove-books
repo_name: trove-books
notebook: recipe-generator.ipynb
zenodo_concept_id: 3549480
tags:
  - text analysis
  - fun
hide:
  - toc
---

In this notebook we use TextBlob to extract nouns, verbs, and sentences from the OCRd text of a 19th century cookery book. We try to clean things up a bit, using regular expressions to discard likely OCR errors. Then we recombine the various parts in random combinations to create delicious recipes for all occasions. Enjoy!

![Screenshot of recipe generator results](../images/recipe-generator.png)

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/recipe-generator.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/recipe-generator.ipynb)


### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}