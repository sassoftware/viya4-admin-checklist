![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Monitor Observability Storage

<!--
SortString: 0560
Description: Monitor the disk or other storage space used for the log and metric monitoring tools, and other observability tools deployed to monitor SAS Viya
Tags: Regular,New,Done
Topic: Observability
Essential: -
Authors: David Stern
Frequency: Weekly
-->
When: Regularly per housekeeping schedule

This task is not applicable if your observabilty tools (log and metric monitoring etc.) are provided by a service that has effectively unlimited capacity, or whose capacity you cannot measure or manage.

As often as your schedule indicates, note the amount of used and free storage in volumes used by your observability tools.

For example, if you have deployed SAS Viya Monitoring for Kubernetes, you should pay attention to the free/used space in the OpenSearch persistent volumes (in the log monitoring namespace, used for log document storage and other data required for OpenSearch), and in the Prometheus

Consider setting up alerts for disk utilization reaching e.g. 80% of total capacity, or when the space used is growing at a rate which might fill the disk within a short period of time, e.g. a week.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Storage Space](./monitor_storage_space.md) [Task]
* SAS Demo | Viewing Logs with SAS Viya Monitoring for Kubernetes: [Managing Log Retention](https://www.youtube.com/watch?v=7TrOxfx6WdU) [Video]

[Back to checklist](../checklist.md)