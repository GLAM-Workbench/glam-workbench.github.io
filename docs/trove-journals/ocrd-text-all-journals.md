---
title: OCRd text from Trove digitised journals
description: I harvested metadata and OCRd text from Trove's digitised periodicals. 1,163 periodicals had OCRd text available for download. OCRd text was downloaded from 51,928 periodical issues.
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
zenodo_concept_id: 3545215
tags:
  - text dataset
  - CSV dataset
  - metadata
hide:
  - toc
---

*Harvested: 5 August 2021*

I harvested metadata and OCRd text from Trove's digitised periodicals:

+ 1,163 periodicals had OCRd text available for download
+ OCRd text was downloaded from 51,928 periodical issues
+ About 10gb of text was downloaded

As well as downloading the text files, the harvesting process generated a CSV file for each periodical that captures details of each available issue with OCRd text. For each issue, the CSV file lists:

| Column | Description |
|--------|-------------|
`title` | the title of the periodical
`id` | the Trove object identifier for the issue
`details` | additional issue details such as volume and issue number
`pages` | the number of pages in the issue
`text_file` | the name of the file containing the OCRd text from this issue


[Download from CloudStor](https://cloudstor.aarnet.edu.au/plus/s/QOmnqpGQCNCSC2h){ .md-button .md-button--primary }

### Other options

* The complete collection of text files for all the periodicals can be [browsed here](https://github.com/GLAM-Workbench/trove-journals/blob/master/digital-journals-with-text.md)

### Related resources

* [Download the OCRd text for ALL the digitised journals in Trove!](get-ocrd-text-from-all-journals.md)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}


