---
title: Trove journals
description: Trove's 'journals' zone includes journals and journal articles, as well as other research outputs and things like press releases. You can access metadata from the journal zone through the Trove API, but to get text and images you need to use some screen scraping.
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
zenodo_concept_id: 3545215
---

{{ git_latest_tag() }}

Trove's 'journals' zone includes journals and journal articles, as well as other research outputs and things like press releases. You can access metadata from the journal zone through the Trove API, but to get text and images you need to use some screen scraping.

[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?urlpath=lab)

## Harvesting metadata

### [:material-notebook-outline: Create a list of Trove's digitised journals](create-list-digitised-journals.md) 

Everyone know's about Trove's newspapers, but there is also a growing collection of digitised journals available in the journals zone. They're not easy to find, however, which is why I created the [Trove Titles](https://trove-titles.herokuapp.com/) web app. This notebook uses the Trove API to harvest metadata relating to periodicals available from Trove in digital form. As well as digitised publications, this includes born digital publications in formats like PDF and MOBI that have been made available through the edeposit program.

## Harvesting text

### [:material-notebook-outline: Get OCRd text from a digitised journal in Trove](get-ocrd-text-from-digitised-journal.md) 

Many of the digitised journals available in Trove make OCRd text available for download – one text file for each journal issue. However, while there are records for journals and articles in Trove (and available through the API), there are no records for issues. So how do we find them? This notebook shows how to extract issue data from a digitised journal and download OCRd text for each issue.


### [:material-notebook-outline: Download the OCRd text for ALL the digitised journals in Trove!](get-ocrd-text-from-all-journals.md) 

Using the code and data from the previous two notebooks, you can download the OCRd text from every digitised journal. If you're going to try this, you'll need a lots of patience and lots of disk space. Needless to say, don't try this on a cloud service like Binder. Fortunately you don't have to do it yourself, as I've already run the harvest and made all the text files available. See below for details. I repeat, you probably don't want to do this yourself. The point of this notebook is really to document the methodology used to create the repository.

### [:material-notebook-outline: Harvest parliament press releases from Trove](harvest-parliament-press-releases.md) 

Trove includes more than 380,000 press releases, speeches, and interview transcripts issued by Australian federal politicians and saved by the Parliamentary Library. You can view them all in Trove by searching for nuc:"APAR:PR" in the books & libraries category. This notebook shows you how to harvest both metadata and full text from a search of the parliamentary press releases. The metadata is available from Trove, but to get the full text we have to go back to the Parliamentary Library's database, ParlInfo.

### [:material-notebook-outline: Create a database to search across each line of text in a series of volumes](create-text-db-indexed-by-line.md) 

The code in this notebook was used to create the [NSW Post Office Directories search interface](https://nsw-post-office-directories-yajhxrvxsa-ts.a.run.app/) which lets you search across 54 volumes from 1886 to 1950. The same code, with minor modifications, could be used to index any series of publication where it would be useful to search by line (rather than Trove's default 'article') – for example, lists, directories and gazetteers – turning them into searchable databases.

## Harvesting images

### [:material-notebook-outline: Get covers (or any other pages) from a digitised journal in Trove](get-covers-from-digitised-journal.md) 

In another notebook, I showed how to get issue metadata and OCRd texts from a digitised journal in Trove. It's also possible to download page images and PDFs. This notebook shows how to download all the cover images from a specified journal. With some minor modifications you could download any page, or range of pages.

### [:material-notebook-outline: Finding editorial cartoons in the Bulletin](finding-editorial-cartoons-in-bulletin.md) 

In another notebook I showed how you could download all the front pages of The Bulletin (and other journals) as images. Amongst the front pages you'll find a number of full page editorial cartoons under The Bulletin's masthead. But you'll also find that many of the front pages are advertising wrap arounds. The full page editorial cartoons were a consistent feature of The Bulletin for many decades, but they moved around between pages one and eleven. That makes them hard to find. I wanted to try and assemble a collection of all the editorial cartoons, but how?

## Exploring harvested text

### [:material-notebook-outline: Topic Modelling of Australian Parliamentary Press Releases by Adel Rahmani](topic-modelling-parliament-press-releases.md) 

This notebook explores the [Politicians talking about 'immigrants' and 'refugees'](#politicians-talking-about-immigrants-and-refugees) collection of press releases (see below). Adel notes: 'I was curious about the contents of the press releases, however, at more than 12,000 documents the collection is too overwhelming to read through, so I thought I'd get the computer to do it for me, and use topic modelling to poke aroung the corpus.'

## Datasets

### [:material-database-outline: CSV formatted list of journals available from Trove in digital form](csv-digital-journals.md) 

*Harvested: 31 August 2022*

This file provides metadata of 8,662 periodicals that are available from Trove's journal zone in digital form. This includes both 'digitised' periodicals, and born-digital periodicals submitted through Electronic Legal Deposit. Note that this list contains 8,728 records as there are some duplicates where multiple Trove work records point to the same digitised periodicals. The duplicates have been left in as they include different metadata, and can be easily removed with Pandas. 

### [:material-database-outline: CSV formatted list of journals with OCRd text](csv-journals-with-ocr.md) 

*Harvested: 31 August 2022*

This file provides metadata of 1,430 digitised periodicals in Trove that have OCRd text for download.

### [:material-database-outline: List of journals with OCRd text](journals-with-ocr.md) 

*Harvested: 31 August 2022*

This page provides a human-readable list of 1,430 digitised periodicals in Trove that have OCRd text for download. Links are provided to download and explore each

### [:material-folder-text-outline: OCRd text from Trove digitised journals](ocrd-text-all-journals.md) 

*Harvested: 31 August 2022*

Using the notebooks above I harvested metadata and OCRd text from Trove's digitised periodicals.

+ 1,430 periodicals had OCRd text available for download
+ OCRd text was downloaded from 41,645 periodical issues
+ About 9gb of text was downloaded

### [:material-database-outline: Government publications in digital form](../trove-books/government-publications-in-digital-form.md) 

*Harvested: 5 August 2021*

This dataset combines records from the separate harvests of books and periodicals available in digital form that have the type 'Government publication'.


### [:material-folder-text-outline: Editorial cartoons from The Bulletin, 1886 to 1952](bulletin-cartoons-collection.md) 

*Harvested: 9 May 2019*

Using the notebook above I downloaded at least one full page editorial cartoon for every issue of *The Bulletin* from 4 September 1886 to 17 September 1952. In total there are 3,471 images (approximately 60gb). 

### [:material-folder-text-outline: Politicians talking about 'immigrants' and 'refugees'](politicans-press-releases-refugees.md) 

Using the notebook above I harvested parliamentary press releases that included any of the terms 'immigrant', 'asylum seeker', 'boat people', 'illegal arrivals', or 'boat arrivals'. A total of 12,619 text files were harvested.

### [:material-folder-text-outline: Politicians talking about COVID](politicans-press-releases-covid.md) 

Using the notebook above I harvested parliamentary press releases that included any of the terms 'COVID' or 'coronavirus'. A total of 3,995 text files were harvested.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}