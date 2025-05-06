---
title: Trove People & Organisations
description: Trove's People and Organisations zone aggregates information about individuals and organisations, bringing multiple sources together under a single identifier. Data is available through a number of APIs.
repo_url: https://github.com/GLAM-Workbench/trove-people
repo_name: trove-people
zenodo_concept_id: 7645058
---

{{ git_latest_tag() }}

Trove's People and Organisations zone aggregates information about individuals and organisations, bringing multiple sources together under a single identifier.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Harvesting data

There are two methods of harvesting the complete set of data from the People and Organisations zone – using the [OAI-PMH API](http://www.nla.gov.au/apps/peopleaustralia-oai/), or using the main Trove API in conjunction with the [SRU interface](http://www.nla.gov.au/apps/srw/search/peopleaustralia). The OAI-PMH method is *much* faster, but includes duplicate records that you'll need to filter out afterwards.

### [:material-notebook-outline: Harvesting the complete set of data from the People and Organisations zone](complete_harvest.md) {: data-toc-omit }

This notebook demonstrates the API/SRU method for creating a complete data harvest.

### [:material-notebook-outline: Harvesting the complete set of data from the People and Organisations zone using OAI-PMH](complete_harvest_oai.md) {: data-toc-omit }

This notebook demonstrates the OAI-PMH method for creating a complete data harvest.

## Analysing data

### [:material-notebook-outline: Extract some aggregated data from the complete harvest](extract_aggregated_data_from_harvest.md) {: data-toc-omit }

The complete harvest of records in the Trove People & Organisations zone is very large – more than 1.3 million records, almost 9gb of data. To do some analysis of its content, we'll extract some aggregate totals by looping through all the EAC-CPF records.

### [:material-notebook-outline: Harvest SRU API results as JSON](get_sru_results_as_json.md) {: data-toc-omit }

You can query the People & Organisations data using the SRU (Search/Retrieve via URL) API, and retrieve data in a number of XML formats, the richest and most complex of which is EAC-CPF. However, the XML records are not easy to work with, so to simplify further processing, this notebook queries the SRU interface and then converts the EAC-CPF XML results into JSON.

### [:material-notebook-outline: Visualising intersections and overlaps between data sources](intersections.md) {: data-toc-omit }

The People & Organisations zone aggregates information from a range of data sources into individual records. In this notebook we'll explore connections between the data sources.

### [:material-notebook-outline: Get VIAF links relating to Trove People & Organisation records](viaf.md) {: data-toc-omit }

VIAF, the Virtual International Authority File, aggregates identifiers for people and organisations from a wide range of name authority systems, including Libraries Australia. Many records in Trove's People & Organisations zone have Libraries Australia identifiers attached to them. Using these LA identifers it's possible to query VIAF for links related to a Trove record in other name authority systems.

## Data

### [:material-folder-outline: Complete harvest of People and Organisations data](complete_harvest_dataset.md) {: data-toc-omit }

This is a complete harvest of the EAC-CPF records in Trove's People & Organisations zone.

### [:material-folder-outline: Aggregated data extracted from People and Organisations data](aggregated_datasets.md) {: data-toc-omit }

These datasets provide aggregated data extracted from the complete harvest of data from Trove's People and Organisations zone.

<!-- START RUN INFO -->

{% include "nb-run-info.md" %}

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}