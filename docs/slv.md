---
title: State Library of Victoria
repo_url: https://github.com/GLAM-Workbench/state-library-victoria
repo_name: state-library-victoria
---

# State Library of Victoria

The State Library of Victoria provides some machine-readable collection data as [downloads](https://www.slv.vic.gov.au/search-discover/open-data) and image data using IIIF.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/state-library-victoria/master?urlpath=lab)

## Tips, tools, and examples

### Download an image using the IIIF server and a Handle url

The State Library of Victoria makes many of its images available from an IIIF-compliant server. This means you can access and manipulate the images in standard ways set out by the IIIF Image API. Many images in the State Library's collection also have a permanent url, created using the Handle system. These are displayed in Trove. But there's no obvious way of getting an IIIF image from a Handle. That's what this notebook does.

* [Download from GitHub](https://github.com/GLAM-Workbench/state-library-victoria/blob/master/download_image_from_iiif.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/state-library-victoria/blob/master/download_image_from_iiif.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/state-library-victoria/master?urlpath=lab%2Ftree%2Fdownload_image_from_iiif.ipynb)

### More fun with IIIF

IIIF (the International Image Interoperability Framework) has defined a set of standards for publishing and using image collections. The State Library of Victoria makes many of its images available from an IIIF-compliant server. This means you can access and manipulate the images in standard ways set out by the IIIF Image API. This notebook demonstrates some of the possibilities.

* [Download from GitHub](https://github.com/GLAM-Workbench/state-library-victoria/blob/master/more_fun_with_iiif.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/state-library-victoria/blob/master/more_fun_with_iiif.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/state-library-victoria/master?urlpath=lab%2Ftree%2Fmore_fun_with_iiif.ipynb)

![Screenshot showing rotated image](images/slv-iiif-rotate.png)

## Contributors

{{ repo_contributors() }}