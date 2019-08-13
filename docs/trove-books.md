---
title: Trove books
repo_url: https://github.com/GLAM-Workbench/trove-books
repo_name: trove-books
---

Trove's 'book' zone includes books (of course), but also ephemera (like pamphlets and leaflets) and theses. You can access metadata from the book zone through the Trove API.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master)

## Tips, tools, and examples

### [Harvesting the text of digitised books (and ephemera)](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Harvesting-digitised-books.ipynb)  
This notebook harvests metadata and OCRd text from digitised works in Trove's book zone. Results of the harvest are available below.

### [Metadata for Trove digitised works](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Metadata-for-Trove-digitised-works.ipynb)  
In poking around to try and find a way of automating the download of OCR text from Trove's digitised books, I discovered that there's lots of useful metadata embedded in the page of a digitised work. Most of this metadata isn't available through the Trove API.

### [Getting the text of Trove books from the Internet Archive](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Getting-Trove-books-from-Internet-Archive.ipynb)  
Previously I've harvested the text of books digitised by the National Library of Australia and made available through Trove. But it occured to me it might be possible to get the full text of other books in Trove by making use of the links to the Open Library.

## Data and text

### OCRd text from Trove books (and ephemera)
Harvested: 15 April 2019

I've harvested 9,738 text files from digitised books using the notebook above. You can [browse the collection in CloudStor](https://cloudstor.aarnet.edu.au/plus/s/ugiw3gdijSKaoTL), or download the complete set as [a zip file (400mb)](https://cloudstor.aarnet.edu.au/plus/s/SrNqP4IOwF1fMBz).

### CSV formatted list of books with OCRd text
Harvested: 15 April 2019

This file provides metadata of 9,738 works in the Trove book zone that have OCRd text for download. You can [download the CSV file](https://render.githubusercontent.com/view/trove_digitised_books_with_ocr.csv), or [browse the metadata using Google Sheets](https://docs.google.com/spreadsheets/d/1O8Zs-n27j1T4zGcXEhbPOrwnbtcicvi7UM99Lh9JQQ8/edit?usp=sharing).

This file includes the following columns:

+ `children` – pipe-separated ids of any child works
+ `contributors` – pipe-separated names of contributors
+ `date` – publication date
+ `form` – work format
+ `fulltext_url` – link to the digitised version
+ `pages` – number of pages
+ `parent` – id of parent work (if any)
+ `text_downloaded` – file name of the downloaded OCR text
+ `text_file` – True/False is there any OCRd text
+ `title` – title of the work
+ `trove_id` – unique identifier
+ `url` – link to the metadata record in Trove
+ `volume` – volume/part number

### OCRd text from the Internet Archive of 'Australian' books listed in Trove  
I've harvested 1,513 text files from the Internet Archive of 'Australian' books listed in Trove using the notebook above. Trove's 'Australian content' filter was used to try to limit the results to books published in, or about, Australia. However, this is not always accurate and some of the harvested works don't seem to have an Australian connection. You can [browse the collection in CloudStor](https://cloudstor.aarnet.edu.au/plus/s/3h3GHfS3tQTDLaX).

### CSV formatted list of 'Australian' books in Trove with full text versions in the Internet Archive
Harvested: 24 May 2019

This file includes metadata of 1,511 'Australian' books listed in Trove that have freely available text versions in the Internet Archive. You can [download the CSV file](https://github.com/GLAM-Workbench/trove-books/blob/master/trove-books-in-ia.csv), or [browse the metadata using Google Sheets](https://docs.google.com/spreadsheets/d/1QgWaziVsryBaL-TX_iqoR_RmAwUy6CJ82CcYApoHkHA/edit?usp=sharing).

This file includes the following columns:

* `creators` – pipe-separated list of creators
* `date` – publication date
* `ia_formats` – pipe-separated list of file formats available from the Internet Archive (these can be downloaded from the IA)
* `ia_id` – Internet Archive identifier
* `ia_url` – link to more information in the Internet Archive
* `ol_id` – Open Library identifier
* `publisher` – publisher
* `text_filename` – name of the downloaded text file
* `title` – title of the book
* `trove_url` – link to more information in Trove
* `version_id` – Trove version identifier
* `work_id` – Trove work identifier
