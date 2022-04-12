---
title: Unique subdomains of gov.au split into components
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

This is a dataset of unique subdomains within the gov.au domain. It was generated from [this dataset](harvest-of-govau-subdomains.md) using [this notebook](exploring-govau-subdomains.md). The dataset is in CSV format, and contains the following columns:

| Field | Description |
|-------|-------------|
| `urlkey` | The full domain of the url in SURT (Sort-friendly URI Reordering Transform) format |
| `number of pages` | The number of captures in the original dataset from this subdomain |
| `0` | First level domain – `au` |
| `1` | Second level domain – `gov` |
| `2` | Third level domain |
| `3` | Fourth level domain |
| `4` | Fifth level domain |
| `5` | Sixth level domain |
| `6` | Seventh level domain |
| `7` | Eighth level domain |
| `8` | Ninth level domain |
| `9` | Tenth level domain |
| `domain` | The full domain name in conventional dot separated format |

[Download from CloudStor (2.4mb)](https://cloudstor.aarnet.edu.au/plus/s/F3BjoCaS5U3BHCh/download?path=gov-au-domains-split-20220406155220.csv){ .md-button .md-button--primary } 

### Related resources

* [Exploring subdomains in the whole of gov.au](exploring-govau-subdomains.md)
* [Harvest of unique urls from the gov.au domain](harvest-of-govau-subdomains.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}