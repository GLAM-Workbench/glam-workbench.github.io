---
title: Trove newspaper & gazette harvester
repo_name: trove-newspaper-harvester
repo_url: https://github.com/glam-workbench/trove-newspaper-harvester
zenodo_concept_id: 3545044
---

The Trove Newspaper & Gazette Harvester makes it easy to download large quantities of digitised articles from Trove's newspapers and gazettes. Just give it a search from the Trove web interface, and the harvester will save the metadata of all the articles in a CSV (spreadsheet) file for further analysis. You can also save the full text of every article, as well as copies of the articles as JPG images, and even PDFs. While the web interface will only show you the first 2,000 results matching your search, the Newspaper & Gazette Harvester will get **everything**.

You can install the Harvester as a [Python command line tool](https://pypi.org/project/troveharvester/), or use it in one of these notebooks below:

* [Using TroveHarvester to get newspaper and gazette articles in bulk](#using-troveharvester-to-get-newspaper-articles-in-bulk) – shows you how to use the command line tool in a Jupyter notebook
* [Trove Harvester web app](#trove-harvester-web-app) – provides a simple web interface to the newspaper & gazette harvester

Both notebooks can be run live, online using the Binder service, so you can start harvesting articles straight away without installing any software. All you need to get started is:

* A search url – just construct your search using the [Trove web interface](http://trove.nla.gov.au/newspaper/)), and when you're happy with the results, copy the url.
* A [Trove API key](http://help.nla.gov.au/trove/building-with-trove/apihttp://help.nla.gov.au/trove/building-with-trove/api).

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab)

## Your harvested data

When you start a new harvest, the harvester looks for a directory called [data](data). Within this directory it creates another directory for your harvest. The name of this directory will be in the form of a unix timestamp – a very large number that represents the number of seconds since 1 January 1970. So this means the directory with the largest number will contain the most recent harvest.

The harvester saves your results inside this directory. There will be at least two files created for each harvest:

* `results.csv` – a text file containing the details of all harvested articles
* `metadata.json` – a configuration file which stores all the details of the harvest

The `results.csv` file is a plain text CSV (Comma Separated Values) file. You can open it with any spreadsheet program. The details recorded for each article are:

* `article_id` – a unique identifier for the article
* `title` – the title of the article
* `newspaper_id` – a unique identifier for the newspaper or gazette title (this can be used to retrieve more information or build a link to the web interface)
* `newspaper_title` – the name of the newspaper (or gazette)
* `page` – page number (of course), but might also indicate the page is part of a supplement or special section
* `date` – in ISO format, YYYY-MM-DD
* `category` – one of ‘Article’, ‘Advertising’, ‘Detailed lists, results, guides’, ‘Family Notices’, or ‘Literature’
* `words` – number of words in the article
* `illustrated` – is it illustrated (values are y or n)
* `corrections` – number of text corrections
* `snippet` – short text sample
* `url` – the persistent url for the article
* `page_url` – the persistent url of the page on which the article is published

If you’ve asked for PDFs or text files, there will be additional directories containing those files. Files containing the OCRd text of the articles will be saved in a directory named `text`. These are just plain text files, stripped on any HTML. These files include some basic metadata in their file titles – the date of the article, the id number of the newspaper, and the id number of the article. So, for example, the filename `19460104-1002-206680758.txt` tells you:

* `19460104` – the article was published on 4 January 1946 (YYYYMMDD)
* `1002` – the article was published in [*The Tribune*](https://trove.nla.gov.au/newspaper/title/1002)
* `206680758` – the [article's unique identifier](http://nla.gov.au/nla.news-article206680758)

As you can see, you can use the newspaper and article ids to create direct links into Trove:

* to a newspaper or gazette `https://trove.nla.gov.au/newspaper/title/[newspaper id]`
* to an article `http://nla.gov.au/nla.news-article[article id]`

Similarly, if you've asked for copies of the articles as images, they'll be in a directory named `image`. The image file names are similar to the text files, but with an extra id number for the page from which the image was extracted. So, for example, the image filename `19250411-460-140772994-11900413.jpg` tells you:

* `19250411` – the article was published on 11 April 1925 (YYYYMMDD)
* `460` – the article was published in [*The Australasian*](https://trove.nla.gov.au/newspaper/title/460)
* `140772994` – the [article's unique identifier](http://nla.gov.au/nla.news-article140772994)
* `11900413` – the [page's unique identifier](https://trove.nla.gov.au/newspaper/page/11900413) (some articles can be split over multiple pages)

Once you have your data you can start exploring! You'll find some Jupyter notebooks below that provide examples of analysing and visualising both the metadata and the full text.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master)

## Tools, tips, and examples

### Using TroveHarvester to get newspaper and gazette articles in bulk  
An introduction to the Trove Harvester command line tool. Edit a few cells and you'll be harvesting metadata and full text of thousands of articles in minutes.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/Using-TroveHarvester-to-get-newspaper-articles-in-bulk.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/Using-TroveHarvester-to-get-newspaper-articles-in-bulk.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab/tree/Using-TroveHarvester-to-get-newspaper-articles-in-bulk.ipynb)

### Trove Harvester web app
A simple web interface to the TroveHarvester, the easiest way to harvest data from Trove.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/newspaper_harvester_app.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/newspaper_harvester_app.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=%2Fapps%2Fnewspaper_harvester_app.ipynb)

![Screen capture of Trove Harvester](images/trove-harvester.gif)

### Display the results of a harvest as a searchable database using Datasette

![Screen capture of Datasette](images/datasette-row.png)

[Datasette](https://github.com/simonw/datasette) is 'a tool for exploring and publishing data'. Give it a CSV file and it turns it into a fully-searchable database, running in your browser. It supports facets, full-text search, and, with a bit of tweaking, can even present images. Although Datasette is a command-line tool, we can run from within a Jupyter notebook, and open a new window to display the results. This notebook shows you how to load the newspaper data you've harvested into Datasette, and start it up. If you've also harvested full-text and images from the newspaper articles, you can add these to your database as well!

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/display_harvest_results_using_datasette.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/display_harvest_results_using_datasette.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab/tree/display_harvest_results_using_datasette.ipynb)

### Exploring your TroveHarvester data
This notebook shows some ways in which you can analyse and visualise the article metadata you've harvested — show the distribution of articles over time and space; find which newspapers published the most articles. (Under construction)

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/Exploring-your-TroveHarvester-data.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/Exploring-your-TroveHarvester-data.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab/tree/Exploring-your-TroveHarvester-data.ipynb)

### Exploring harvested text files  
This notebook suggests some ways in which you can aggregate and analyse the individual OCRd text files for each article — look at word frequencies ; calculate TF-IDF values. (Under construction)

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspaper-harvester/blob/master/Explore-harvested-text-files.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspaper-harvester/blob/master/Explore-harvested-text-files.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab/tree/Explore-harvested-text-files.ipynb)

## Cite as

{{ git_latest_version }}
