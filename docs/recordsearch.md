---
repo_name: recordsearch
repo_url: https://github.com/glam-workbench/recordsearch
---

# RecordSearch

[RecordSearch](https://recordsearch.naa.gov.au/) is the online collection database of the National Archives of Australia. Based on the [series system](http://www.naa.gov.au/collection/fact-sheets/fs06.aspx), RecordSearch provides rich, contextual information about series, items, agencies, and functions.

Unfortunately RecordSearch doesn't provide access to machine-readable data through an API, so we have to resort to screen scraping. The notebooks here all make use of the [RecordSearch Tools library](https://github.com/wragge/recordsearch_tools) to handle the scraping.

If you plan to `git clone` this repository, make sure you include the `--recurse-submodules` option. This will grab the RecordSearch Tools code along with the notebooks.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master)


## Tools, tips, and examples

### Harvest items from a search in RecordSearch
Ever searched for items in RecordSearch and wanted to save the results as a CSV file, or in some other machine-readable format? This notebook walks you through the process of creating, managing, and saving item searches – all the way from search terms to downloadable dataset. You can even download all the images from items that have been digitised! And if you want to harvest series with more than 20,000 items, some strategies for this are included as well.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/harvesting_items_from_a_search.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/harvesting_items_from_a_search.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?urlpath=lab%2Ftree%2Fharvesting_items_from_a_search.ipynb)

### Harvest files with the access status of 'closed'  
The National Archives of Australia's RecordSearch database includes some information about files that we're not allowed to see. These files have been through the access examination process and ended up with an access status of 'closed'. While you can search by access status in RecordSearch, you can't explore the reasons, so if you want to dig any deeper you need to harvest the data. This notebook shows you how.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/harvest_closed_files.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/harvest_closed_files.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?filepath=harvest_closed_files.ipynb)

### Harvesting functions from the RecordSearch interface  
This notebook attempts to extract information from the RecordSearch interface about the hierarchy of functions it uses to describe the work of government agencies. [Previous explorations](https://timsherratt.org/research-notebook/aggregated-archives/notes/naa-functions/) have shown that the NAA's use of functions is rather inconsistent. All I'm doing here is finding out what functions RecordSearch itself says it is using. This may not be complete, but it seems like a useful starting point.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/harvesting_functions_from_recordsearch.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/harvesting_functions_from_recordsearch.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?filepath=harvesting_functions_from_recordsearch.ipynb)

### How many of the functions are actually used?
In this notebook we'll import data about functions that we've harvested earlier and search for each of these functions in RecordSearch to see how many are actually used.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/how_many_functions_are_used.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/how_many_functions_are_used.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?filepath=how_many_functions_are_used.ipynb)

### Harvest agencies associated with *all* functions  
This notebook loops through the list of functions that were extracted from the RecordSearch interface and saves basic details of the agencies responsible for each function. To keep down the file size and avoid too much duplication it doesn't include the full range of relationships that an agency might have. If you want the full agency data, use the app below to harvest agencies associated with an individual function or hierarchy.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/get_all_agencies_by_function.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/get_all_agencies_by_function.ipynb)
* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?filepath=get_all_agencies_by_function.ipynb)

### Download the contents of a digitised file  
RecordSearch lets you download a PDF of a digitised file, but sometimes it's more convenient to work with individual images. Just give this app the barcode of a digitised file and it will grab all the images as JPGs, zip them up into a folder, and generate a download link.

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/get_images_from_a_digitised_file.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/get_images_from_a_digitised_file.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?urlpath=apps%2Fget_images_from_a_digitised_file.ipynb)

### Get a list of agencies associated with a function
RecordSearch describes the business of government in terms of 'functions'. A function is an area of responsibility assigned to a particular government agency. Over time, functions change and move between agencies. If you're wanting to track particular areas of government activity, such as 'migration' or 'meteorology', it can be useful to start with functions, then follow the trail through agencies, series created by those agencies, and finally items contained within those series. This app makes it easy for you to download a list agencies associated with a particular function.  

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/get_agencies_associated_with_function.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/get_agencies_associated_with_function.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?urlpath=apps%2Fget_agencies_associated_with_function.ipynb)

### Who's responsible?
The National Archives of Australia's RecordSearch database divides government activities up into a series of functions. Over time, different agencies have been made responsible for these functions, and it can be interesting to track how these responsibilities have shifted. This notebook uses data about functions harvested from RecordSearch to create a a simple visualisation of the agencies responsible for a selected function.  

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/display_agencies_by_function.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/display_agencies_by_function.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?urlpath=apps%2Fdisplay_agencies_by_function.ipynb)

![Screen capture demonstrating use of app](images/rs_agencies_by_function.gif)

### DFAT Cable Finder
If you ever need to find a file in the National Archives of Australia that contains a specific numbered cable from the Department of Foreign Affairs this is the tool for you! Just give it a cable number and it will look in the series listed below for a file that might contain the cable. For each possible match it returns a link to the file as well as a bit of information about it.  

* [Download from GitHub](https://github.com/GLAM-Workbench/recordsearch/blob/master/Find_cables.ipynb)
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/recordsearch/blob/master/Find_cables.ipynb)
* [Run live on Binder in Appmode](https://mybinder.org/v2/gh/GLAM-Workbench/recordsearch/master?urlpath=apps%2FFind_cables.ipynb)

![Screen capture demonstrating use of app](images/cable-finder.gif)

## Cite as

Sherratt, Tim. (2019, November 17). GLAM-Workbench/recordsearch (Version v0.1.0). Zenodo. <http://doi.org/10.5281/zenodo.3544754>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3544754.svg)](https://doi.org/10.5281/zenodo.3544754)
