# OLX Phone Number Scraper

Scrapes phone numbers from OLX listings.

## Usage

**NOTE**: rewrite this when final version is done, this here is just to guide
the design of the program, to make it intuitive.

```
olxscrape <url_of_listings> <page_limit>* <phone_number_limit>* <output_file_name>

The tools should write a phone number to the file as soon as it's scraped, so that
it can be safely stopped with Ctrl^C at any time.
```

```
join <file_1> ... <file_n> <output_file_name>

Joins two or more files into a single one, removing duplicates.

```

```
prefix_phone <input_file_name> <prefix> <output_file_name>

Prefixes the given string to all of the phone nubmers in the list. Useful if you
want to prefix all with a country code.
```

Features marked with `*` might only be considered for beyond-base-version of the
tool.

## About

This tool can be easily altered to scrap e-mails and any other useful information
as well. This was written as a need for a specific project and is only
designed to support this functionality. It's a result of reverse-engineering
necessary to fulfill the purpose of scraping phone numbers from listings,
given a url of to a list of those listings. Some command-line tools are included.

A **minimal** test set is included. You can use this as a basis for a tool
with similar purpose.

I have a lack of time at the moment and quickly hacked this in. When reading the
code, please keep this in mind.
