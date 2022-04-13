---
title: Unique subdomains of gov.au in SURT format
description: This is a dataset of unique subdomains in the gov.au domain.
repo_url: https://github.com/GLAM-Workbench/web-archives
repo_name: web-archives
zenodo_concept_id: 3894078
tags:
  - API
  - metadata
hide:
  - toc
---

*Harvested in April 2022*

This is a dataset of unique subdomains within the gov.au domain. It was generated from [this dataset](harvest-of-govau-subdomains.md) using [this notebook](exploring-govau-subdomains.md). The dataset is in CSV format, and contains a single column, `urlkey`, which full domain in SURT (Sort-friendly URI Reordering Transform) format.

[Download from CloudStor (2.4mb)](https://cloudstor.aarnet.edu.au/plus/s/F3BjoCaS5U3BHCh/download?path=gov-au-domains-split-20220406155220.csv){ .md-button .md-button--primary } 

### Related resources

* [Exploring subdomains in the whole of gov.au](exploring-govau-subdomains.md)
* [Harvest of unique urls from the gov.au domain](harvest-of-govau-subdomains.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}