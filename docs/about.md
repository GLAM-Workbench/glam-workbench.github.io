---
title: About the GLAM Workbench
---

## What is the GLAM Workbench?

The GLAM Workbench is a collection of Jupyter notebooks to help you explore and use data from GLAM institutions (that's galleries, libraries, archives, and museums). It includes tools, tutorials, examples, hacks, and even some pre-harvested datasets. I'm a historian, so the GLAM Workbench is mostly aimed at researchers in the humanities, but there's plenty to interest others as well. Here's a quick intro...

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/631475562?h=6b2e2b5636" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## How do I get started?

Head over to the [getting started](https://glam-workbench.net/getting-started/) section where I suggest some first steps, and provide a bit of information on finding your way around the GLAM Workbench. If you don't like reading the documentation, just dive in and explore – look for examples or datasets that interest you, and think about the possibilities. Click on any of the 'Run live' links to fire up a notebook and see what happens!

## Where can I get help?

In the help section of the GLAM Workbench you'll find hints on [getting started](https://glam-workbench.net/getting-started/), information on [running Jupyter notebooks](https://glam-workbench.net/using-binder/), and a series of [help videos](https://www.youtube.com/playlist?list=PLAclcciEeCD2z2BWQ2r3xD_Q8c05HppfP) aimed at new users.

If you find that something's not working, either ping [me on Twitter](https://twitter.com/wragge) or add the problem to my [list of issues on GitHub](https://github.com/GLAM-Workbench/glam-workbench.github.io/issues). You can also add suggestions for new notebooks, institutions, or datasets.

If you have a question, head over to the [GLAM Workbench section of OzGLAM help](https://ozglam.chat/c/glam-workbench/8).

If you're after a more in-depth discussion, [book in to see me](https://calendly.com/timsherratt/30minchat) during office hours.

## Can I reuse, modify, and share the notebooks? Can I use the GLAM Workbench in my workshop?

YES! All the notebooks and documentation in the GLAM Workbench are openly licensed to encourage reuse. **So please take them, change them, share them!**

Some of the pre-harvested datasets available through the GLAM Workbench will come with their own copyright or licensing conditions. I've noted this where I can. In many cases the conditions aren't clear, so depending on your planned uses, you might want to go back to the source institution and check.

## How is the GLAM Workbench funded?

The GLAM Workbench is mostly self-funded. It’s a passion project that brings together a lot of work I’ve been doing over the last 14 years to open GLAM collections to new research uses. But that doesn’t mean I don’t have help. 

Inevitably, there are overlaps between the GLAM Workbench and the one day a week I’m employed by the Centre for Creative and Cultural Research at the University of Canberra. Indeed, our latest [ARC Linkage grant](https://dataportal.arc.gov.au/NCGP/Web/Grant/Grant/LP200301446) specifically includes the development of resources for the GLAM Workbench in its outputs. I also do some paid work that ends up in the GLAM Workbench, such as the [Sydney Stock Exchange project](https://glam-workbench.net/anu-archives/#sydney-stock-exchange-records) I've been working on with the ANU Archives.

I’ve also received a couple of grants and contracts over the last few years that have supported particular areas of the GLAM Workbench. The International Internet Preservation Consortium (IIPC) contributed US$3,500 [towards the development](https://netpreserve.org/projects/jupyter-notebooks-for-historians/) of the Web Archives section, as part of its [Discretionary Funding program](https://netpreserve.org/projects/funding/). In 2019 the HASS DeVL project contracted me ($12,000 over 6 months) to develop Jupyter notebooks using Trove and other GLAM sources. The HASS DeVL project no longer exists, but the notebooks I developed are still available and working – for example, the [GLAM CSV Explorer](https://glam-workbench.net/csv-explorer/), and many of the notebooks in the the [Trove Journals](https://glam-workbench.net/trove-journals/) section.

I’m particularly grateful for the support of my [GitHub Sponsors](https://glam-workbench.net/supporters/) (and those who previously supported me through Patreon). The amount I receive varies, but at the moment it’s somewhere between AU$2-3,000 per annum. This makes a big contribution towards my cloud hosting costs, enabling the GLAM Workbench, and a range of related digital tools and projects, to keep chugging along. More than money though, the fact that people think this work is worth supporting really helps keep my motivation up!

## Is the GLAM Workbench sustainable?

Yes, I think so. To me, a sustainable project is one that is open to the future. My sustainability plan for the GLAM Workbench isn't based on having an institutional host or a steady stream of funding. It's based on the following ideas:

* **Make everything open** – If I go under a bus tomorrow, all of the notebooks will still be openly-licensed and accessible. If they are of use, people will fork the repositories, update the code, and share the results. If they're not, they'll fade gently into irrelevance.
* **Small parts, loosly coupled** – There is no underlying platform that needs to be maintained. Jupyter notebooks are just JSON files, structured according to an agreed standard, and can be deployed in a wide variety of environments. The GLAM Workbench uses existing services to run its notebooks, integrating with tools and platforms like Binder, Reclaim Cloud, Nectar, and Docker. But it's not dependent on any of them. If a particular service disappears, something else can be swapped in.
* **Automate the boring stuff** – I'm increasingly making use of scripts and GitHub actions to do routine maintenance tasks like building Docker images, managing versions, and updating documentation. I hope to add more automated testing in the future. I forget things, so having tasks like these set up and running makes it easier for me to focus on development.
* **Promote use and welcome collaboration** – It's obvious, but important. The more a project is used and shared, the more likely it is to be maintained and developed. Outreach is hard, but crucial. One of my priorities at the moment is making it easier for others to contribute resources to the GLAM Workbench.

The GLAM Workbench is itself an experiment, but it's already outlasted some well-funded research infrastructure projects. It won't live on forever in it's current form, but that doesn't mean it can't have a long-term impact. 

