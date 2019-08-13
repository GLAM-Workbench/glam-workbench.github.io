---
repo_name: library-archives-canada
repo_url: https://github.com/GLAM-Workbench/library-archives-canada
---

# Library Archives Canada

Unfortunately Library Archives Canada doesn't provide access to machine-readable data through an API, so we have to resort to screen scraping.

[![Binder](images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/library-archives-canada/master)

## Tools, tips, and examples

### [LAC naturalisation database, 1915-1946 — harvest by country](https://nbviewer.jupyter.org/github/GLAM-Workbench/library-archives-canada/blob/master/lac-naturalisation-1915-1945-harvest-by-country.ipynb)  
This notebook helps you extract the records of people from a specific country from the [LAC 1915-1946 naturalisations database](http://www.bac-lac.gc.ca/eng/discover/immigration/citizenship-naturalization-records/naturalized-records-1915-1951/Pages/introduction.aspx). There are numerous limitations and problems, including the fact that you can only get the first 2000 results. Women and children are not returned in a search by country, so the notebook makes an attempt to find and add them to the initial harvest. Here's an [example harvest for 'China'](https://github.com/GLAM-Workbench/library-archives-canada/blob/master/lac-naturalisations-china-with-families.csv).
