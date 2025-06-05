---
title: Trove web archive collections (Pandora)
description: This section includes information on finding, understanding, and using Pandora's collections of archived web pages.
repo_url: https://github.com/GLAM-Workbench/trove-web-archives
repo_name: trove-web-archives
page_type: repo
rocrate: "https://github.com/GLAM-Workbench/trove-web-archives/raw/master/ro-crate-metadata.json"
zenodo_concept_id: 11118559
---

{% include "trove-notice.md" %}

{{ git_latest_tag() }}

{{ page.meta.description}}

[Pandora](http://pandora.nla.gov.au/) has been selecting web sites and online resources for preservation since 1996. It has assembled a collection of more than 80,000 titles, organised into subjects and collections. The archived websites are now part of the Australian Web Archive (AWA), which combines the selected titles with broader domain harvests, and is searchable through Trove. However, Pandora's curated collections offer a useful entry point for researchers trying to find web sites relating to particular topics or events.

The [Web Archives](https://glam-workbench.net/web-archives/) section of the GLAM Workbench provides documentation, tools, and examples to help you work with data from a range of web archives, including the Australian Web Archive. The title urls obtained through Pandora can be used to obtain additional data from the AWA for analysis. For example:

- [Find all the archived versions of a web page using Timemaps](https://glam-workbench.net/web-archives/get-all-versions/)
- [Display changes in the text of an archived web page over time](https://glam-workbench.net/web-archives/display-changes-in-text/)
- [Harvesting collections of text from archived web pages](https://glam-workbench.net/web-archives/harvesting-text/)
- [Using screenshots to visualise change in a page over time](https://glam-workbench.net/web-archives/create-screenshots-over-time/)

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Notebooks

{% for nb in page.meta.notebooks %}

### [:material-notebook-outline: {{ nb.name }}]({{ nb.mainEntityOfPage["@id"].strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ nb.description.split("\n\n")[0] }}

{% endfor %}


## Datasets

{% for ds in page.meta.datasets|sort(attribute="position") %}

### [:material-database-outline: {{ ds.name }}]({{ ds.url.strip("/").split("/")[-1] }}.md) {: data-toc-omit }

{{ ds.description }}

{% endfor %}

### [:material-database-outline: Pandora subject hierarchy](pandora-subject-hierarchy.md) {: data-toc-omit }

A single-page view of Pandora's complete subject hierarchy.

{% include "nb-run-info.md" %}


## Contributors

{{ repo_contributors() }}

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}

{% endif %}