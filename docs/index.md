---
repo_url: https://github.com/GLAM-Workbench
repo_name: GLAM-Workbench
---

# Welcome to the wonderful world of GLAM data!

Here you’ll find a collection of tools, tutorials, examples, and hacks to help you work with data from galleries, libraries, archives, and museums (the GLAM sector). The primary focus is Australia and New Zealand, but new collections are being added all the time. Let me know if there’s some GLAM data you’d like me to explore – [suggestions](/suggest-a-topic/) are always welcome!

Here’s a brief explanation of what I’m trying to do, courtesy of the 2018 National Digital Forum in New Zealand.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ONnxd-1KJFI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There’s [more presentations](/presentations/) here.

## What is GLAM data?

When we talk about GLAM data we’re usually referring to the collections held by cultural institutions &ndash; books, manuscripts, photographs, objects, and much more. We’re used to exploring these collections through online search interfaces or finding aids, but sometimes we want to do more &ndash; instead of a list of search results on a web page, we want access to the underlying collection data for analysis, enrichment, or visualisation. We want [collections as data](https://collectionsasdata.github.io/).

This GLAM Workbench shows you how to create your own research datasets from a variety of GLAM collections. In some cases cultural institutions provide direct access to collection data through APIs (Application Programming Interfaces) or data downloads. In other cases we have to find ways of extracting data from web interfaces &ndash; a process known as screen-scraping. Here you’ll find examples of all these approaches, as well as links to a number of pre-harvested datasets.

## What can I do with GLAM data?

Ask different types of questions!

* Shift scales
* Find patterns
* Extract features
* Make connections

This GLAM Workbench demonstrates a variety of tools and techniques that you can use to explore your data.

## Do I need to be able to code?

No, you can use the Jupyter notebooks within the workbench without any coding experience &ndash; just edit and click where indicated. But every time you do edit one of the notebooks, you *are* coding. The notebooks provide an opportunity to gain confidence and experiment. They might not turn you into a coder, but they will show you how to do useful things with code.

You can have a go right and here and now. The code below retrieves data from the [National Museum of Australia API](/nma/). Look for the line that says `keyword = 'stone'` and change 'stone' to something else, like 'koala', or 'Phar Lap'. Then click on the **run** button. Try as many different keywords as you like.

<pre data-executable>
import requests
keyword = 'stone' # <-- EDIT ME! (But leave the quotes)
url = 'https://data.nma.gov.au/object?limit=1&text='
response = requests.get(url + keyword)
results = response.json()
total = results['meta']['results']
print(f'There are {total} {keyword}s in the NMA!')
</pre>

Congratulations, you're coding! If you can click, edit, and hit a few keys, you can use Jupyter notebooks.

Behind the scenes, this code cell is loading up a customised computing environment on [Binder](https://mybinder.org/), sending the code off to run, and then displaying the result. It's very similar to the way that Jupyter notebooks run, in fact, you can explore this example further in the notebook linked from the [getting started](/getting-started/) page.

## Other GLAM related notebooks

* [GLAM Jupyter Notebooks](http://data.cervantesvirtual.com/blog/notebooks/), Biblioteca Virtual Miguel de Cervantes Labs
* [Awesome Jupyter GLAM](https://github.com/LibraryCarpentry/awesome-jupyter-glam), Chris Erdmann
* [Getting started with ODate](https://o-date.github.io/support/notebooks-toc/), Shawn Graham
* [Jupyter notebooks for digital humanities](https://github.com/quinnanya/dh-jupyter), Quinn Dombrowski
