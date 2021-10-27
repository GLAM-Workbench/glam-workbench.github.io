---
title: Trove books
repo_url: https://github.com/GLAM-Workbench/trove-books
repo_name: trove-books
zenodo_concept_id: 3549480
---

Trove's 'book' zone includes books (of course), but also ephemera (like pamphlets and leaflets) and theses. You can access metadata from the book zone through the Trove API.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab/tree/index.md)

## Harvesting data

### Harvesting the text of digitised books (and ephemera)
This notebook harvests metadata and OCRd text from digitised works in Trove's book zone. Results of the harvest are available below.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/Harvesting-digitised-books.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Harvesting-digitised-books.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab%2Ftree%2FHarvesting-digitised-books.ipynb)

### Metadata for Trove digitised works
In poking around to try and find a way of automating the download of OCR text from Trove's digitised books, I discovered that there's lots of useful metadata embedded in the page of a digitised work. Most of this metadata isn't available through the Trove API.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/Metadata-for-Trove-digitised-works.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Metadata-for-Trove-digitised-works.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab%2Ftree%2FMetadata-for-Trove-digitised-works.ipynb)

### Getting the text of Trove books from the Internet Archive
Previously I've harvested the text of books digitised by the National Library of Australia and made available through Trove. But it occured to me it might be possible to get the full text of other books in Trove by making use of the links to the Open Library.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/Getting-Trove-books-from-Internet-Archive.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/Getting-Trove-books-from-Internet-Archive.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab%2Ftree%2FGetting-Trove-books-from-Internet-Archive.ipynb)

## Exploring harvested books

### Counting words and phrases
This notebook provides a simple example of extracting word and ngram frequencies from the OCRd text of a digitised book using TextBlob and Wordcloud. The text is downloaded from the Cloudstor repository created by the full harvest of Trove digitised books.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/counting-words-in-text.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/counting-words-in-text.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab%2Ftree%2Fcounting-words-in-text.ipynb)

### Recipe generator
In this notebook we use TextBlob to extract nouns, verbs, and sentences from the OCRd text of a 19th century cookery book. We try to clean things up a bit, using regular expressions to discard likely OCR errors. Then we recombine the various parts in random combinations to create delicious recipes for all occasions. Enjoy!

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-books/blob/master/recipe-generator.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-books/blob/master/recipe-generator.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab%2Ftree%2Frecipe-generator.ipynb)

![Screenshot of recipe generator results](images/recipe-generator.png)

### Exploring the Digitised Books Collection from Trove by  [Adel Rahmani](https://twitter.com/dinkumdata)

This notebook explores the [9,738 text files](https://glam-workbench.github.io/trove-books/#ocrd-text-from-trove-books-and-ephemera) from digitised books available below. Adel notes:
'A particular feature of this book collection is that it is multilingual, therefore I'll be focusing a bit on that, and on the use of the topic model to figure out what the collection is about.'

* [View using NBViewer](https://nbviewer.jupyter.org/github/adelr/trove-books/blob/master/Trove_Digitised_Books.ipynb)

## Data and text

### OCRd text from Trove books and ephemera
Harvested: August 2021

I've harvested 26,762 files of OCRd text from digitised books and ephemera using the notebook above. You can [browse the full collection in CloudStor](https://cloudstor.aarnet.edu.au/plus/s/ugiw3gdijSKaoTL). There's about 3.6gb in total. You can also use this [**searchable database running on Glitch**](https://trove-digital-books.glitch.me/data/trove-digital-books) to identify and download texts of interest.

### CSV formatted list of books available in digital form
Harvested: August 2021

This file provides metadata of 42,174 works in the Trove book zone that are available in digital form. You can [download the CSV file](https://github.com/GLAM-Workbench/trove-books/blob/master/trove_digitised_books_with_ocr.csv), or explore using a [**searchable database running on Glitch**](https://trove-digital-books.glitch.me/data/trove-digital-books).

The CSV file includes the following columns:

* `title` – title of the work
* `url` – link to the metadata record in Trove
* `contributors` – pipe-separated names of contributors
* `date` – publication date
* `format` – the type of work, eg 'Book' or 'Government publication', can have multiple values (pipe-separated)
* `fulltext_url` – link to the digital version
* `trove_id` – unique identifier of the digital version
* `language` – main language of the work
* `rights` – copyright status
* `pages` – number of pages
* `form` – work format, generally one of 'Book', 'Multi volume book', or 'Digital publication'
* `volume` – volume/part number
* `children` – pipe-separated ids of any child works
* `parent` – id of parent work (if any)
* `text_downloaded` – file name of the downloaded OCR text
* `text_file` – True/False is there any OCRd text

### Government publications in digital form
Harvested: 5 August 2021

This dataset combines records from the separate harvests of books and periodicals available in digital form that have the type 'Government publication'. You can explore it using a [**searchable database running on Glitch**](https://trove-government-publications.glitch.me/data/trove-government-publications).

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

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-books/master?urlpath=lab/tree/index.md)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See the [Using Binder](https://glam-workbench.net/using-binder/) section of the GLAM Workbench for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-books/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See the [Using Reclaim Cloud](https://glam-workbench.net/using-reclaim-cloud/) section GLAM Workbench [for more details.

### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name trove-books -v "$PWD":/home/jovyan/work glamworkbench/trove-books repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.md'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See the [Using Docker](https://glam-workbench.net/using-docker/) section of the GLAM Workbench for more details.

## Cite as

{{ git_latest_version }}
