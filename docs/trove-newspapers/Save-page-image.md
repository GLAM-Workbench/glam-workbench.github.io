---
title: Download a page image
description: The Trove web interface doesn’t provide a way of getting high-resolution page images from newspapers. This simple app lets you download page images as complete, high-resolution jpeg files.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
notebook: Save-page-image.ipynb
tags:
  - image
  - web app
hide:
  - toc
---

*{{ description }}*

<!--
![Screen capture](../images/trove-page-images.gif)

{{ description }}

[Run live in Voila](https://trove-newspaper-apps.uw.r.appspot.com/voila/render/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab%2Ftree%2F{{notebook}})
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/master?urlpath=lab%2Ftree%2F{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}
-->

!!! info "Options"

    Page images are available in seven resolutions that correspond to the zoom levels in the Trove web interface. As a rough guide:

    - level 1 is around 900 x 1200 px (500kb)
    - level 4 is around 2700 x 3500 px (3mb)
    - level 7 is around 6100 x 7800 px (7mb)

Just enter a page or article url in the box below and click the button...

<input id="page-id" type="text" class="md-input md-input--stretch" placeholder="page or article url">

<label for="level"><small>Size: </small></label> 
<select class="md-select" name="level" id="level">
  <option value="1">Level 1</option>
  <option value="2">Level 2</option>
  <option value="3">Level 3</option>
  <option value="4" selected>Level 4</option>
  <option value="5">Level 5</option>
  <option value="6">level 6</option>
  <option value="7">Level 7</option>
</select>

<div class="mdc-select mdc-select--filled demo-width-class">
  <input type="hidden" name="demo-input">
  <div class="mdc-select__anchor">
    <!-- Rest of component omitted for brevity -->
  </div>
</div>

<button id="download-image" class="md-button md-button--primary">Get image url</button> <button id="clear-image-results" class="md-button">Clear</button>

<div id="status" markdown>:material-loading:{.spinner}</div>

<div id="images"></div>

<script src="../../scripts/newspaper-page-images-script.js"></src>