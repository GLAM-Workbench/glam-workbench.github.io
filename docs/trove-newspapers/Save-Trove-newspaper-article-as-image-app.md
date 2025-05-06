---
title: Save Trove newspaper article as image web app
description: A simple web app that helps you save a Trove newspaper article as an image.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
notebook: Save-Trove-newspaper-article-as-image.ipynb
tags:
  - image
  - web app
hide:
  - toc
---

*{{description}}*


There’s no reliable way of downloading an image of a Trove newspaper article from the web interface. The image download option produces an HTML page with embedded images, and the article is often sliced into pieces to fit the page.

This app provides an easy-to-use workaround. Just enter an article url or identifier and you get back an image (or images if the article is split across multiple pages).

!!! info "Options"
    - **mask image** – check this to try and remove content from neighbouring articles
    - **retry** – check this if there's been an error and you want to force the app to try again

<!--

[Run live in Voila](https://trove-newspaper-apps.uw.r.appspot.com/voila/render/{{notebook}}){ .md-button .md-button--primary }

### Related resources

* [Save a Trove newspaper article as an image](Save-Trove-newspaper-article-as-image.md) (the notebook version of this app)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}
-->

Just enter an article identifier or url in the box below and click on the button...

<input id="article-id" type="text" class="md-input md-input--stretch" placeholder="enter article id or url">

<input id="mask-image" type="checkbox"> <label><small>mask image</small></label> <input id="retry" type="checkbox"> <label><small>retry</small></label>

<button id="download-image" class="md-button md-button--primary">Get images</button> <button id="clear-image-results" class="md-button">Clear</button>

<div id="status" markdown>:material-loading:{.spinner}</div>

<div id="images"></div>


<script src="../../scripts/newspaper-article-images-script.js"></src>

