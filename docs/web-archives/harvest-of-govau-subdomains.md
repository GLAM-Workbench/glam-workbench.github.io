---
title: Harvest of unique urls from the gov.au domain
description: This is a dataset of urls in the gov.au domain harvested using the IA CDX API.
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

This is a dataset of (mostly unique) urls in the gov.au domain harvested using the IA CDX API. It is saved as newline-delimited JSON, with one JSON object per line. Each JSON object contains the following fields:

| Field | Description |
|-------|-------------|
| `urlkey` | The domain of the url in SURT (Sort-friendly URI Reordering Transform) format |
| `timestamp` | Time and date when the url was captured |
| `original` | The archived url |

[Download from CloudStor (75.7gb)](https://cloudstor.aarnet.edu.au/plus/s/F3BjoCaS5U3BHCh/download?path=gov-au-cdx-data-20220406105227.ndjson){ .md-button .md-button--primary } 

### Related resources

* [Exploring subdomains in the whole of gov.au](exploring-govau-subdomains.md)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}

--8<-- "web-archives-sponsor.md"