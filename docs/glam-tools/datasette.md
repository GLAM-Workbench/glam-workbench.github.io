---
title: Use Datasette-Lite to share a CSV file as a searchable, online database
---

This page generates a url that will publish a CSV file as a fully-searchable, online database using [Datasette-Lite](https://github.com/simonw/datasette-lite). All you need is the url of a CSV file  saved in a public GitHub repository. [Additional documentation](#documentation) is provided below.

## Quick start

Just copy and paste the GitHub url that points to your CSV file.

<input id="github-url" type="text" class="md-input md-input--stretch" placeholder="GitHub CSV url">

<button id="create-url" class="md-button md-button--primary">Create url</button> <button id="clear-all" class="md-button">Clear</button>

<div id="datasette-url"></div>

## Optional settings

### Add full text index

Provide a comma-separated list of columns that you want to be added to the database's full-text index. For example, `title,description,creator` would index the `title`, `description`, and `creator` columns.

<input id="fts-cols" type="text" class="md-input md-input--stretch" placeholder="index these full-text columns">

### Drop unwanted columns

Provide a comma-separated list of columns that you don't want to be displayed in Datasette. For example, `old_id,internal_note` would drop the `old_id`, and `internal_note` columns from the table.

<input id="drop-cols" type="text" class="md-input md-input--stretch" placeholder="drop these columns">

### Add a link to more information

Insert a url to a page with more infomation about your dataset.

<input id="about-url" type="text" class="md-input md-input--stretch" placeholder="link for more information">

## Documentation

Often researchers compile data in spreadsheets. But how do you share this data with others in a form they can easily explore? [Datasette](https://datasette.io/) is a tool that helps you publish your data as an interactive website. There's a few different varieties of Datasette, but [Datasette-Lite](https://github.com/simonw/datasette-lite) is probably the easiest, as you don't need to install any software. Datasette-Lite runs completely within your web browser, converting your data into into a searchable database on demand.

I'm using Datasette-Lite throughout the GLAM Workbench. For example, try clicking the **Explore in Datasette** buttons on any of these pages:

- [digitised periodicals in Trove](https://glam-workbench.net/trove-journals/periodicals-data-api/)
- [editorial cartoons from the Bulletin](https://glam-workbench.net/trove-journals/bulletin-cartoons-collection/)
- [oral histories in Trove](https://glam-workbench.net/trove-music/trove-oral-histories/)

The buttons are simply links that point my [customised version of Datasette-Lite](https://github.com/GLAM-Workbench/datasette-lite) to a specific dataset. To explore your dataset in Datasette-Lite, all you need is a url that tells Datasette-Lite what to load. This tool helps you generate those urls.

### Save your dataset as a CSV file in GitHub

1. Save your spreadsheet as a CSV file (if it's not already in CSV format)
2. [Create a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (it's free) and login
3. [Create a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories#create-a-repository)
4. From the main page of your new repository, Click on the 'Add file' button and select 'Upload file'.
5. Select your CSV data file (or drag it to your browser) to upload it.
6. Once it has uploaded, click on the green 'Commit changes' button to save the file to your repository.

### Generate a url to load the CSV in Datasette

1. Click on the uploaded data file in your GiHub repository.
2. Copy the url of the data file from your browser's location bar.
3. Paste the url into GitHub url box above.
4. Click on the **Create url** button and the new url will appear.
5. Click on the url to load Datasette, or right click and select 'Copy link' to share your dataset with others.

### Optional settings

#### Index text columns

The GLAM Workbench version of Datasette-Lite includes an option to index selected full-text columns. When you add a full-text index, Datasette will automatically display a keyword search box. For example, you might have columns for `title` and `description` that contain long full-text values. If you  index these columns you'll be able to search them both simply by entering words or phrases in the search box.

To tell Datasette which columns to index, enter the column names, separated by commas, in [Add full text index](#add-full-text-index) box. For example, to index the `title` and `description` columns, you'd enter `title.description`. Click the **Create url** button when you've finished to update the Datasette-Lite url.

#### Hide unwanted columns

There might be columns in your CSV dataset that you don't want to display in Datasette. You can tell Datasette to hide them by entering the column names, separated by commas, in the [Drop unwanted columns](#drop-unwanted-columns) box. Click the **Create url** button when you've finished to update the Datasette-Lite url.

#### Add a link to more information

If you have a webpage that provides more information about your dataset, you can add a link to it from Datasette. Just paste the url into the [Add a link to more information](#add-a-link-to-more-information) box. Click the **Create url** button when you've finished to update the Datasette-Lite url.

### Limitations and alternatives

This tool makes it easy to share single CSV files as searchable databases. But if your CSV has millions of rows it'll probably make your web browser unhappy if you try and load it in Datasette-Lite. Instead you can make use of Datasette's 'publish' option to push your data to a dedicated Datasette instance running on a cloud server. You can also customise your instance by changing the theme or using canned queries.

For example, the [GLAM Name Index Search](https://glam-workbench.net/name-search/) contains more than 10 millions rows of data from multiple datasets, all aggregated through a single search interface. The [Tasmanian Post Office Directories](https://glam-workbench.net/libraries-tasmania/tasmanian-post-office-directories/) provides full-text search across 48 digitised volumes and has a heavily customised interface that displays page images as well as the OCRd content. Both of these Datasette instances are hosted on Google Cloudrun.

Similarly, the method described here is designed to work with single CSV files. If you have multiple, interconnected tables you'll probably want to generate your own SQLite database to use with Datasette. There's an example of how you can do this in the [Enrich the list of periodicals from the Trove API](https://glam-workbench.net/trove-journals/periodicals-enrich-for-datasette/) notebook.

<script src="../../scripts/datasette-script.js"></src>
