![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Monitor Log Messages

<!--
SortString: 0520
Description: Monitor log messages
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern
Frequency: Daily
-->
When: Regularly per housekeeping schedule

Being able to effectively use a good set of log and metric monitoring tools is
essential for SAS Administrators. See [Why you need a log and metric monitoring
solution for the SAS Viya platform](https://communities.sas.com/t5/SAS-Communities-Library/Why-you-need-a-log-and-metric-monitoring-solution-for-the-SAS/ta-p/861725)
[Blog], which has links to many videos and other blog posts which may be useful
to learn more about log monitoring for SAS Viya.

Using whichever log monitoring tool you have implemented, learn by observing
your SAS Viya log messages regularly what 'normal' amounts of log messages look
like for ***your*** SAS Viya deployment, both overall and for key SAS Viya
services. Different SAS Viya deployments, with different topologies, usage and
software components have different patterns of 'normal' log messages.

As you become more used to what 'normal' looks like, you should become better
able to notice unusual patterns in volume or source of log messages. For
example, these might indicate that a service is stopped, being used more than
usual, experiencing an issue, or has been left in a state where it has an
elevated log threshold so that more log messages than normal are being output.

Not every 'ERROR' or 'WARNING' level log message is cause for concern, but over
time, you may learn which ones are of concern for your SAS Viya deployment and
which are not.

Make a list of notable log messages which might indicate an issue, and either
manually look for them from time to time, or set up alerts to notify you when
they appear.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Storage Space](./monitor_storage_space.md) [Task]

[Back to checklist](../checklist.md)