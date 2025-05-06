---
title: Save a collection of digitised images as an IIIF manifest
description: This notebook harvests metadata describing the contents of a digitised collection in Trove and saves it as an IIIF manifest. This makes it possible to work with data from Trove in a variety of IIIF-compliant tools.
repo_url: https://github.com/GLAM-Workbench/trove-images
repo_name: trove-images
notebook: save-image-collection-iiif.ipynb
tags:
  - images
  - IIIF
hide:
  - toc
rocrate: "https://github.com/GLAM-Workbench/trove-images/raw/master/ro-crate-metadata.json"
page_type: notebook
---


{{ page.meta.rocrate_description|htmlify }}


{{ nb_preview() }}

## Using this notebook

=== "ARDC Binder"

    To run this notebook using the ARDC Binder service you'll need to log in using an account from an Australian university or research organisation. If you don't have an account, try [MyBinder](#__tabbed_1_2) instead.

    [Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

=== "MyBinder"

    The MyBinder service doesn't require any authentication, but it can be slow to start and will sometimes fail when busy. If you have a login at an Australian university, you'll probably get better results with [ARDC Binder](#__tabbed_1_1).

    [Run live on MyBinder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button .md-button--primary }

=== "Other options"

    Binder is great for experimentation and quick tasks, but for some projects you might need a dedicated, persistent environment in which to work. There's information on other options in the [run these notebooks](../#run-these-notebooks) section.

## Examples


<iframe src="https://uv-v3.netlify.app/uv/uv.html#?manifest=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-140670968-v3-manifest.json&c=0&m=0&s=0&cv=0" width="100%" height="600" allowfullscreen frameborder="0"></iframe>

| collection | manifest | UV3 | Mirador |
|----|----|----|----|
| [B.A.N.Z. Antarctic Research Expedition photographs](https://nla.gov.au/nla.obj-141170265) | [nla.obj-141170265-v3-manifest.json](https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-141170265-v3-manifest.json) | [view in UV3](https://uv-v3.netlify.app/#?c=&m=&s=&cv=54&manifest=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-141170265-v3-manifest.json) | [view in Mirador](https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-141170265-v3-manifest.json) |
| [The Papers of Sir Edmund Barton](https://nla.gov.au/nla.obj-224441684) | [nla.obj-224441684-v3-manifest.json](https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441684-v3-manifest.json) | [view in UV3](https://uv-v3.netlify.app/#?c=&m=&s=&cv=54&manifest=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441684-v3-manifest.json) | [view in Mirador](https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441684-v3-manifest.json) |
| [Papers relating to the Federation Campaign (a single series from the Barton papers)](https://nla.gov.au/nla.obj-224441858) | [nla.obj-224441858-v3-manifest.json](https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441858-v3-manifest.json) | [view in UV3](https://uv-v3.netlify.app/#?c=&m=&s=&cv=54&manifest=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441858-v3-manifest.json) | [view in Mirador](https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-224441858-v3-manifest.json) |
| [Postcard portraits of actresses, and of Australian towns, 1900s](https://nla.gov.au/nla.obj-140670968) | [nla.obj-224441858-v3-manifest.json](https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-140670968-v3-manifest.json) | [view in UV3](https://uv-v3.netlify.app/#?c=&m=&s=&cv=54&manifest=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-140670968-v3-manifest.json) | [view in Mirador](https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/wragge/iiif-tests/main/nla.obj-140670968-v3-manifest.json) |


{% if page.meta.datasets %}

## Related datasets

{% for ds in page.meta.datasets %}

- [{{ ds.name }}]({{ ds.url.strip("/").split("/")[-1] }}.md)

{% endfor %}

{% endif %}

{% if page.meta.example_image %}
<figure markdown="span" style="float:right;">
  ![Image title](../images/{{page.meta.example_image.file}}){ width="300" }
  <figcaption markdown="span" >{{page.meta.example_image.caption}}</figcaption>
</figure>
{% endif %}

{% if page.meta.nb.workExample %}

## Examples of use

{% for eg in page.meta.nb.workExample %}

- [{{ eg.name }}]({{ eg.url }})

{% endfor %}

{% endif %}

## Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}

{% endif %}