# voracious-etl
A hungry etl process for humans

This is a quick mockup of an idea.
Can you take a code first approach to ETL similar to how EntityFramework in .Net works?

Goals:
A user should be able to add a model to the list of models and have the app spin up a new table, detect relationships and handle CRUD through:
* an API
* a website that allows searching, editing, etc
* filewatchers for datafiles with good headers

Security should be handled at the model level in code.

Forked applications should be able to facade the main application for storage to present a coherent whole.

[![Build Status](https://travis-ci.org/mattkatz/voracious-etl.svg?branch=master)](https://travis-ci.org/mattkatz/voracious-etl)
