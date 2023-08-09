---
title: Trove API v3
description: Information about changes to the Trove API coming in version 3.
---

!!! info
    This is a temporary section of the the GLAM Workbench created to bring together information and examples relating to version 3 of the Trove API. It will probably disappear once the new version is officially released and I reorganise the Trove sections of the GLAM Workbench accordingly.

**Release 3 of the Trove API Version 3 beta** is now available for testing. See the [introductory notes](https://trove.nla.gov.au/sites/default/files/attachments/2023-06/Introducing%20Trove%20API%20v3%20-%20Release%203_0.pdf) for more details.

## Timeline

* March 2023: Trove API v3 beta (release 1)
* May 2023: Trove API v3 beta (release 2)
* June 2023: Trove API v3 beta (release 3)
* Mid 2023: Trove API v3 officially released
* Early 2024: Trove API v2 decommissioned

## Trove API Console

The [Trove API Console](https://troveconsole.herokuapp.com/) has been updated to add examples from v3 of the API. It provides many sample queries that you can run and modify without the need for an API key.

## Summary of breaking changes

!!! info
    This is a work in progress as I work my way through the API changes. Additions are very welcome.

This summary only includes **breaking changes** – the things you'll need to change in your code before v2 of the API is switched off in early 2024. For a full list of changes see the [introduction to the v3 API](hhttps://trove.nla.gov.au/sites/default/files/attachments/2023-07/Introducing%20Trove%20API%20v3%20-%20Release%203%20updated.pdf), and the [v3 technical guide](https://trove.nla.gov.au/about/create-something/using-api/v3/api-technical-guide).

The release notes don't mention the changes to the JSON responses. In general, the changes flatten the JSON responses by removing top-level wrappers that served no function. This means the way you access data within responses has changed. For example, assuming that you've saved the JSON response as a variable called `data`, to access the title of a newspaper article retrieved via the `/newspaper/[article id]` endpoint in version 2 you would use:

``` python
data["article"]["heading"]
```

While in version 3 you'd use:

``` python
data["heading"]
```

There are similar changes across all endpoints.

### All endpoints {: data-toc-omit }

- API keys will now **automatically expire** 12 months after activation! (There will be an option to renew.)
- change `v2` to `v3` in the endpoint url!
- `callback` parameter for JSONP removed, use CORS instead
- ~~default encoding now JSON not XML (I've been told this is a bug and release 3 will make XML the default again)~~ Default encoding is once again XML (same as API v2).

### `/result` endpoint {: data-toc-omit }

- `zone` parameter has been replaced with `category`, possible values are: all, newspaper, magazine, image, research, book,
diary, music, people, list; note that in most cases there is no one-to-one correspondence between zones and categories as the boundaries of what's included have changed, for example, the 'newspaper' category includes the contents of both the 'newspaper' and 'gazette' zones
- the handling of 'blank' searches has changed – ~~in version 2 you could use a " " space as a value for `q` allowing you to search for everything, this doesn't work in v3beta, however, using the unicode null value, `%00`, does seem to work~~ release 2 of the v3 beta made the `q` (query) parameter optional. This means blank searches are supported without any need for workarounds.
- the behaviour of the `include` parameter has changed – previously you could supply multiple values to `include` as a comma-separated string, now to specify mutiple values you have to include `include` multiple times (eg. instead of `&include=tags,comments` you need `&include=tags&include=comments`).
- JSON response format changes:
    - top-level `response` key removed
    - `zone` key changed to `category`
    - the meaning of the `name` parameter inside each `category` value has change – the old name value can be accessed via the `code` key, while `name` now returns the category's display name.
    - If you requested a single facet in version 2, it was returned as a JSON object. In version 3, facets are **always** returned as an array of objects no matter how many you request. So if you include the `facet=format` parameter in your request, the facet terms within each category will be in `category["facets"]["facet"][0]` rather than `category["facets"]["facet"]`. Compare the [v2 result](https://troveconsole.herokuapp.com/?url=https%3A%2F%2Fapi.trove.nla.gov.au%2Fv2%2Fresult%3Fq%3D+%26zone%3Dall%26encoding%3Djson%26facet%3Dformat%2Cdecade%26n%3D0) with the [v3 result](https://troveconsole.herokuapp.com/v3/?url=https%3A%2F%2Fapi.trove.nla.gov.au%2Fv3%2Fresult%3Fcategory%3Dall%26encoding%3Djson%26facet%3Dformat%26n%3D0).

### Newspapers and gazette records (both `/result` and  `/newspaper/[article id]`) {: data-toc-omit }

- urls of newspaper and gazette articles and pages returned by the API have changed to use NLA identifiers. In most cases this shouldn't break anything as they still go to the same place. However, if you've been extracting the numeric page identifier from the `trovePageUrl` then you might need to adjust your code. Previously the `trovePageUrl` value was of the form `https://trove.nla.gov.au/ndp/del/page/[PAGE ID]`, but in v3 it is `https://nla.gov.au/nla.news-page[PAGE ID]`.
- the structure of the `title` element has changed – in v2 the text version of a newspaper title was found in `record["title"]["value"]`, but in v3 this has changed to `record["title"]["title"]`

### List records (both `/result` and  `/list/[list id]`) {: data-toc-omit }

- in v2 the dates a list was created and updated were available at `record["created"]` and `record["lastupdated"]`, but in v3 both dates are under `record["date"]` so `record["date"]["created"]` and `record["date"]["lastupdated"]`.
- the values of `tagCount` and `commentCount` have moved – in v2 they were available at `record["tagCount"]` and `record["commentCount"]`, but in v3 they have moved down a level to `record["tagCount"]["value"]` and `record["commentCount"]["value"]`
  
### `/work/[work id]` endpoint {: data-toc-omit }

- JSON response format changes:
    - top-level `work` key removed

### `/newspaper/[article id]` endpoint {: data-toc-omit }

- JSON response format changes:
    - top-level `article` key removed
  
### `/newspaper/titles` endpoint {: data-toc-omit }

- JSON response format changes:
    - top-level `response` and `records` keys removed
  
### `/newspaper/titles/[title id]` endpoint {: data-toc-omit }

- JSON response format changes:
    - top-level `newspaper` key removed
  
### `/list/[list id]` endpoint {: data-toc-omit }

- JSON response format changes:
    - top-level `list` key removed – note too that in v2 `list` returned an array (even though there was only one value), in v3 there is just a single value, not an array; so instead of using `data["list"][0]["title"]` to get the title of a list, you'll need to use `data["title"]`.

### `contributor` endpoint {: data-toc-omit }

~~There are major changes here that aren't mentioned in the release notes. Previously a call to this endpoint without additional parameters just returned a long list of contributors. Now, you need to supply a `q` parameter to filter the results.~~

- ~~`q` parameter added and required – to do a blank search and get all contributors (ie the v2 behaviour), include the `q` parameter with no value, eg: `contributor?q=&encoding=json&reclevel=full`~~ Release 2 of the v3 API beta made the `q` parameter optional.
- JSON response format changes:
    - top-level `response` key removed

### `contributor/[NUC]` endpoint {: data-toc-omit }
 
- JSON response format changes:
    - top-level `contributor` key removed

### `magazine/titles/` endpoint {: data-toc-omit }

~~This endpoint was introduced in release 2 of the Trove API v3 beta, however, it's currently returning no results. I've been told this will be fixed in release 3.~~ Fixed in release 3.

