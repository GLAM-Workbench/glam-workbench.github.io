---
title: CSV formatted list of journals with OCRd text
description: This file provides metadata of 1,430 digitised periodicals in Trove that have OCRd text for download.
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
zenodo_concept_id: 3545215
tags:
  - CSV dataset
  - metadata
hide:
  - toc
file_url: https://github.com/GLAM-Workbench/trove-journals/blob/master/digital-journals-with-text-20220831.csv
---

**Harvested: 31 August 2022**

This file provides metadata of 1,430 digitised periodicals in Trove that have OCRd text for download. 

[Download the CSV file]({{ file_url }}){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv={{ file_url }}){ .md-button .md-button--info }

This file includes the following columns:

| Column | Description |
|--------|-------------|
`title` | the title of the periodical
`contributor` | information about creator or publisher
`issued` | publication date, or date range
`format` | the type of publication, all entries should include 'Periodical', but may include other types such as 'Government publication'
`trove_id` | the 'nla.obj' part of the fulltext_url, a unique identifier for the digital periodical
`trove_url` | url of the periodical's metadata record in Trove
`fulltext_url` | the url of the landing page of the digital version of the periodical
`fulltext_url_type` | the type of digital periodical, one of 'digitised', 'edeposit', or 'other'
`issues` | the number of available issues
`issues_with_text` | the number of issues that OCRd text could be downloaded from
`directory` | the directory in which the files from this journal have been saved (relative to the output directory)

### Other options

* [List of journals with OCRd text](journals-with-ocr.md)

### Related resources

* [Download the OCRd text for ALL the digitised journals in Trove!](get-ocrd-text-from-all-journals.md)
* [Create a list of Trove's digitised journals](create-list-digitised-journals.md)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}


