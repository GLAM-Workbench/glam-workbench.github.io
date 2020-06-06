---
title: Trove journals
repo_url: https://github.com/GLAM-Workbench/trove-journals
repo_name: trove-journals
---

Trove's 'journals' zone includes journals and journal articles, as well as other research outputs and things like press releases. You can access metadata from the journal zone through the Trove API, but to get text and images you need to use some screen scraping.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master)

## Tips, tools, and examples

### Create a list of Trove's digitised journals  
Everyone know's about Trove's newspapers, but there is also a growing collection of digitised journals available in the journals zone. They're not easy to find, however, which is why I created the [Trove Titles](https://trove-titles.herokuapp.com/) web app. This notebook uses the Trove API to harvest metadata relating to digitised journals – or more accurately, journals that are freely available online in a digital form. This includes some born digital publications that are available to view in formats like PDF and MOBI, but excludes some digital journals that have access restrictions.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Create-digitised-journals-list.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Create-digitised-journals-list.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Create-digitised-journals-list.ipynb)

### Get OCRd text from a digitised journal in Trove
Many of the digitised journals available in Trove make OCRd text available for download – one text file for each journal issue. However, while there are records for journals and articles in Trove (and available through the API), there are no records for issues. So how do we find them? This notebook shows how to extract issue data from a digitised journal and download OCRd text for each issue.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Get-text-from-a-Trove-journal.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Get-text-from-a-Trove-journal.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Get-text-from-a-Trove-journal.ipynb)

### Get covers (or any other pages) from a digitised journal in Trove
In another notebook, I showed how to get issue metadata and OCRd texts from a digitised journal in Trove. It's also possible to download page images and PDFs. This notebook shows how to download all the cover images from a specified journal. With some minor modifications you could download any page, or range of pages.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Get-page-images-from-a-Trove-journal.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Get-page-images-from-a-Trove-journal.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Get-page-images-from-a-Trove-journal.ipynb)

### Download the OCRd text for ALL the digitised journals in Trove!
Using the code and data from the previous two notebooks, you can download the OCRd text from every digitised journal. If you're going to try this, you'll need a lots of patience and lots of disk space. Needless to say, don't try this on a cloud service like Binder. Fortunately you don't have to do it yourself, as I've already run the harvest and made all the text files available. See below for details. I repeat, you probably don't want to do this yourself. The point of this notebook is really to document the methodology used to create the repository.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Download-text-for-all-digitised-journals.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Download-text-for-all-digitised-journals.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Download-text-for-all-digitised-journals.ipynb)

### Harvest parliament press releases from Trove  
Trove includes more than 370,000 press releases, speeches, and interview transcripts issued by Australian federal politicians and saved by the Parliamentary Library. You can view them all in Trove by searching for nuc:"APAR:PR" in the journals zone. This notebook shows you how to harvest both metadata and full text from a search of the parliamentary press releases. The metadata is available from Trove, but to get the full text we have to go back to the Parliamentary Library's database, ParlInfo.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Harvest-parliament-press-releases.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Harvest-parliament-press-releases.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Harvest-parliament-press-releases.ipynb)

### Harvesting data from the Bulletin
This is a more specific example of harvesting metadata and OCRd text from a digitised journal, in this case *The Bulletin*. It also shows how you can get the front cover images (or any other page).

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Harvesting-data-from-the-Bulletin.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Harvesting-data-from-the-Bulletin.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Harvesting-data-from-the-Bulletin.ipynb)

### Finding editorial cartoons in the Bulletin
In another notebook I showed how you could download all the front pages of The Bulletin (and other journals) as images. Amongst the front pages you'll find a number of full page editorial cartoons under The Bulletin's masthead. But you'll also find that many of the front pages are advertising wrap arounds. The full page editorial cartoons were a consistent feature of The Bulletin for many decades, but they moved around between pages one and eleven. That makes them hard to find. I wanted to try and assemble a collection of all the editorial cartoons, but how?

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Finding_editorial_cartoons_in_the_Bulletin.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Finding_editorial_cartoons_in_the_Bulletin.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Finding_editorial_cartoons_in_the_Bulletin.ipynb)

### Harvesting data from Home
This is a more specific example of harvesting metadata and OCRd text from a digitised journal, in this case *The Home*. It also shows how you can get the front cover images (or any other page).

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-journals/blob/master/Harvesting-data-from-the-Home.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/Harvesting-data-from-the-Home.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-journals/master?filepath=Harvesting-data-from-the-Home.ipynb)

### Topic Modelling of Australian Parliamentary Press Releases by  [Adel Rahmani](https://twitter.com/dinkumdata)
This notebook explores the [Politicians talking about 'immigrants' and 'refugees'](#politicians-talking-about-immigrants-and-refugees) collection of press releases (see below). Adel notes: 'I was curious about the contents of the press releases, however, at more than 12,000 documents the collection is too overwhelming to read through, so I thought I'd get the computer to do it for me, and use topic modelling to poke aroung the corpus.'

* [View using NBViewer](https://nbviewer.jupyter.org/github/adelr/trove-refugee/blob/master/Analyses.ipynb)

## Data and text

### CSV formatted list of journals available from Trove in digital form
Harvested: 25 August 2019

This file provides metadata of 2,620 journals that are available from Trove in a digital form. You can [download the CSV file](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-journals/blob/master/digital-journals.csv).

This file includes the following columns:

+ `fulltext_url` – the url of the landing page of the digital version of the journal
+ `title` – the title of the journal
+ `trove_id` – the 'nla.obj' part of the fulltext_url, a unique identifier for the digital journal
+ `trove_url` – url of the journal's metadata record in Trove

### CSV formatted list of journals with OCRd text
Harvested: 25 August 2019  

This file provides metadata of 720 digitised journals in Trove that have OCRd text for download. You can [download the CSV file](https://github.com/GLAM-Workbench/trove-journals/blob/master/digital-journals-with-text.csv). You can also [browse a human-readable list](https://github.com/GLAM-Workbench/trove-journals/blob/master/digital-journals-with-text.md).

This file includes the following columns:

+ `fulltext_url` – the url of the landing page of the digital version of the journal
+ `title` – the title of the journal
+ `trove_id` – the 'nla.obj' part of the fulltext_url, a unique identifier for the digital journal
+ `trove_url` – url of the journal's metadata record in Trove
+ `issues` – the number of available issues
+ `issues_with_text` – the number of issues that OCRd text could be downloaded from
+ `directory` – the directory in which the files from this journal have been saved (relative to the output directory)

### OCRd text from Trove digitised journals
Harvested: 25 August 2019

Using the notebook above I harvested metadata and OCRd text from Trove's digitised journals.

+ 719 journals had OCRd text available for download
+ OCRd text was downloaded from 33,035 journal issues
+ About 8gb of text was downloaded

The complete collection of text files for all the journals can be [browsed here](https://github.com/GLAM-Workbench/trove-journals/blob/master/digital-journals-with-text.md) and downloaded [using this repository on CloudStor](https://cloudstor.aarnet.edu.au/plus/s/QOmnqpGQCNCSC2h).

### Editorial cartoons from The Bulletin, 1886 to 1952

Harvested: 9 May 2019

Using the notebook above I downloaded at least one full page editorial cartoon for every issue of *The Bulletin* from 4 September 1886 to 17 September 1952. In total there are 3,471 images (approximately 60gb). The complete collection can be [downloaded from CloudStor](https://cloudstor.aarnet.edu.au/plus/s/bI7hJREvO0oJLGL). The names of each image file provide useful contextual metadata. For example, the file name `19330412-2774-nla.obj-606969767-7.jpg` tells you:

+ `19330412` – the cartoon was published on 12 April 1933
+ `2774` – it was published in issue number 2774
+ `nla.obj-606969767` – the Trove identifier for the issue, can be used to make a url eg `https://nla.gov.au/nla.obj-606969767`
+ `7` – on page 7

To make it easier to browse the images, I've compiled them into a series of PDFs – one PDF for each decade. The PDFs include lower resolution versions of the images together with their publication details and a link to Trove. They're all [available from DropBox](https://www.dropbox.com/sh/rulkbsqgfe8cyhv/AABel9b95buJSG5hZrVCvaQsa?dl=0):

+ [1886 to 1889](https://www.dropbox.com/s/altjl6jixwv5pt0/bulletin-1886-1889.pdf?dl=0) (45mb PDF)
+ [1890 to 1899](https://www.dropbox.com/s/p15swmact2c9euf/bulletin-1890-1899.pdf?dl=0) (139mb PDF)
+ [1900 to 1909](https://www.dropbox.com/s/0rivg50s8qam2et/bulletin-1900-1909.pdf?dl=0) (147mb PDF)
+ [1910 to 1919](https://www.dropbox.com/s/pdsj6xjot0l928w/bulletin-1910-1919.pdf?dl=0) (153mb PDF)
+ [1920 to 1929](https://www.dropbox.com/s/64x9y5nvgez1q3o/bulletin-1920-1929.pdf?dl=0) (159mb PDF)
+ [1930 to 1939](https://www.dropbox.com/s/8mytp5qhqcrctt3/bulletin-1930-1939.pdf?dl=0) (151mb PDF)
+ [1940 to 1949](https://www.dropbox.com/s/go3vyuqq0td6oqd/bulletin-1940-1949.pdf?dl=0) (146mb PDF)
+ [1950 to 1952](https://www.dropbox.com/s/klcv0gyjs81c0pm/bulletin-1950-1952.pdf?dl=0) (42mb PDF)

### Politicians talking about 'immigrants' and 'refugees'  
Using the notebook above I harvested parliamentary press releases that included any of the terms 'immigrant', 'asylum seeker', 'boat people', 'illegal arrivals', or 'boat arrivals'. A total of 12,619 text files were harvested. You can [browse the files on CloudStor](https://cloudstor.aarnet.edu.au/plus/s/Msoj978Zlrud40g), or download the [complete dataset as a zip file (43mb)](https://cloudstor.aarnet.edu.au/plus/s/diwB0tnpv1X1ORN).

## Cite as

Sherratt, Tim. (2019, November 18). GLAM-Workbench/trove-journals (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3545216>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3545216.svg)](https://doi.org/10.5281/zenodo.3545216)
