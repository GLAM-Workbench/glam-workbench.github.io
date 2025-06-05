---
title: Trove newspaper & gazette harvester
description: The Trove Newspaper & Gazette Harvester makes it easy to download large quantities of digitised articles from Trove's newspapers and gazettes. Just give it a search from the Trove web interface, and the harvester will save the metadata of all the articles in a CSV (spreadsheet) file for further analysis.
repo_name: trove-newspaper-harvester
repo_url: https://github.com/glam-workbench/trove-newspaper-harvester
zenodo_concept_id: 3545044
page_type: repo
rocrate: "https://raw.githubusercontent.com/GLAM-Workbench/trove-newspaper-harvester/master/ro-crate-metadata.json"
categories:
    - Harvesting
    - Exploring
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

{{ page.meta.description}}

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)


## Notebooks

{% for category in page.meta.categories %}

### {{category}}

{% for nb in page.meta.notebooks|selectattr("category", "equalto", category.lower())|sort(attribute="position") %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description.split("\n\n")[0] }}

{% endfor %}

{% endfor %}

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

{% include "nb-run-info.md" %}

{% if page.meta.zenodo_concept_id %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}

{% endif %}
