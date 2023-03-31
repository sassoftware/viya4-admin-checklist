![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Monitor Memory, CPU, Network, and Disk Throughput Usage

<!--
SortString: 0510
Description: Monitor memory usage, CPU usage, network I/O usage, disk throughput usage, input/output operations per second (IOPS), etc
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern,Michael Erickson
Frequency: Daily
-->
When: Regularly per housekeeping schedule

## Monitor memory usage, CPU usage, network I/O usage, disk throughput usage, input/output operations per second (IOPS), etc

At the cluster or node level, take measurements regularly (for example, every 5 minutes) and maintain a time history of these measurements (for example, 30 days). Analysis of the time series history is usually more insightful than a single-point measurement.

At the pod level, use your monitoring tools to measure disk I/O in launched SAS Programming Run-time pods (sas-compute-server, sas-connect-server, sas-batch-server), especially where the SAS Programming run-time pod has fewer cores allocated to it (due to settings for container and pod CPU Requests and Limits) than the host nodes have available. Understand how to measure the I/O in mbps (megabits per second) and calculate mbps/core speed, to ensure you are getting the expected/intended I/O throughput performance for SAS Programming Run-time sessions.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Storage Space](./monitor_storage_space.md) [Task]

[Back to checklist](../checklist.md)