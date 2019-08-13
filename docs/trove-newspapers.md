---
title: Trove newspapers
repo_name: trove-newspapers
repo_url: https://github.com/glam-workbench/trove-newspapers
---

Assorted experiments and examples working with Trove’s digitised newspapers

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master)

## Tips, tools, and examples

### Visualise Trove newspaper searches over time
This notebook helps you zoom out and explore how the number of Trove newspaper articles in your search results varies over time by using the `decade` and year `facets`. We then combine this approach with other search facets to see how we can slice a set of results up in different ways to investigate historical changes.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/visualise-searches-over-time.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/visualise-searches-over-time.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=visualise-searches-over-time.ipynb)

![Chart showing search results over time](images/search-over-time.png)

### Visualise the total number of newspaper articles in Trove by year and state
Trove currently includes more 200 million digitised newspaper articles published between 1803 and 2015. In this notebook we explore how those newspaper articles are distributed over time, and by state.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/visualise-total-newspaper-articles-by-state-year.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/visualise-total-newspaper-articles-by-state-year.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=visualise-total-newspaper-articles-by-state-year.ipynb)
* [View an interactive HTML chart](examples/trove-newspaper-articles-by-state-and-year.html)

![Chart showing number of newspaper articles by state and year](images/trove-newspapers-states.png)

### Map Trove newspaper results by state
Uses the Trove `state` facet to create a choropleth map that visualises the number of search results per state.  

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-state.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-state.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Map-newspaper-results-by-state.ipynb)

### Map Trove newspaper results by place of publication
Uses the Trove `title` facet to find the number of results per newspaper, then merges the results with a dataset of geolocated newspapers to map where articles were published.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Map-newspaper-results-by-place-of-publication.ipynb)

![Screen capture of heatmap](images/heatmap.png)

### Map Trove newspaper results by place of publication over time
Adds a time dimension to the examples in the previous notebook to create an animated heatmap.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication-over-time.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication-over-time.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Map-newspaper-results-by-place-of-publication-over-time.ipynb)

### Today’s news yesterday
Uses the `date` index and the `firstpageseq` parameter to find articles from exactly 100 years ago that were published on the front page. It then selects one of the articles at random and downloads and displays an image of the front page.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Todays-news-yesterday.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Todays-news-yesterday.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Todays-news-yesterday.ipynb)

### Create a Trove OCR corrections ticker
Uses the `has:corrections` parameter to get the total number of newspaper articles with OCR corrections, then displays the results, updating every five seconds.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Create-a-Trove-corrections-ticker.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/mastea-Trove-corrections-ticker.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Create-a-Trove-corrections-ticker.ipynb)

![Screen capture](images/corrections-ticker.gif)

### Save a Trove newspaper article as an image
This notebook grabs the page on which an article was published, and then crops the page image to the boundaries of the article. The result is an image which presents the article as it was originally published.  

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Save-Trove-newspaper-article-as-image.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Save-Trove-newspaper-article-as-image.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Save-Trove-newspaper-article-as-image.ipynb)
* [Run as an app using Voila](http://trove-newspaper-apps.herokuapp.com/voila/render/Save-Trove-newspaper-article-as-image-app.ipynb)

![Screen capture](images/run_save_images.gif)

### Upload Trove newspaper articles to Omeka-S
This notebook steps through the process of uploading Trove newspaper articles to your own Omeka-S instance via the API. As well as uploading the article metadata, it attaches image(s) and PDFs of the articles, and creates a linked record for the publishing newspaper. The source of the articles can be a Trove search, a Trove list, a Zotero collection, or just a list of article ids.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Upload-Trove-newspapers-to-Omeka.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Upload-Trove-newspapers-to-Omeka.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Upload-Trove-newspapers-to-Omeka.ipynb)

### Beyond the copyright cliff of death  
Most of the newspaper articles on Trove were published before 1955, but there are some from the later period. Let's find out how many, and which newspapers they were published in.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Beyond_the_copyright_cliff_of_death.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Beyond_the_copyright_cliff_of_death.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Beyond_the_copyright_cliff_of_death.ipynb)

### Download a page image  
The Trove web interface doesn’t provide a way of getting high-resolution page images from newspapers. This simple app lets you download page images as complete, high-resolution JPG files.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Save-page-image.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Save-page-image.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=%2Fapps%2FSave-page-image.ipynb)
* [Run as an app using Voila](http://trove-newspaper-apps.herokuapp.com/voila/render/Save-Trove-newspaper-page-as-image-app.ipynb)

![Screen capture](images/trove-page-images.gif)

### Generate an article thumbnail
Generate a nice square thumbnail image for a newspaper article.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Get-article-thumbnail.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Get-article-thumbnail.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=%2Fapps%2FGet-article-thumbnail.ipynb)
* [Run as an app using Voila](http://trove-newspaper-apps.herokuapp.com/voila/render/Create-thumbnail-from-Trove-newspaper-article-app.ipynb)

### Make composite images from lots of Trove newspaper thumbnails
This notebook starts with a search in Trove's newspapers. It uses the Trove API to work its way through the search results. For each article it creates a thumbnail image using the code from this notebook. Once this first stage is finished, you have a directory full of lots of thumbnails. The next stage takes all those thumbnails and pastes them one by one into a BIG image to create a composite, or mosaic.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Composite-thumbnails.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Composite-thumbnails.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Composite-thumbnails.ipynb)


<iframe allowfullscreen="true" src="https://easyzoom.com/embed/139535" width="800" height="400"></iframe>

### QueryPic Deconstructed  
[QueryPic](http://dhistory.org/querypic/) is a tool I created many years ago to visualise searches in Trove's digitised newspapers. It shows you the number of articles each year that match your query — instead of a page of search results, you see the complete result set. You can look for patterns and trends across time. This is a deconstructed, extended, and hackable version of QueryPic.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/QueryPic_deconstructed.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/QueryPic_deconstructed.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=%2Fapps%2FQueryPic_deconstructed.ipynb)

![Screen capture](images/querypic-aliens.png)

### Get a list of Trove newspapers that doesn't include government gazettes
The Trove API includes an option to retrieve details of digitised newspaper titles. Version 2 of the API added a separate option to get details of government gazettes. However the original `newspaper/titles` requests actually returns both the newspaper and gazette titles, so there's no way of getting just the newspaper titles. This notebook explains the problem and provides a simple workaround.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Get_newspaper_titles_not_including_gazettes.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Get_newspaper_titles_not_including_gazettes.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?filepath=Get_newspaper_titles_not_including_gazettes.ipynb)
