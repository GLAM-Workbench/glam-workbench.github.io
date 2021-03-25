---
title: Trove newspapers
repo_name: trove-newspapers
repo_url: https://github.com/glam-workbench/trove-newspapers
---

Assorted experiments and examples working with Trove’s digitised newspapers

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab)

## Tips, tools, and examples

### QueryPic Deconstructed  
[QueryPic](http://dhistory.org/querypic/) is a tool I created many years ago to visualise searches in Trove's digitised newspapers. It shows you the number of articles each year that match your query — instead of a page of search results, you see the complete result set. You can look for patterns and trends across time. This is a deconstructed, extended, and hackable version of QueryPic.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/QueryPic_deconstructed.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/QueryPic_deconstructed.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=%2Fapps%2FQueryPic_deconstructed.ipynb)

![Screen capture](images/querypic-aliens.png)

### Visualise Trove newspaper searches over time
This notebook helps you zoom out and explore how the number of Trove newspaper articles in your search results varies over time by using the `decade` and year `facets`. We then combine this approach with other search facets to see how we can slice a set of results up in different ways to investigate historical changes.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/visualise-searches-over-time.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/visualise-searches-over-time.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/visualise-searches-over-time.ipynb)

![Chart showing search results over time](images/search-over-time.png)

### Visualise the total number of newspaper articles in Trove by year and state
Trove currently includes more 200 million digitised newspaper articles published between 1803 and 2015. In this notebook we explore how those newspaper articles are distributed over time, and by state.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/visualise-total-newspaper-articles-by-state-year.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/visualise-total-newspaper-articles-by-state-year.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/visualise-total-newspaper-articles-by-state-year.ipynb)
* [View an interactive HTML chart](examples/trove-newspaper-articles-by-state-and-year.html)

![Chart showing number of newspaper articles by state and year](images/trove-newspapers-states.png)

### Map Trove newspaper results by state
Uses the Trove `state` facet to create a choropleth map that visualises the number of search results per state.  

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-state.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-state.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/=Map-newspaper-results-by-state.ipynb)

### Map Trove newspaper results by place of publication
Uses the Trove `title` facet to find the number of results per newspaper, then merges the results with a dataset of geolocated newspapers to map where articles were published.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Map-newspaper-results-by-place-of-publication.ipynb)

![Screen capture of heatmap](images/heatmap.png)

### Map Trove newspaper results by place of publication over time
Adds a time dimension to the examples in the previous notebook to create an animated heatmap.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication-over-time.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Map-newspaper-results-by-place-of-publication-over-time.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Map-newspaper-results-by-place-of-publication-over-time.ipynb)

### Analyse rates of OCR correction  

The full text of newspaper articles in Trove is extracted from page images using Optical Character Recognition (OCR). The accuracy of the OCR process is influenced by a range of factors including the font and the quality of the images. Many errors slip through. Volunteers have done a remarkable job in correcting these errors, but it's a huge task. This notebook explores the scale of OCR correction in Trove.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Analysing_OCR_corrections.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Analysing_OCR_corrections.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Analysing_OCR_corrections.ipynb)

### Finding non-English newspapers in Trove

There are a growing number of non-English newspapers digitised in Trove. However, if you're only searching using English keywords, you might never know that they're there. I thought it would be useful to generate a list of non-English newspapers, but it wasn't quite as straightforward as I thought.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/find-non-english-newspapers.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/find-non-english-newspapers.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/find-non-english-newspapers.ipynb)

### Today’s news yesterday
Uses the `date` index and the `firstpageseq` parameter to find articles from exactly 100 years ago that were published on the front page. It then selects one of the articles at random and downloads and displays an image of the front page.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Todays-news-yesterday.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Todays-news-yesterday.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Todays-news-yesterday.ipynb)

### Create a Trove OCR corrections ticker
Uses the `has:corrections` parameter to get the total number of newspaper articles with OCR corrections, then displays the results, updating every five seconds.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Create-a-Trove-corrections-ticker.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/mastea-Trove-corrections-ticker.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Create-a-Trove-corrections-ticker.ipynb)

![Screen capture](images/corrections-ticker.gif)

### Save a Trove newspaper article as an image
Sometimes you want to be able to save a Trove newspaper article as an image. Unfortunately, the Trove web interface doesn't make this easy. The 'Download JPG' option actually loads an HTML page, and while you could individually save the images embedded in the HTML page, often articles are sliced up in ways that make the whole thing hard to read and use. This notebook grabs the page on which an article was published, and then crops the page image to the boundaries of the article. The result is a complete, intact image which presents the article as it was originally published. And if the article is split across multiple pages, you'll get one image per page.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Save-Trove-newspaper-article-as-image.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Save-Trove-newspaper-article-as-image.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Save-Trove-newspaper-article-as-image.ipynb)
* [Run as an app using Voila](http://trove-newspaper-apps.herokuapp.com/voila/render/Save-Trove-newspaper-article-as-image-app.ipynb) (the easiest, no code option!)

![Screen capture](images/run_save_images.gif)

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
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Composite-thumbnails.ipynb)

<iframe allowfullscreen="true" src="https://easyzoom.com/embed/139535" width="800" height="400"></iframe>

### Create 'scissors and paste' messages from Trove newspaper articles

![Scissors and past message - help trapped inside trove](images/trapped-trove.jpg)

When you search for a term in Trove's digitised newspapers and click on individual article, you'll see your search terms are highlighted. If you look at the code you'll see the highlighted box around the word includes its page coordinates. That means that if we search for a word, we can find where it appears on a page, and by cropping the page to those coordinates we can create an image of an individual word. By combining these images we can create scissors and paste style messages!

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/trove-newspapers-scissors-and-paste.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/trove-newspapers-scissors-and-paste.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=%2Fapps%2Ftrove-newspapers-scissors-and-paste.ipynb)

### Create large composite images from snipped words

![Trove words - composite image](images/trove_words-cropped.jpg)

This is a variation of the 'scissors & paste' notebook that extracts words from Trove newspaper images and compiles them into messages. In this notebook, you can harvest multiple versions of a list of words and compile them all into one big image.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/trove-newspapers-create-composite-from-words.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/trove-newspapers-create-composite-from-words.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/trove-newspapers-create-composite-from-words.ipynb)

### Upload Trove newspaper articles to Omeka-S
This notebook steps through the process of uploading Trove newspaper articles to your own Omeka-S instance via the API. As well as uploading the article metadata, it attaches image(s) and PDFs of the articles, and creates a linked record for the publishing newspaper. The source of the articles can be a Trove search, a Trove list, a Zotero collection, or just a list of article ids.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Upload-Trove-newspapers-to-Omeka.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Upload-Trove-newspapers-to-Omeka.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Upload-Trove-newspapers-to-Omeka.ipynb)

### Harvest Australian Women's Weekly covers (or the front pages of any newspaper)
Somewhat confusingly, the *Australian Women's Weekly* is in with Trove's digitised newspapers and not the rest of the magazines. There are notebooks in the GLAM Workbench's journals section to help harvest all of a journal's covers as images, so I thought I should do the same for the Weekly. This notebook can be easily adjusted to download the front pages of any digitised newspaper.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/harvest-aww-covers-and-newspaper-front-pages.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/harvest-aww-covers-and-newspaper-front-pages.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/harvest-aww-covers-and-newspaper-front-pages.ipynb)

### Beyond the copyright cliff of death  
Most of the newspaper articles on Trove were published before 1955, but there are some from the later period. Let's find out how many, and which newspapers they were published in.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Beyond_the_copyright_cliff_of_death.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Beyond_the_copyright_cliff_of_death.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Beyond_the_copyright_cliff_of_death.ipynb)

### Get a list of Trove newspapers that doesn't include government gazettes
The Trove API includes an option to retrieve details of digitised newspaper titles. Version 2 of the API added a separate option to get details of government gazettes. However the original `newspaper/titles` requests actually returns both the newspaper and gazette titles, so there's no way of getting just the newspaper titles. This notebook explains the problem and provides a simple workaround.

* [Download from GitHub](https://github.com/GLAM-Workbench/trove-newspapers/blob/master/Get_newspaper_titles_not_including_gazettes.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/trove-newspapers/blob/master/Get_newspaper_titles_not_including_gazettes.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/trove-newspapers/master?urlpath=lab/tree/Get_newspaper_titles_not_including_gazettes.ipynb)

## Data and images

### CSV formatted list of Australian Women's Weekly issues, 1933 to 1982
Harvested: 26 July 2020

[This file](https://github.com/GLAM-Workbench/trove-newspapers/blob/58307d3ccae4d2c939ecb6aff59944f27d213842/data/aww-issues.csv) includes metadata for 2,566 issues of the Australian Women's Weekly from 1933 to 1982. Fields:

* `issue_id`: issue identifier
* `date`: issue date (YYYY-MM-DD)
* `url`: issue url
* `page_id`: identifier of the first page in this issue
* `image_file`: file name of downloaded image of front page.

### Australian Women's Weekly front covers, 1933 to 1982
Harvested: 26 July 2020

Using the notebook above, images of the front covers of Australian Women's Weekly issues on Trove were downloaded. Harvest details:

* 2,566 images were downloaded.
* The full set of images is [available from Cloudstor](https://cloudstor.aarnet.edu.au/plus/s/NaKjoKNFOGXXDNN).
* For easy browsing, I've compiled the images into a set of PDF files, one for each decade, available from Dropbox:
  * [1933 to 1939](https://www.dropbox.com/s/0j6zpeuw6tbey5k/aww-1933-1939.pdf?dl=0)
  * [1940 to 1949](https://www.dropbox.com/s/y1he8dd6h655weu/aww-1940-1949.pdf?dl=0)
  * [1950 to 1959](https://www.dropbox.com/s/i9gp9i51nofmlqo/aww-1950-1959.pdf?dl=0)
  * [1960 to 1969](https://www.dropbox.com/s/2of63tovcnphijo/aww-1960-1969.pdf?dl=0)
  * [1970 to 1979](https://www.dropbox.com/s/f2yxpg8u4dx5uf2/aww-1970-1979.pdf?dl=0)
  * [1980 to 1982](https://www.dropbox.com/s/xanohtas1fi7eu4/aww-1980-1982.pdf?dl=0)

### Trove newspapers with non-English language content

Created: 11 January 2021

Markdown formatted [list of newspapers with non-English content](https://gist.github.com/wragge/9aa385648cff5f0de0c7d4837896df97), created using the notebook above.
