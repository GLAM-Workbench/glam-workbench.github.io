---
title: CSV formatted list of 'Australian' books in Trove with full text versions in the Internet Archive
description: This file includes metadata of 1,511 'Australian' books listed in Trove that have freely available text versions in the Internet Archive. 
repo_url: https://github.com/GLAM-Workbench/trove-books
repo_name: trove-books
zenodo_concept_id: 3549480
tags:
  - CSV dataset
  - metadata
  - Internet Archive
hide:
  - toc
---

**Harvested: 24 May 2019**

This file includes metadata of 1,511 'Australian' books listed in Trove that have freely available text versions in the Internet Archive.

[Download the CSV file](https://github.com/GLAM-Workbench/trove-books/blob/master/trove-books-in-ia.csv){ .md-button .md-button--primary }

This file includes the following columns:

| Column | Contents |
|--------|----------|
`creators` | pipe-separated list of creators
`date` | publication date
`ia_formats` | pipe-separated list of file formats available from the Internet Archive (these can be downloaded from the IA)
`ia_id` | Internet Archive identifier
`ia_url` | link to more information in the Internet Archive
`ol_id` | Open Library identifier
`publisher` | publisher
`text_filename` | name of the downloaded text file
`title` | title of the book
`trove_url` | link to more information in Trove
`version_id` | Trove version identifier
`work_id` | Trove work identifier

### Other options

* [Browse the metadata using Google Sheets](https://docs.google.com/spreadsheets/d/1QgWaziVsryBaL-TX_iqoR_RmAwUy6CJ82CcYApoHkHA/edit?usp=sharing)

### Related resources

* [Getting the text of Trove books from the Internet Archive](harvesting-text-from-books-in-ia.md)
* [OCRd text from the Internet Archive of 'Australian' books listed in Trove](ocrd-text-from-ia.md)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}