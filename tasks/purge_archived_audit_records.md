![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Enable job to purge archived audit records

<!--
SortString: 0230
Description: Enable the routine purging of archived audit records from the archive location (PV)
Tags: Initial,New,Done
Topic: Observability
Essential: -
Authors: Ajmal Farzam
-->
When: Initial

The Audit service can be configured to periodically run a job that deletes records from the audit archive location (persistent volume) that have exceeded their defined archive retention period. Different types of audit records can have different expiration dates, as specified in the `sas.audit.archive.process` configuration instance (default value of 7 days for audit records and 1827 days, or 5 years, for activity records).

To enable the job that deletes expired records from the archive:
* Set the `sas.audit.purge` property to `enabled`
* Specify the schedule using cron syntax in `sas.audit.purge > purgeSchedule`.
* If required, adjust the retention period in the `sas.audit.archive.process` configuration instance's `audit.retention.in.archive` and `activity.retention.in.archive` properties.

See also:
* [Configure audit record archival](./audit_record_archival.md) [Task]
* [Configure the Audit Archive](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/p0txfp3picp59on1ua27dsqcpjwv.htm#n1g99yn3s6mk65n14y3i2z3df87a) [Doc]
* [Purging archived audit records](https://communities.sas.com/t5/SAS-Communities-Library/Purging-archived-audit-records-in-SAS-Viya/ta-p/839571) [Blog]

[Back to checklist](../checklist.md)