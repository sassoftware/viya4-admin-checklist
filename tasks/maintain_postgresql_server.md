![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Maintain SAS Infrastructure Data Server

<!--
SortString: 0680
Description: Perform routine maintenance on the SAS Infrastructure Data Server
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

For the most part, the underlying PostgreSQL server maintains itself but it is
a good practice to periodically review the storage demands PostgreSQL is
placing on your persistent volumes and carry out recommended cleanup.

Review the steps outlined in the documentation and perform and schedule
recommended tasks that are appropriate for your deployment.

Primary resource:

* [SAS Viya Platform Administration: SAS Infrastructure Data Server (Platform PostgreSQL)](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00000sasinfrdatasrv000admin.htm) [Doc]

See Also:

* [Manage content stored in PostgreSQL](manage_postgresql_content.md)

[Back to checklist](../checklist.md)