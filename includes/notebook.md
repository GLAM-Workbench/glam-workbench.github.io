{{ page.meta.rocrate_description|htmlify }}

{{ nb_preview() }}

## Using this notebook

{% if page.meta.interface == "voila" %}This notebook is designed to run as a web app using Voilá, hiding all the code. If you want to see the code behind the app, click on the non-Voilá button.{% endif %}

{% if page.meta.jlite_repo %}
=== "Jupyter Lite"

    Use Jupyter Lite to run this notebook in your browser without the need for additional cloud services.
    
    [Run live using Jupyter Lite](https://glam-workbench.net/{{page.meta.jlite_repo}}/lab/index.html?path={{notebook}}){ .md-button .md-button--primary }
    
{% endif %}
=== "ARDC Binder"

    To run this notebook using the ARDC Binder service you'll need to log in using an account from an Australian university or research organisation. If you don't have an account, try [MyBinder](#__tabbed_1_2) instead.

    {% if page.meta.interface == "voila" %}[Run live on ARDC Binder using Voilá](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=voila/render/{{notebook}}){ .md-button .md-button--primary }{% endif %} [Run live on ARDC Binder](https://binderhub.rc.nectar.org.au/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button {% if page.meta.interface != "voila" %}.md-button--primary{% endif%} }

=== "MyBinder"

    The MyBinder service doesn't require any authentication, but it can be slow to start and will sometimes fail when busy. If you have a login at an Australian university, you'll probably get better results with [ARDC Binder](#__tabbed_1_1).

    {% if page.meta.interface == "voila" %}[Run live on MyBinder using Voilá](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=voila/render/{{notebook}}){ .md-button .md-button--primary }{% endif %} [Run live on MyBinder](https://mybinder.org/v2/gh/GLAM-Workbench/{{repo_name}}/HEAD?urlpath=/lab/tree/{{notebook}}){ .md-button {% if page.meta.interface != "voila" %}.md-button--primary{% endif%} }

=== "Other options"

    Binder is great for experimentation and quick tasks, but for some projects you might need a dedicated, persistent environment in which to work. There's information on other options in the [run these notebooks](../#run-these-notebooks) section.


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

{% if page.meta.videos %}
## Help videos

{% for video in page.meta.videos %}
<p><iframe width="560" height="315" loading="lazy" src="https://www.youtube.com/embed/{{video}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

{% endfor %}

{% endif %}

## Additional documentation

* [Run these notebooks](../#run-these-notebooks)

--8<-- "help.md"

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}

{% endif %}