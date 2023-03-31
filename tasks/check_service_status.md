![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Check the Status of SAS services

<!--
SortString: 0500
Description: Regularly check the status of SAS services
Tags: Regular,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern,Michael Erickson
Frequency: Daily
-->
When: Regularly per housekeeping schedule

Using one or more of the tools described in the task [Understand how to Check the Status of Services](how_to_check_service_status.md), determine whether your SAS services are running and responding.

## What to do if any services are not running normally

If any services are not running normally, or are running but responding normally, investigate why. Here are some questions you might try to answer:

* Were these services running in your SAS Viya deployment previously?
* Do you have notes in a runbook or configuration document that explain *why* these services might not be running?
* Do the services that are not running produce log messages at all (or do they produce no log message)?
* If they produce log messages, is there anything in these log messages which indicates why the service is experiencing problems starting or running normally?
* Using a tool such as Lens, OpenLens, K9s or OpenSearch Dashboards (part of SAS Viya Monitoring for Kubernetes), or just kubectl logs, do you see any kubernetes events relating to the services which indicate why they are not starting normally?

Searching the web for any error messages you find can be very helpful in diagnosing what is happening.

Discuss the issues you discover with your architects, deplopyment engineers and SAS Administrator colleagues. Perhaps there is a reasonable explanation for why it is not running, such as a planned outage?

If necessary, you can contact SAS Technical Support. Ensure you [Know how to Contact SAS Technical Support for Help](./contact_SAS_technical_support.md) [Task].

[Back to checklist](../checklist.md)