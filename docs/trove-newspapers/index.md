---
title: Trove newspapers
repo_name: trove-newspapers
repo_url: https://github.com/glam-workbench/trove-newspapers
zenodo_concept_id: 3521724
---

{{ git_latest_tag() }}

Assorted experiments and examples working with Trove’s digitised newspapers.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Trove newspapers in context

!!! note ""
    Notebooks in this section look at the Trove newspaper corpus as a whole, to try and understand what's there, and what's not.

### [:material-notebook-outline: Visualise the total number of newspaper articles in Trove by year & state](visualise-total-newspaper-articles-by-state-year.md) {: data-toc-omit }

Trove currently includes more 200 million digitised newspaper articles published between 1803 and 2015. In this notebook we explore how those newspaper articles are distributed over time, and by state.

### [:material-notebook-outline: Analyse rates of OCR correction](Analysing_OCR_corrections.md) {: data-toc-omit }

The full text of newspaper articles in Trove is extracted from page images using Optical Character Recognition (OCR). The accuracy of the OCR process is influenced by a range of factors including the font and the quality of the images. Many errors slip through. Volunteers have done a remarkable job in correcting these errors, but it's a huge task. This notebook explores the scale of OCR correction in Trove.

### [:material-notebook-outline: Finding non-English newspapers in Trove](find-non-english-newspapers.md) {: data-toc-omit }

There are a growing number of non-English newspapers digitised in Trove. However, if you're only searching using English keywords, you might never know that they're there. I thought it would be useful to generate a list of non-English newspapers, but it wasn't quite as straightforward as I thought.

### [:material-notebook-outline: Beyond the copyright cliff of death](Beyond_the_copyright_cliff_of_death.md) {: data-toc-omit }

Most of the newspaper articles on Trove were published before 1955, but there are some from the later period. Let's find out how many, and which newspapers they were published in.

### [:material-notebook-outline: Gathering historical data about the addition of newspaper titles to Trove](historical-data-newspaper-titles.md) {: data-toc-omit }

The number of digitised newspapers available through Trove has increased dramatically since 2009. Understanding when newspapers were added is important for historiographical purposes, but there's no data about this available directly from Trove. This notebook uses web archives to extract lists of newspapers in Trove over time, and chart Trove's development.


## Visualising searches

!!! note ""
    Notebooks in this section demonstrate some ways of visualising searches in Trove newspapers – seeing everything rather than just a list of search results.

### [:material-notebook-outline: QueryPic](querypic.md) {: data-toc-omit }

This is the latest iteration of QueryPic with many new features. Use it to visualise searches in Trove's newspapers and gazettes, aggregating the number of results by day, month, or year. Simply copy and paste a url from a Trove web search to get started. QueryPic's charts help you explore patterns and trends, and if you find something interesting you can click on a point to view the results in Trove for that time period.

### [:material-notebook-outline: QueryPic Deconstructed  ](QueryPic_deconstructed.md) {: data-toc-omit }

This is an older version of QueryPic that lets you build queries using keywords, states, or newspapers.

### [:material-notebook-outline: Visualise Trove newspaper searches over time](visualise-searches-over-time.md) {: data-toc-omit }

This notebook helps you zoom out and explore how the number of Trove newspaper articles in your search results varies over time by using the `decade` and year `facets`. We then combine this approach with other search facets to see how we can slice a set of results up in different ways to investigate historical changes.

### [:material-notebook-outline: Map Trove newspaper results by state](Map-newspaper-results-by-state.md) {: data-toc-omit }
Uses the Trove `state` facet to create a choropleth map that visualises the number of search results per state.  

### [:material-notebook-outline: Map Trove newspaper results by place of publication](Map-newspaper-results-by-place-of-publication.md) {: data-toc-omit }

Uses the Trove `title` facet to find the number of results per newspaper, then merges the results with a dataset of geolocated newspapers to map where articles were published.

### [:material-notebook-outline: Map Trove newspaper results by place of publication over time](Map-newspaper-results-by-place-of-publication-over-time.md) {: data-toc-omit }

Adds a time dimension to the examples in the previous notebook to create an animated heatmap.


## Harvesting data

!!! note ""
    Notebooks in this section help you harvest data relating to Trove's newspapers. To harvest all the newspaper articles from a search, see the [Trove Newspaper and Gazette Harvester](/trove-harvester/).

### [:material-notebook-outline: Harvest information about newspaper issues](harvest_newspaper_issues.md) {: data-toc-omit }

When you search Trove's newspapers, you find articles – these articles are grouped by page, and all the pages from a particular date make up an issue. But how do you find out what issues are available? On what dates were newspapers published? This notebook shows how you can get information about issues from the Trove API.

### [:material-notebook-outline: Harvest the issues of a newspaper as PDFs](harvest_newspaper_issues_as_pdfs.md) {: data-toc-omit }

This notebook harvests issues of a newspaper as PDFs – one PDF per issue. If the newspaper has an long print run, this will consume large amounts of time and disk space, so you might want to limit your harvest by date range.

### [:material-notebook-outline: Harvest Australian Women's Weekly covers (or the front pages of any newspaper)](harvest-aww-covers-and-newspaper-front-pages.md) {: data-toc-omit }

Somewhat confusingly, the *Australian Women's Weekly* is in with Trove's digitised newspapers and not the rest of the magazines. There are notebooks in the GLAM Workbench's journals section to help harvest all of a journal's covers as images, so I thought I should do the same for the Weekly. This notebook can be easily adjusted to download the front pages of any digitised newspaper.

## Useful tools

!!! note ""
    Notebooks in this section provide useful tools that extend or enhance the Trove web interface and API.

### [:material-notebook-outline: Save a Trove newspaper article as an image](Save-Trove-newspaper-article-as-image.md) {: data-toc-omit }

Sometimes you want to be able to save a Trove newspaper article as an image. Unfortunately, the Trove web interface doesn't make this easy. The 'Download JPG' option actually loads an HTML page, and while you could individually save the images embedded in the HTML page, often articles are sliced up in ways that make the whole thing hard to read and use. This notebook grabs the page on which an article was published, and then crops the page image to the boundaries of the article. The result is a complete, intact image which presents the article as it was originally published. And if the article is split across multiple pages, you'll get one image per page.

### [:material-notebook-outline: Save Trove newspaper article as image web app](Save-Trove-newspaper-article-as-image-app.md) {: data-toc-omit }

A simple web app that helps you save a Trove newspaper article as an image.

### [:material-notebook-outline: Download a page image](Save-page-image.md) {: data-toc-omit }

The Trove web interface doesn’t provide a way of getting high-resolution page images from newspapers. This simple app lets you download page images as complete, high-resolution JPG files.

### [:material-notebook-outline: Generate an article thumbnail](Get-article-thumbnail.md) {: data-toc-omit }

Generate a nice square thumbnail image for a newspaper article.

### [:material-notebook-outline: Upload Trove newspaper articles to Omeka-S](Upload-Trove-newspapers-to-Omeka.md) {: data-toc-omit }

This notebook steps through the process of uploading Trove newspaper articles to your own Omeka-S instance via the API. As well as uploading the article metadata, it attaches image(s) and PDFs of the articles, and creates a linked record for the publishing newspaper. The source of the articles can be a Trove search, a Trove list, a Zotero collection, or just a list of article ids.

## Tips and tricks

!!! note ""
    Notebooks in this section provide some useful hints to use with the Trove API.

### [:material-notebook-outline: Today’s news yesterday](Todays-news-yesterday.md) {: data-toc-omit }

Uses the `date` index and the `firstpageseq` parameter to find articles from exactly 100 years ago that were published on the front page. It then selects one of the articles at random and downloads and displays an image of the front page.

### [:material-notebook-outline: Create a Trove OCR corrections ticker](Create-a-Trove-corrections-ticker.md) {: data-toc-omit }

Uses the `has:corrections` parameter to get the total number of newspaper articles with OCR corrections, then displays the results, updating every five seconds.

### [:material-notebook-outline: Get the page coordinates of a digitised newspaper article from Trove](trove-newspapers-get-coordinates-of-articles.md) {: data-toc-omit }

This notebook demonstrates how to find the coordinates of a newspaper article on a digitised page.

## Get creative

!!! note ""
    Notebooks in this section look at ways you can use data from Trove newspapers in creative ways.

### [:material-notebook-outline: Make composite images from lots of Trove newspaper thumbnails](Composite-thumbnails.md) {: data-toc-omit }

This notebook starts with a search in Trove's newspapers. It uses the Trove API to work its way through the search results. For each article it creates a thumbnail image using the code from this notebook. Once this first stage is finished, you have a directory full of lots of thumbnails. The next stage takes all those thumbnails and pastes them one by one into a BIG image to create a composite, or mosaic.

### [:material-notebook-outline: Create 'scissors and paste' messages from Trove newspaper articles](trove-newspapers-scissors-and-paste.md) {: data-toc-omit }

When you search for a term in Trove's digitised newspapers and click on individual article, you'll see your search terms are highlighted. If you look at the code you'll see the highlighted box around the word includes its page coordinates. That means that if we search for a word, we can find where it appears on a page, and by cropping the page to those coordinates we can create an image of an individual word. By combining these images we can create scissors and paste style messages!

### [:material-notebook-outline: Create large composite images from snipped words](trove-newspapers-create-composite-from-words.md) {: data-toc-omit }

This is a variation of the 'scissors & paste' notebook that extracts words from Trove newspaper images and compiles them into messages. In this notebook, you can harvest multiple versions of a list of words and compile them all into one big image.

## Data and images

### [:material-folder-outline: Data about newspaper issues](data-newspaper-issues.md) {: data-toc-omit }

This datatset includes information about digitised newspaper issues, including the total number of issues per newspaper/year, and a complete list of issues, identifiers and dates for every digitised newspaper in Trove.

### [:material-folder-outline: Newspaper titles harvested from web archives](csv-newspaper-titles-from-web-archives.md) {: data-toc-omit }

The number of digitised newspapers available through Trove has increased dramatically since 2009. Understanding when newspapers were added is important for historiographical purposes, but there's no data about this available directly from Trove. These datasets were created by harvesting information about newspaper titles in Trove from web archives.

### [:material-folder-outline: Australian Women's Weekly issues and front covers, 1933 to 1982](dataset-aww-covers.md) {: data-toc-omit }

This dataset contains metadata and front cover images of 2,566 Australian Women's Weekly issues on Trove published between 1933 and 1982.

### [:material-folder-outline: Trove newspapers with non-English language content](list-non-english-newspapers.md) {: data-toc-omit }

This dataset contains information about newspapers published in languages other than English that have been digitised and made available through Trove. Data about the languages present in newspapers was generated by harvesting a sample of articles from each newspaper using the Trove API, and then using language detection software on the OCRd text of each article.

### [:material-folder-outline: Trove newspapers with articles published after 1954](csv-newspapers-post-54.md) {: data-toc-omit }

CSV formatted dataset containing a list of digitised newspapers in Trove with articles published after 1954 (the copyright cliff of death).

### [:material-folder-outline: OCR corrections in Trove newspapers](csv-newspapers-corrections.md) {: data-toc-omit }

OCR errors in Trove's digitised newspapers can be corrected by users. To help understand patterns in newspaper correction, this dataset has been created to record information about the number of articles with corrections.

{% include "nb-run-info.md" %}

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}
