
{{ page.meta.rocrate_description|htmlify }}

{% if page.meta.distribution %}
[Download complete dataset as zip]({{ page.meta.distribution }}){ .md-button .md-button--primary }
{%- endif %} {%- if page.meta.datasette %}
[Explore in Datasette]({{datasette.url}}){ .md-button .md-button--info }
{% endif %}

## Files

{% for dataset in page.meta.datasets %}
### {{ dataset.name }}

{% if dataset["encodingFormat"] %}
{% set format = dataset["encodingFormat"] %}
{% elif "." in dataset["@id"] %}
{% set format = dataset["@id"].split(".")[-1] %}
{% else %}
{% set format = "directory" %}
{% endif %}

<table>
<tbody>
<tr><td><b>date harvested</b></td><td>{{ dataset["dateModified"] }}</td></tr>
<tr><td><b>format</b></td><td>{{format}}</td></tr>
{%- if dataset["contentSize"] %}<tr><td><b>file size</b></td><td>{{ dataset["contentSize"] | filesizeformat}}</td></tr>{% endif %}
{%- if format == "text/csv"  %}<tr><td><b>number of rows</b></td><td>{{ "{:,}".format(dataset["size"])}}</td></tr>{% endif %}
{% if format == "directory" %}<tr><td><b>number of files</b></td><td>{{ "{:,}".format(dataset["size"])}}</td></tr>{% endif %}
{%- if dataset.license %}<tr><td><b>license</b></td><td><a href="{{dataset.license.url}}">{{ dataset.license.name }}</a></td></tr>{% endif %}
</tbody>
</table>

{% if dataset.description and dataset.description != page.meta.rocrate_description %}{{ dataset.description|htmlify }}{% endif %}

[Download{% if "github" in dataset.url %} from GitHub{% endif %}]({{ dataset.url }}){ .md-button .md-button--primary }

{% if dataset.columns %}
#### Columns
| name | type | description |
|------|------|-------------|
{%- for column in dataset.columns %}
| `{{ column.name }}` | {{column.type}} | {{column.description}} |
{%- endfor %}

{% endif %}

{% endfor %}

{% if page.meta.action %}
## Context of creation

<table>
<tbody>
<tr><td><b>date harvested</b></td><td>{{ page.meta.action.endDate }}</td></tr>
{% if page.meta.action.nb.mainEntityOfPage %}<tr><td><b>notebook</b></td><td><a href="{{page.meta.action.nb.mainEntityOfPage['@id']}}">{{ page.meta.action.nb.name }}</a></td></tr>{% endif %}
{% if page.meta.action.query %}<tr><td><b>query</b></td><td><code>{{ page.meta.action.query }}</code></td></tr>{% endif %}

</tbody>
</table>
{% endif %}

{% if page.meta.examples %}

## Examples of use

{% for example in page.meta.examples %}

{% if not example.url.startswith("https://glam-workbench.net/datasette-lite/") %}
- [{{example.name}}]({{example.url}})
{% endif %}
{% endfor %}
{% endif %}


--8<-- "help.md"

{% if page.meta.zenodo_concept_id %}

## Cite as

{{ zenodo_citation() }}

{% endif %}