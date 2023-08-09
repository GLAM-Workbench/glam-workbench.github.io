---
title: CSV formatted list of Trove books available in digital form
description: This file provides metadata of 42,174 works in the Trove book zone that are available in digital form.
repo_url: https://github.com/GLAM-Workbench/trove-books
repo_name: trove-books
zenodo_concept_id: 3549480
tags:
  - CSV dataset
  - metadata
hide:
  - toc
file_url: https://github.com/GLAM-Workbench/trove-books/blob/master/trove_digitised_books_with_ocr.csv
---

**Harvested: August 2021**

This file provides metadata of 42,174 works in the Trove book zone that are available in digital form. 

[Download from GitHub](file_url){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv=https://github.com/GLAM-Workbench/trove-books/blob/master/trove-digital-books-datasette.csv){ .md-button .md-button--info }

The CSV file includes the following columns:

| Column | Contents |
|--------|----------|
`title` | title of the work
`url` | link to the metadata record in Trove
`contributors` | pipe-separated names of contributors
`date` | publication date
`format` | the type of work, eg 'Book' or 'Government publication', can have multiple values (pipe-separated)
`fulltext_url` | link to the digital version
`trove_id` | unique identifier of the digital version
`language` | main language of the work
`rights` | copyright status
`pages` | number of pages
`form` | work format, generally one of 'Book', 'Multi volume book', or 'Digital publication'
`volume` | volume/part number
`children` | pipe-separated ids of any child works
`parent` | id of parent work (if any)
`text_downloaded` | file name of the downloaded OCR text
`text_file` | True/False is there any OCRd text

The Datasette version renames and reorders some columns for clarity, and adds live links to download OCRd text.

| Column | Contents |
|--------|----------|
`title` | title of the work
`contributors` | pipe-separated names of contributors
`date` | publication date
`format` | the type of work, eg 'Book' or 'Government publication', can have multiple values (pipe-separated)
`language` | main language of the work
`copyright` | copyright status
`pages` | number of pages
`view_details_url` | link to the metadata record in Trove
`view_book_url` | link to the digital version
`download_text_url` | link to download the OCRd text
`form` | work format, generally one of 'Book', 'Multi volume book', or 'Digital publication'
`volume` | volume/part number
`parent` | id of parent work (if any)
`children` | pipe-separated ids of any child works

### Related resources

* [Harvesting the text of digitised books (and ephemera)](harvesting-text-of-digitised-books.md)
* [OCRd text from Trove books and ephemera](ocrd-text-from-trove-books.md)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}