![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Examine the User Activity Report

<!--
SortString: 0530
Description: Examine the user activity report
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern
Frequency: Weekly
-->
When: Regularly per housekeeping schedule

Once a week, or at another frequency that makes better sense for your organization, open the [User Activity report](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/p0txfp3picp59on1ua27dsqcpjwv.htm#n1jiq82q4ma2kkn1aj4st3z65mla) which is provided with the SAS Viya platform.

You can use this report to get an overview of how users are using your SAS Viya deployment. The report provides high-level information on the most active users, logins over time, most used applications, most used reports, and about tables access through applications like SAS Visual Analytics which uses the CAS Management Service to access data.

However, you should be aware of some of the limitations of the audit data available in SAS Viya platform: data access directly in CAS (i.e. not going through the CAS Manangement Service) is not recorded in the audit data. Data access of BASE and library tables from a SAS Programming Run-Time session - i.e. a compute, connect or batch session, is not recorded in the audit tables.

See [Audit: Overview](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calaudit/n0buxigkyloiv2n1s0i5jfhyxunm.htm) [Doc] for urther detail of how auditing works in the SAS Viya platform currently.

Look for connections from users or applications that should not be connecting.

See Also: [Configure audit record archival](./audit_record_archival.md) [Task]

[Back to checklist](../checklist.md)