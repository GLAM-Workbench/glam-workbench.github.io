---
title: Trove newspaper & gazette harvester
description: The Trove Newspaper & Gazette Harvester makes it easy to download large quantities of digitised articles from Trove's newspapers and gazettes. Just give it a search from the Trove web interface, and the harvester will save the metadata of all the articles in a CSV (spreadsheet) file for further analysis.
repo_name: trove-newspaper-harvester
repo_url: https://github.com/glam-workbench/trove-newspaper-harvester
zenodo_concept_id: 3545044
---

{{ git_latest_tag() }}

!!! info
    Now updated to work with version 3 of the Trove API!

The Trove Newspaper & Gazette Harvester makes it easy to download large quantities of digitised articles from Trove's newspapers and gazettes. Just give it a search from the Trove web interface, and the harvester will save the metadata of all the articles in a CSV (spreadsheet) file for further analysis. You can also save the full text of every article, as well as copies of the articles as JPG images, and even PDFs. While the web interface will only show you the first 2,000 results matching your search, the Newspaper & Gazette Harvester will get **everything**.

You can [install the Harvester](https://wragge.github.io/trove-newspaper-harvester/) as a Python command line tool, or import it for use as a Python library. The notebooks below provide examples of the different ways you can use the Harvester and the data it creates.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Harvesting search results



### [:material-notebook-outline: Trove Harvester web app](harvester-web-app.md) {: data-toc-omit }

A simple web interface to the Trove Newspaper and Gazette Harvester – the easiest and quickest way to download all the results from a Trove newspaper or gazette search.


### [:material-notebook-outline: Using TroveHarvester to get newspaper and gazette articles in bulk](using-troveharvester.md) {: data-toc-omit }

This notebook provides an introduction to the Trove Newspaper and Gazette Harvester command line tool. Edit a few cells and you'll be harvesting metadata and full text of thousands of articles in minutes. This gives you you more control over your harvest than the simple web app, including the ability to restart a failed harvest.

### [:material-notebook-outline: Harvesting articles that mention "Anzac Day" on Anzac Day](harvest-specific-days.md) {: data-toc-omit }

This notebook provides an example of harvesting a complex search by using the `trove_newspaper_harvester` library directly. It shows how you can loop through a span of years to harvest results from a particular day each year.

## Exploring your harvested data

### [:material-notebook-outline: Display the results of a harvest as a searchable database using Datasette](display-harvest-results-in-datasette.md) {: data-toc-omit }

[Datasette](https://github.com/simonw/datasette) is 'a tool for exploring and publishing data'. Give it a CSV file and it turns it into a fully-searchable database, running in your browser. It supports facets, full-text search, and, with a bit of tweaking, can even present images. Although Datasette is a command-line tool, we can run from within a Jupyter notebook, and open a new window to display the results. This notebook shows you how to load the newspaper data you've harvested into Datasette, and start it up. If you've also harvested full-text and images from the newspaper articles, you can add these to your database as well!

### [:material-notebook-outline: Exploring your TroveHarvester data](exploring-troveharvester-data.md) {: data-toc-omit }

This notebook shows some ways in which you can analyse and visualise the article metadata you've harvested — show the distribution of articles over time and space; find which newspapers published the most articles. (Under construction)

### [:material-notebook-outline: Exploring harvested text files](exploring-troveharvester-text.md) {: data-toc-omit }

This notebook suggests some ways in which you can aggregate and analyse the individual OCRd text files for each article — look at word frequencies ; calculate TF-IDF values. (Under construction)

## Your harvested data

When you start a new harvest, the harvester by default looks for a directory called `data`. Within this directory it creates another directory for your harvest. The name of this directory will reflect the current date/time. The harvester saves your results inside this directory.

!!! info
    You can customise the name and location of the harvest directory using either the Harvester command-line tool, or using the Harvester as a Python library. See the [Trove Newspaper Harvester documentation](https://wragge.github.io/trove-newspaper-harvester/) for full details. The [Harvesting articles that mention "Anzac Day" on Anzac Day](harvest-specific-days.md) provides an example of this.

There will be at least three files created for each harvest:

* `harvester_config.json` a file that captures the parameters used to launch the harvest
* `ro-crate-metadata.json` a metadata file documenting the harvest in [RO-Crate](https://www.researchobject.org/ro-crate/) format
* `results.csv` contains details of all the harvested articles in a plain text CSV (Comma Separated Values) file. You can open it with any spreadsheet program.

The details recorded for each article are:

* `article_id` – a unique identifier for the article
* `title` – the title of the article
* `date` – in ISO format, YYYY-MM-DD
* `page` – page number (of course), but might also indicate the page is part of a supplement or special section
* `newspaper_id` – a unique identifier for the newspaper or gazette title (this can be used to retrieve more information or build a link to the web interface)
* `newspaper_title` – the name of the newspaper (or gazette)
* `category` – one of ‘Article’, ‘Advertising’, ‘Detailed lists, results, guides’, ‘Family Notices’, or ‘Literature’
* `words` – number of words in the article
* `illustrated` – is it illustrated (values are y or n)
* `edition` – edition of newspaper (rarely used)
* `supplement` – section of newspaper (rarely used)
* `section` – section of newspaper (rarely used)
* `url` – the persistent url for the article
* `page_url` – the persistent url of the page on which the article is published
* `snippet` – short text sample
* `relevance` – search relevance score of this result
* `status` – some articles that are still being processed will have the status "coming soon" and might be missing other fields
* `corrections` – number of text corrections
* `last_correction` – date of last correction
* `tags` – number of attached tags
* `comments` – number of attached comments
* `lists` – number of lists this article is included in
* `text` – path to text file
* `pdf` – path to PDF file
* `images` – path to image file(s)

!!! info
    If you use the harvester as a Python library, the metadata will be saved in a newline delimited JSON file (one JSON object per line) named `results.ndjson`, rather than `results.csv`. You can convert the `ndjson` file to CSV using the `Harvester.save_csv()` method. The `results.ndjson` stores the API results from Trove *as is*, with a couple of exceptions:

    * if the `text` parameter has been set to `True`, the `articleText` field will contain the path to a `.txt` file containing the OCRd text contents of the article (rather than containing the text itself)
    * similarly if PDFs and images are requests, the `pdf` and `image` fields int the `ndjson` file will point to the saved files.

If you’ve asked for text files PDFs or images, there will be additional directories containing those files. Files containing the OCRd text of the articles will be saved in a directory named `text`. These are just plain text files, stripped on any HTML. These files include some basic metadata in their file titles – the date of the article, the id number of the newspaper, and the id number of the article. So, for example, the filename `19460104-1002-206680758.txt` tells you:

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

Once you have your data you can start exploring! You'll find some Jupyter notebooks above that provide examples of analysing and visualising both the metadata and the full text.

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using ARDC Binder

[![Launch on ARDC Binder](../images/launch-ARDC-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

Click on the button above to launch the notebooks in this repository using the [ARDC Binder](https://mybinder.org/) service. This is a free service available to researchers in Australian universities. You'll be asked to log in with your university credentials. Note that sessions will close if you stop using the notebooks, and no data will be preserved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using ARDC Binder](https://glam-workbench.net/using-ardc-binder/) for more details.

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspaper-harvester/master?urlpath=lab/tree/index.md)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/trove-newspaper-harvester/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See [Using Reclaim Cloud](https://glam-workbench.net/using-reclaim-cloud/) for more details.

### Using the Nectar Cloud

![Screenshot of GLAM Workbench application](../images/nectar-gw-app.png){width="600"}

The [Nectar Research Cloud](https://ardc.edu.au/services/nectar-research-cloud/) (part of the Australian Research Data Commons) provides cloud computing services to researchers in Australian and New Zealand universities. Any university-affiliated researcher can log on to Nectar and receive [up to 6 months of free cloud computing time](https://tutorials.rc.nectar.org.au/allocation-management/03-account-and-trial). And if you need more, you can [apply for a specific project allocation](https://tutorials.rc.nectar.org.au/allocation-management/04-allocation-and-projects).

The GLAM Workbench is available in the Nectar Cloud as a pre-configured application. This means you can get it up and going without worrying about the technical infrastructure – just fill in a few details and you're away! To create an instance of this repository in the Nectar Cloud:

* Log in to the [Nectar Dashboard](https://dashboard.rc.nectar.org.au/) using your university credentials.
* From the Dashboard choose **Applications -> Browse Local**.
* Enter 'GLAM' in the filter box and hit Enter, you should see the GLAM Workbench application.
* Click on the GLAM Workbench application's  **Quick Deploy** button.
* Step through the various [configuration options](https://glam-workbench.net/using-nectar/#setting-up-your-own-glam-workbench-repository). Some options are only available if you have a dedicated project allocation.
* When asked to select a GLAM Workbench repository, choose 'Trove newspaper & gazette harvester' from the dropdown list.
* Complete the configuration and deploy your GLAM Workbench instance.
* The url to access your instance will be displayed once it's ready. Click on the url!

See [Using Nectar](https://glam-workbench.net/using-nectar/) for more information.

### Using Docker or Podman

You can use Docker or Podman to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/) or [Podman](https://podman.io/).
* From the command line, run the following command for Docker:  
  ```
  docker run -p 8888:8888 --name trove-newspaper-harvester quay.io/glamworkbench/trove-newspaper-harvester repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --ServerApp.token=''
  ```
* Or for Podman:  
  ```
  podman run -p 8888:8888 --name trove-newspaper-harvester quay.io/glamworkbench/trove-newspaper-harvester repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --ServerApp.token=''
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
