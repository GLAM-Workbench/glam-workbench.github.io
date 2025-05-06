---
title: Trove music, sound, and oral histories
description: Trove's 'music' zone includes music, oral history interviews, and radio programs. You can access metadata from the music zone through the Trove API.
repo_url: https://github.com/GLAM-Workbench/trove-music
repo_name: trove-music
zenodo_concept_id: 7659567
---

{{ git_latest_tag() }}

Trove's 'music' category includes music, oral history interviews, and radio programs. You can access metadata from the music category through the Trove API.

See below for information on [running these notebooks](#run-these-notebooks) in a live computing environment. Or just take them for a spin using Binder.

[![ARDC Binder](../images/explore-live-on-ardc-binder.svg)](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)
[![Binder](../images/Explore live on-Binder-579ACA.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=lab/tree/index.ipynb)

## Tips, tools, and examples

### [:material-notebook-outline: Harvest oral histories metadata](harvest-oral-histories.md) {: data-toc-omit }
Harvests metadata describing the NLA's oral history collection from Trove and saves the results as a CSV file.

### [:material-notebook-outline: Save a list of oral history collections and projects](save-series.md) {: data-toc-omit }
Extracts a list of series from metadata describing oral histories held by the NLA and described in Trove.

### [:material-notebook-outline: Download summaries and transcripts from oral histories](download-transcripts.md) {: data-toc-omit }
Downloads all the available transcripts and summaries from digitised oral histories available in Trove.

### [:material-notebook-outline: Harvest ABC Radio National records from Trove](harvest-abcrn.md) {: data-toc-omit }
Trove harvests details of programs and segments broadcast on ABC Radio National. You can find them by searching for nuc:"ABC:RN" in the Music & Audio category. The records include basic metadata such as titles, dates, and contributors, but not full transcripts or audio. This notebook harvests, cleans, and saves all the available Radio National data from Trove.

### [:material-notebook-outline: Exploring ABC Radio National metadata](explore-abcrn-data.md) {: data-toc-omit }
This notebook shows a few ways you can start to explore the ABC Radio National metadata harvested by the notebook above.

## Data

### [:material-folder-outline: NLA oral histories metadata](trove-oral-histories.md) {: data-toc-omit }

*Harvested: December 2023*

### [:material-folder-outline: List of NLA oral history collections and projects](trove-oral-history-series.md) {: data-toc-omit }

*Harvested: December 2023*

### [:material-folder-outline: ABC Radio National programs](abcrn-data.md) {: data-toc-omit }

*Harvested: December 2023*

## See also

### [:material-book-open-outline: Oral histories in the *Trove Data Guide*](https://tdg.glam-workbench.net/other-digitised-resources/oral-histories/index.html) {: data-toc-omit }

{% include "nb-run-info.md" %}

<!-- END RUN INFO -->

## Contributors

{{ repo_contributors() }}

## Cite as

{{ zenodo_citation() }}