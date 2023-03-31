![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Manage content stored in PostgreSQL

<!--
SortString: 0670
Description: Manage content stored in PostgresQL
Tags: New,Regular,Done
Topic: PostgreSQL
Essential: -
Authors: Scott McCauley
Frequency: Monthly
-->
When: Ongoing

The SAS Infrastructure Data Server stores SAS Viya platform user content, such
as reports, authorization rules, selected source definitions, attachments, and
user preferences. SAS Viya platform uses High Availability (HA) PostgreSQL for
SAS Infrastructure Data Server.

In addition to predictable SAS Viya content, over time, additional content may
accumulate in PostgreSQL storage including, but not limited to

* Random files that users upload from SAS Drive
* Images and other media files
* Logs from scheduled jobs

As an administrator you may not be comfortable deleting content owned by others
but you should at least review the user content stored in PostgreSQL and work
with your user community to remove files that are no longer needed.

Primary resources:

* [Where are my Viya files?](https://blogs.sas.com/content/sgf/2019/04/04/where-are-my-viya-files/) [Blog]
* [Related pyviyatools](https://github.com/sassoftware/pyviyatools) [Tools]
  * [listfiles.py](https://github.com/sassoftware/pyviyatools/blob/master/listfiles.py) for inventorying content
  * [archivefiles.py](https://github.com/sassoftware/pyviyatools/blob/master/archivefiles.py) for extracting or deleting content
  * [listcontent.py](https://github.com/sassoftware/pyviyatools/blob/master/listcontent.py) for inventorying content from a specific folder

See Also:

* [Maintain SAS Viya Infrastructure Data Server](maintain_postgresql_server.md)

[Back to checklist](../checklist.md)