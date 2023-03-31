![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Inspect the Status of Scheduled Jobs

<!--
SortString: 0630
Description: Inspect the status of scheduled jobs
Tags: Regular,Legacy,Done
Topic: SAS Administration
Essential: -
Authors: David Stern,Michael Erickson
Frequency: Daily
-->
When: Regularly per housekeeping schedule

SAS Viya 4 does not currently have its own full-featured job scheduler, in the same way that SAS 9 was able to use Platform Suite for SAS. However, it does have a simple time-triggered scheduler for one-shot jobs, which is used for running backups, data loads, and custom jobs created in SAS Data Explorer, SAS Data Studio, and SAS Visual Analytics. See the section on [Jobs Flows in the SAS Viya Environment Manager User's Guide](https://documentation.sas.com/doc/en/sasadmincdc/default/evfun/n0b9cf8ru47gp6n1lvamxqwbr3by.htm) for more details.

Check the Jobs page in SAS Environment Manager regularly - e.g. daily - to determine which jobs are scheduled and whether they ran successfully or exited with another state (canceled, failed, timed out, and so on).

[Back to checklist](../checklist.md)