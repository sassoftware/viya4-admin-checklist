![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Know how to Contact SAS Technical Support for Help

<!--
SortString: 0260
Description: Ensure all SAS platform administration staff know how to contact SAS Technical Support for help
Tags: Initial,Legacy,Done
Topic: SAS Administration
Essential: -
Authors: David Stern,Michael Erickson
-->
When: Post-install, after platform changes, or after organizational changes

SAS Technical Support [can be contacted](https://www.sas.com/en_us/contact/technical-support.html) using a web page to open a track or by email, chat, or phone.

Know which [local support office to call](https://www.sas.com/en_us/contact.html#global-locations) for service. There is usually one in your country. The first-line technical support consultant will ask you for some basic information during the initial conversation. This includes information about your SAS platform (for example, its site number, installed products, and the operating system) and your contact details. Many organizations have multiple SAS platforms or environments. It is common for these to have different site numbers. Do not assume the site number from one of your environments is shared by your other environments.

In certain situations, other departments in SAS Professional Services might be better able to assist you than SAS Technical Support. For example, consider engaging SAS Professional Services consultants or technical architects if you are planning a new installation, a hardware or software upgrade, or a migration. SAS Premium Support or your country’s SAS Customer Success team can help with needs that require ongoing support and that fall somewhere between consultancy projects and technical support.

Contact your usual SAS account representative or SAS sales representative in your country if you are interested in using or trying additional SAS software.

Also, ensure that all SAS Viya platform administration staff are familiar with the content of your shared repository of documentation for the SAS platforms that they support, as discussed in [Identify Components of SAS and Third-Party Software](./identify_viya_components.md) [Task].

## Sending log messages to SAS Technical Support

SAS Technical Support representatives often ask to see log messages from your SAS Viya deployment. Unlike SAS 9 and SAS Viya 3 which produced log files that you could find and attach to e.g. email or upload to our SAS Technical Support web site, SAS Viya does not produce log files. Instead, the SAS Viya platform follows the standard Kubernetes pattern of writing all its log messages to stdout and stderr inside each pod, from where they are picked up by Kubernetes and stored in the pod logs. You can use kubernetes tools (like the kubectl CLI), to access, search, view and further process log messages. However, we recommend you use a Log Monitoring tool, such as the logging component of [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes), or the log monitoring stack offered by your Cloud Provider to give you a much more capable and feature-rich log message capture, storace and analysis tool for log monitoring.

Knowing where to find logs messages and how to find specific messages will simplify the process of providing information about an issue to SAS Technical Support.

See also:

* [Ways to View Log Messages](https://go.documentation.sas.com/doc/en/sasadmincdc/default/callogging/p0a7df6ku17zx3n1uqvo130phlzx.htm) [Doc]
* [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes) [GitHub project]
* [SAS Demo | Viewing Logs with SAS Viya Monitoring for Kubernetes: Changing Log Levels](https://www.youtube.com/watch?v=pGMj23QCA_c) [Video]
* [SAS Demo | Viewing Logs with SAS Viya Monitoring for Kubernetes: Managing Log Retention](https://www.youtube.com/watch?v=7TrOxfx6WdU) [Video]

You may be asked to send SAS Viya logs as part of the troubleshooting process, and in order to get the log messages needed, you may need to [change log levels](./change_log_levels.md) [Task].



[Back to checklist](../checklist.md)