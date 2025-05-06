---
title: GLAM datasets in government data portals
description: This dataset contains information about open access datasets made available by Australian GLAM organisations through government data portals.
repo_url: https://github.com/GLAM-Workbench/gov-portals-data
repo_name: gov-portals-data
zenodo_concept_id: 13958899
tags:
  - CSV dataset
---

This dataset contains information about open access datasets made available by Australian GLAM organisations through government data portals. The dataset was created by harvesting data from state and national portals. The method is documented in [this notebook](https://glam-workbench.net/glam-data-portals/#harvesting-glam-data-from-government-portals) in the GLAM Workbench.

[Download complete dataset as zip](https://github.com/GLAM-Workbench/gov-portals-data/archive/refs/heads/main.zip){ .md-button .md-button--primary }

## Summary

*Harvested 21 October 2024*

Number of datasets: 443
Number of files: 1251

Datasets by organisation:

<table>
  <thead>
    <tr style="text-align: left;">
      <th>publisher</th>
      <th>number of datasets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>State Library of Queensland</td>
      <td>355</td>
    </tr>
    <tr>
      <td>Queensland State Archives</td>
      <td>212</td>
    </tr>
    <tr>
      <td>State Library of South Australia</td>
      <td>138</td>
    </tr>
    <tr>
      <td>South Australian Museum</td>
      <td>102</td>
    </tr>
    <tr>
      <td>State Records Office of Western Australia</td>
      <td>86</td>
    </tr>
    <tr>
      <td>Libraries Tasmania</td>
      <td>85</td>
    </tr>
    <tr>
      <td>State Library of Western Australia</td>
      <td>73</td>
    </tr>
    <tr>
      <td>Queensland Museum</td>
      <td>53</td>
    </tr>
    <tr>
      <td>State Records South Australia</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Public Records Office Victoria</td>
      <td>30</td>
    </tr>
    <tr>
      <td>History Trust of South Australia</td>
      <td>20</td>
    </tr>
    <tr>
      <td>NSW State Archives</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Western Australian Museum</td>
      <td>18</td>
    </tr>
    <tr>
      <td>National Library of Australia</td>
      <td>5</td>
    </tr>
    <tr>
      <td>State Library of NSW</td>
      <td>5</td>
    </tr>
    <tr>
      <td>State Library of Victoria</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Museum of Applied Arts and Sciences</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS)</td>
      <td>3</td>
    </tr>
    <tr>
      <td>National Archives of Australia</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Mount Gambier Library</td>
      <td>2</td>
    </tr>
    <tr>
      <td>National Portrait Gallery</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Museums Victoria</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

## Files

### `glam-datasets-from-gov-portals.csv`

This dataset contains details of all of the individual data files contained within datasets shared by GLAM organisations through government data portals. It contains the following columns:

| Column | Contents |
|--------|----------|
`dataset_title` | name of the dataset
`publisher` | name of the GLAM organisation contributing the data
`author` | usually the same as `publisher` but can contain other information such as an email address
`dataset_issued` | date when this dataset was published
`dataset_modified` | date when this dataset was last modified
`dataset_description` | description of the dataset
`source` | the portal through which the dataset is published, eg: `data.qld.gov.au`
`info_url` | link to page providing more information
`start_date` | earliest date of data within this dataset
`end_date` | latest date of data within this dataset
`file_title` | title of data file within this dataset
`download_url` | link to download data file
`format` | format of data file, eg 'CSV'
`file_description` | description of data file
`file_created` | date when this data file was created
`file_modified` | date when this data file was last modified
`file_size` | size of the data file
`licence` | licence applied to data file

[Download from Github](https://github.com/GLAM-Workbench/gov-portals-data/blob/main/glam-datasets-from-gov-portals.csv){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv=https%3A%2F%2Fgithub.com%2FGLAM-Workbench%2Fgov-portals-data%2Fblob%2Fmain%2Fglam-datasets-from-gov-portals.csv&install=datasette-homepage-table&fts=dataset_title%2Cdataset_description%2Cfile_title%2Cfile_description){ .md-button .md-button--info }

### `glam-datasets-from-gov-portals-csvs.csv`

This dataset contains details of all of the individual data files in CSV format contained within datasets shared by GLAM organisations through government data portals.  It contains the following columns:

| Column | Contents |
|--------|----------|
`dataset_title` | name of the dataset
`publisher` | name of the GLAM organisation contributing the data
`author` | usually the same as `publisher` but can contain other information such as an email address
`dataset_issued` | date when this dataset was published
`dataset_modified` | date when this dataset was last modified
`dataset_description` | description of the dataset
`source` | the portal through which the dataset is published, eg: `data.qld.gov.au`
`info_url` | link to page providing more information
`start_date` | earliest date of data within this dataset
`end_date` | latest date of data within this dataset
`file_title` | title of data file within this dataset
`download_url` | link to download data file
`format` | format of data file, eg 'CSV'
`file_description` | description of data file
`file_created` | date when this data file was created
`file_modified` | date when this data file was last modified
`file_size` | size of the data file
`licence` | licence applied to data file

[Download from Github](https://github.com/GLAM-Workbench/gov-portals-data/blob/main/glam-datasets-from-gov-portals-csvs.csv){ .md-button .md-button--primary } [Explore in Datasette](https://glam-workbench.net/datasette-lite/?csv=https%3A%2F%2Fgithub.com%2FGLAM-Workbench%2Fgov-portals-data%2Fblob%2Fmain%2Fglam-datasets-from-gov-portals-csvs.csv&install=datasette-homepage-table&fts=dataset_title%2Cdataset_description%2Cfile_title%2Cfile_description){ .md-button .md-button--info }


### `glam_datasets_from_gov_portals.md`

This is a markdown-formatted list of data files grouped by publishing organisation and dataset. 

[Download from Github](https://github.com/GLAM-Workbench/gov-portals-data/blob/main/glam_datasets_from_gov_portals.md){ .md-button .md-button--primary }

## Examples of use

- [GLAM datasets from Australian government data portals](https://glam-workbench.net/glam-datasets-from-gov-portals/) (embeds the Markdown list)
- Explore the *contents* of the CSV-formatted datasets using the [GLAM CSV Explorer](https://glam-workbench.github.io/csv-explorer/)
- Search across 279 datasets containing names using the [GLAM Name Index Search](https://glam-workbench.net/name-search/)

## Related resources

- [Harvesting GLAM data from government portals](/glam-data-portals/#harvesting-glam-data-from-government-portals)


--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}
