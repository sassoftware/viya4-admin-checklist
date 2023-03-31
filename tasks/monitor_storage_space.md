![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Monitor Storage Space

<!--
SortString: 0550
Description: Monitor the disk space used for SAS Viya
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern,Michael Erickson
Frequency: Weekly
-->
When: Regularly per housekeeping schedule

As often as your schedule indicates, note the amount of used and free storage in volumes used by your SAS Viya deployment. Look especially for volumes whose space used is growing over time and may eventually become full, and for volumes which are nearly full now. Pay particular attention to storage volumes used for SAS Work,  permanent SAS libraries. If either fills up completely, this can easily cause SAS programs to fail.

Similarly monitor and keep free some storage space for CAS libraries, backups and user data stored in formats not directly managed by SAS, e.g. input data from other systems or output data.

Consider setting up alerts for disk utilization reaching e.g. 80% of total capacity, or when the space used is growing at a rate which might fill the disk within a short period of time, e.g. a week.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Observability Storage](./monitor_observabilty_storage.md) [Task]

[Back to checklist](../checklist.md)