![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure audit record archival

<!--
SortString: 0220
Description: Configure and schedule the archiving of SAS Viya audit records.
Tags: Initial,New,Done
Topic: Observability
Essential: -
Authors: Ajmal Farzam
-->
When: Initial, then run regularly per housekeeping schedule

Auditing in SAS Viya is enabled by default at deployment time. SAS Viya’s Audit service tracks system usage through audit records, which are stored in the SAS Infrastructure Data Server and accessible to administrators.

Every seven days ([configurable](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/p0txfp3picp59on1ua27dsqcpjwv.htm?fromDefault=#n03ex24fl4dr07n1hy3qqmgrvl2v) [Doc]), the Audit service transfers records from the audit database into the audit archive; a location which must be accessible to the *sas-audit* pod. If no location is specified, those records are deleted. After transfers, the exported records are also removed from the audit database.

If you wish to keep archived audit records, a persistent volume must be attached to the *sas-audit* pod and used as the archive location. The `sas.audit.archive.process` and `sas.audit.archive.system` configuration instances control the behaviour of the archive process, such as the archive destination, the conditions that must be met before the archive runs and the option to enable and disable archiving altogether.

See also:

* [Enable job to purge archived audit records](./purge_archived_audit_records.md)  [Task]
* [How to configure archiving of audit records](https://communities.sas.com/t5/SAS-Communities-Library/How-to-configure-archiving-of-audit-records-in-SAS-Viya/ta-p/800583) [Blog]
* [Audit Archive](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/p1m6yn3dntt3jmn1xu1t611hnt2p.htm#p0irn8zabme4eun1qs9dcezy5cla) [Doc]
* [Configure the Audit Archive](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/p0txfp3picp59on1ua27dsqcpjwv.htm#n1g99yn3s6mk65n14y3i2z3df87a) [Doc]


[Back to checklist](../checklist.md)