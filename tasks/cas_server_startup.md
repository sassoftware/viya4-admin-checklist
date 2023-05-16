![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure CAS server startup to load data

<!--
SortString: 0650
Description: Configure CAS server startup to load data
Tags: New,Regular,Done
Topic: CAS
Essential: -
Authors: Scott McCauley
Frequency: Monthly
-->
When: Update as needed, and review monthly

When a CAS server stops or restarts, all of the in-memory CAS tables are unloaded. A SAS Visual Analytics report will usually load any CAS tables it requires automatically but there may be situations, such as reports relying on extremely large CAS tables, reports relying on tables which the viewer may not have (CAS [promote or limitedpromote](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthzcas/n1bf0cwn6ae85gn1b64x2j0czu24.htm#n0tn6r1fc41vohn1bycmltsjhw6e)) permission to load, or CAS tables needed for ad-hoc programming or other analytical purposes, where you may want to *pre-load* a number of CAS tables for a better user experience.

In cases where you need to pre-load CAS tables, you should configure the CAS server startup to explicitly load data whenever it starts.  The data loading instructions must be written in the Lua language. You can base your needs on this example of loading a .CSV file from a path-based caslib if you are not familiar with Lua.

```sh
---- Load CAS table
---- s is a reference to the active CAS session
s:table_loadTable{caslib="name-of-caslib",
                  casOut={caslib="name-of-caslib",replication=0.0},
                  path="myHuge.csv",
                  promote=true
                 }
```

Primary resources:

* [Modifying Server Startup Configuration in SAS Viya](https://communities.sas.com/t5/SAS-Communities-Library/Modifying-Server-Startup-Configuration-in-SAS-Viya/ta-p/726824) [Blog]
* [SAS Viya Platform Administration: SAS Cloud Analytic Services - Standard Configuration Files](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calserverscas/n05000viyaservers000000admin.htm#n05025viyaservers000000admin) [Doc]
* [SAS Viya Platform Administration: SAS Cloud Analytic Services: Reference](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calserverscas/n08000viyaservers000000admin.htm#n08172viyaservers000000admin) [Doc]

See Also:

You can also rely on CAS state management jobs to load CAS tables if you have a bit of flexibility for when the tables are loaded.  CAS state management jobs run on a schedule (typically, every 15 minutes) so there is a high likelihood that some period of time will elapse between the time your CAS server starts and when the job next executes.

* [SAS Viya Platform Administration: CAS Table State Management](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caldatamgmtcas/n150v9svjp42ron1hn9r496xj49m.htm) [Doc]

[Back to checklist](../checklist.md)