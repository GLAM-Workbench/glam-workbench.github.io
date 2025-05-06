---
title: Save a Trove newspaper article as an image
description: Sometimes you want to be able to save a Trove newspaper article as an image. Unfortunately, the Trove web interface doesn't make this easy. The 'Download JPG' option actually loads an HTML page, and while you could individually save the images embedded in the HTML page, often articles are sliced up in ways that make the whole thing hard to read and use. This notebook grabs the page on which an article was published, and then crops the page image to the boundaries of the article. The result is a complete, intact image which presents the article as it was originally published. And if the article is split across multiple pages, you'll get one image per page.
repo_url: https://github.com/GLAM-Workbench/trove-newspapers
repo_name: trove-newspapers
zenodo_concept_id: 3521724
notebook: Save-Trove-newspaper-article-as-image.ipynb
tags:
  - image
rocrate: https://raw.githubusercontent.com/GLAM-Workbench/trove-newspapers/master/ro-crate-metadata.json
page_type: notebook
---

![Screen capture](../images/run_save_images.gif)

{% include "notebook.md" %}
