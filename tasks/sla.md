![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Service Level Agreement

<!--
SortString: 0140
Description: For enterprise-scale deployments, define a Service Level Agreement (SLA)
Tags: Initial,Legacy,Done
Topic: Organization & Governance
Essential: -
Authors: David Stern
-->
When: Outline pre-install, review, and adjust post-install

## For enterprise deployments, define a Service Level Agreement (SLA)

The SLA states the measures that you use for service-level monitoring and reporting and how they will be calculated. Implement a service-level reporting product to calculate these measures when they are based on time-history data from a service-level monitoring component.

Consider measuring service-level performance for the system as a whole and for specific subsystems that can operate independently.

Measure the service-level performance using metrics such as:

Availability:

* Availability over specific periods of time - proportion of that time period over which the service was available
* Unplanned outage duration: duration of each period of unavailability that is considered an outage in a given period of time
* Planned outage duration: duration of planned outages in a given period of time
* Mean time between failures: mean time between unplanned outages, and
* Actual recovery time from unplanned outages, as a straight value and compared with recovery time objective.

    *Actual recovery time is the elapsed time from when an outage is detected until the time when recovery is successfully achieved to a specific level, as defined in your [disaster recovery](./disaster_recovery.md) strategy. Consider categorizing the recovery times into those from which it was possible to recover to the intended recovery point, and those from which you are forced to recover to an earlier recovery point because of a corrupted backup, or similar 'problematic' recovery.*

Workload performance:
* Mean time for an end user to sign in over time
* Mean time to start a Compute/CAS/Batch session over time
* Mean time to complete a standard piece of compute workload, once started (i.e. runtime, not queue time)
* Other workload measures as appropriate to your organization

See Also: [Understand how to Check the Status of Services](./how_to_check_service_status.md) [Task]

[Back to checklist](../checklist.md)