![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Change log levels

<!--
SortString: 0540
Description: Change the log threshold for a SAS component or service, to increase or decrease the detail of log messages it produces
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Frequency: When troubleshooting
Authors: David Stern
-->
When: At the beginning and end of a period of troubleshooting activity

## Log message severity

Practically all SAS Viya services output log messages, which have a range of possible severities. These severity levels are described here for CAS, but the same severities are used in all SAS Viya components: [Logging Thresholds](https://go.documentation.sas.com/doc/en/sasadmincdc/default/callogging/p0iu4czueno6x7n1o0nnhsz34nqq.htm) [Doc]. From that documentation page, log severity levels are:

| Log severity level | Description |
| --------- | ----------- |
|Trace | produces the most detailed log messages. This level might be useful when isolating the cause of a problem, but it produces too many messages for normal use. |
| Debug | produces detailed log messages, although less detailed than the Trace threshold. This level might be useful when isolating the cause of a problem, but it produces too many messages for normal use. |
| Info | produces messages that show an application’s progress. |
| Warn | produces messages that identify areas of potential problems. |
| Error | produces messages when errors occur, although the application might continue to run. |
| Fatal | produces messages when severe errors occur. The application probably ends. |

A few SAS Viya components or services (generally those which include components originally written by other organizations) may output log messages with no severity or level value, or with a severity of NONE. A log level of NONE does not indicate a severity.

## Log output severity threshold

We do not want most services to output every  log message they possibly could all the time, because most of the time, the TRACE and DEBUG messages are of little value, and would be produced in great volume. Sometimes, even INFO level messages are too 'chatty', and for a relatively unimportant service, we are normally content to see only ERROR or FATAL messages.

For this reason, practically all SAS Viya components also have a log threshold (or log level) setting, with a value of INFO for most services, which prevents less-severe messages than the set value from being written to the log output.

So, looking at the table above, for a service whose log threshold is set to INFO, that service will only produce INFO, WARN, ERROR and FATAL messages, while TRACE and DEBUG messages are suppressed.

However, if you as SAS Administrator want to see greater detail in the log messages for that service, perhaps to help troubleshoot an issue, you may choose to ***temporarily*** lower the log threshold to DEBUG or even TRACE, so that those lower-severity, messages are output by the service.

Having reviewed the additional log output, you restore the log threshold to its former (normal) level, so as to avoid filling up the log storage with unnecessary detailed messages you will likely no longer need.

## Changing the log threshold for a service

Two log threshold configuration patterns are used in the SAS Viya platform.

1. For **most** SAS Viya services, but not CAS and the SAS Programming Run-Time servers (sas-compute, sas-connect and sas-batch), see:
   1. [Specify the Threshold Level for Service Logs](https://go.documentation.sas.com/doc/en/sasadmincdc/default/callogging/p06eoiaxtu8udtn1q4avwpet6ds8.htm) [Doc], which describes how to change - or create - a **logging.level** configuration instance for a service through SAS Environment Manager's configuration page.
   1. [SAS Demo | Viewing Logs with SAS Viya Monitoring for Kubernetes: Changing Log Levels](https://www.youtube.com/watch?v=pGMj23QCA_c) [Video]
1. CAS and the SAS Programming Run-Time servers (sas-compute, sas-connect and sas-batch) use a log4SAS logconfig XML document to configure loggers and appenders:
   1. For CAS servers, see [Manage CAS Server Logging](https://go.documentation.sas.com/doc/en/sasadmincdc/default/callogging/p06eoiaxtu8udtn1q4avwpet6ds8.htm#n0mkearstln1jqn1s7gvozihdd58) [Doc]
   1. For the Compute Service see SAS Viya Platform Administration > Servers and Services > Programming Run-Time Environment > SAS Compute Server and Compute Service > [Configuration Instances: Compute Service](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00001viyaprgmsrvs00000admin.htm#p0bf5lk5doeuq6n1dp5lilix7wrv) [Doc], and below that link, 'sas.compute.server: logconfig'.

   Log configuration for the SAS Connect and SAS Batch servers is similar to that for the SAS Compute Server.


[Back to checklist](../checklist.md)