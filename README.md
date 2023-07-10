# AutoAPI

## What is AutoAPI ?

In simple words, AutoAPI takes your dataset, be it in CSV, excel, or SQL Data Export file format, and automatically creates APIs for accessing the data. You decide access control, pricing... and all the administrative actions.

## How do I know if I should use AutoAPI ?

* You have a dataset and you want to make it publically avaiable via APIs
* You want fine security control over which data is to be avaiable for access
* You want to set some pricing to monitize the data you're making accessable
* You don't want to go through the burden to setup APIs yourself
* If you check all or some of the boxes, then you can benefit from using AutoAPI

## Installation & Usage
```
1. Clone this project
> git clone git@github.com:deep-bhatt/auto-api.git
    OR
> git clone https://github.com/deep-bhatt/auto-api.git

2. You'll need to have Docker installed
> docker compose up -d

The above commands builds and starts containers.

3. Swagger API docs
> Visit http://127.0.0.1:8000/docs to see the API documentation to upload a CSV file

4. Fetch data using "GET /data" endpoint
example:
> GET http://127.0.0.1:8000/data?fields=id,name&name=foobarbaz&actor=cuzcox

- To specify which columns to fetch from rows, we use `fields` parameter
- To apply conditions, it's simply `<fieldName>=<value>` as query params
- Note that field names and their values are CASE-SENSITIVE
- Missing a feature? Have a look at the product roadmap
```

## Roadmap

* have a superuser token to manage datasource and APIs access
* security token for API access
* add support for limit & offset
* add support for less than, less than equal, greater than, and greater than equal comparasion operators
* add typing conversion support. ie. the returned fields must be of specified types.
* make a UI for easy access
* pricing feature
* custom database migrations system
