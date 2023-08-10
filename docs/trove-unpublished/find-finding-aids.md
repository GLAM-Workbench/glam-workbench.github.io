---
title: Find urls of digitised finding aids
description: This notebook uses the Trove API to harvest urls of NLA digitised finding aids from a search in the `collection` zone.
repo_url: https://github.com/GLAM-Workbench/trove-unpublished
repo_name: trove-unpublished
zenodo_concept_id: 3549343
notebook: find-finding-aids.ipynb
tags:
  - finding aids
  - manuscripts
  - harvest
hide:
  - toc
---

The 'Diaries, Letters, and Archives' category of Trove (aka the 'collection' zone using the Trove API) includes a mix of digitised items, digitised finding aids, and metadata records for an assortment of collections and series. Unfortunately, there are no facets to help separate the different types of content, and so the finding aids can get a bit swamped. For example, you might think that searching for `findingaid "nla.obj"` would help identify the NLA's digitised finding aids, but this search returns 153,345 results, most of which are items within finding aids, rather than the finding aids themselves. I've yet to find a search in Trove that can reliably isolate the digitised finding aids. ([Searching for 'finding aid'](https://catalogue.nla.gov.au/Search/Home?lookfor=findingaid&type=all&limit%5B%5D=&submit=Find&limit%5B%5D=format%3AManuscript) in the manuscripts section of the NLA catalogue gets close.) Nor can I find a complete list of finding aids elsewhere on the NLA site. So how can we find the finding aids?

{{ description }}

[Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

### Other options

* [Run live on Binder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}) (no authentication required)
* [Download from GitHub](https://github.com/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})
* [View using NBViewer](https://nbviewer.jupyter.org/github/GLAM-Workbench/{{repo_name}}/blob/master/{{notebook}})

### Related resources

* [NLA digitised finding aids: list of urls](finding-aids-urls.md) (dataset)

### Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

## Cite as

{{ zenodo_citation() }}