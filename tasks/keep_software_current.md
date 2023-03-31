![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Keep your Software Current

<!--
SortString: 0590
Description: Keep your software current with patch and version updates to stay within Standard Support guidelines.
Tags: Regular,New,Done
Topic: SAS Administration
Essential: -
Author: Scott McCauley,Ajmal Farzam
Frequency: Monthly
-->
When: Regularly

## Overview

There are two main types of updates applicable to a Viya deployment:

* [Patch Updates (updates release number)](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]
* [Updates to a New Version (updates version number)](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc]

Perform updates using the documented instructions linked above for the deployment method you used for the intial deployment. If the SAS Deployment Operator was used, you should follow the instructions for performing the update using the Deployment Operator. If the Deployment Operator was not used, consider deploying it prior to the update and then performing the update using the operator.

Both types of updates may include manual steps, which can include tasks such as restarting CAS servers or making configuration changes in SAS Environment Manager. Carefully read [Deployment Notes](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplynotes/titlepage.htm)  [Doc] for target and interim versions (if skipping versions) and the README.md file in your Deployment Assets archive to verify whether any manual steps or product-specific customisations need to be performed before or after the update.

You may also be required to [update with a new software order](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0wgfbnhvyy2ddn197vzpecdedpe.htm) [Doc] if products have been added to or removed from your SAS license. It is also possible to [switch from one cadence to another](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p168scdc52dssjn18eothkwcb7vy.htm#n0chk9gigni4ban1v7tsyg3vqcbg) [Doc], but be aware that this changes your support agreement with SAS.

## Keep your SAS Viya platform software current with patch and version updates to stay within Standard Support guidelines.

To keep your software up-to-date and covered by Standard Support, update the software to the latest version as it becomes available.

* Apply patch updates as they become available. Patch updates can be released anytime and can include critical fixes and security updates. Patch updates are delivered as new container images and can be thought of as being analagous to SAS 9.4 hotfixes.
* Update to the latest version for your cadence (Stable or Long-Term Support) as it becomes available. For current SAS Viya platform support guidelines consult [SAS Technical Support and Policies](https://support.sas.com/en/technical-support/services-policies.html#Viyastart).
* Opt in to receive emails about new versions that are available for your software order at [my.sas.com](https://my.sas.com) (My SAS). Also, you can view the list of available versions for the deployment assets from your software order. Typically, all versions that are available from your software order are covered by Standard Support.

Primary resources:

* [SAS Viya Platform Operations: Updating Software](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/titlepage.htm) [Doc]
* [SAS Technical Support and Policies](https://support.sas.com/en/technical-support/services-policies.html#Viyastart) [Doc]

## Patch updates

The easiest way to know of the availability of patch updates for your deployment
is to view the results of the Update Checker job which is scheduled to run weekly.

Patch update resources:

* [View the Update Checker Report](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm) [Doc]
* [Apply a Patch Update](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]

## Version updates

Version updates for the SAS Viya platform are released on a set schedule. You should review the release schedule for your cadence and plan for updates as versions become available.

Version update resources:

* [Release Schedule and Versions](https://go.documentation.sas.com/doc/en/sasadmincdc/default/itopscon/n0skwn6305faxnn1v0lfhzssr41u.htm) [Doc]
* [Update to a New Version](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc]

## Update other software

In addition, consider updating:

* [SAS Deployment Operator](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0dyk8rscirt5an1g4nd0f0gtp0c.htm#p08v6eq9jyj6iwn0z2yoz1xgz5h3) [Doc] - *recommended each time you update to a new version*
* [Mirror Registry](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0dyk8rscirt5an1g4nd0f0gtp0c.htm#p15fercepbok98n1k30hzbt9nydh) [Doc] - *recommended each time you update to a new version*
* [SAS Viya Monitoring for Kubernetes](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/p1urfnrds62qman1wh40uzomqymf.htm) [Doc] (if deployed) - *recommended at least every six months*
* Other monitoring or observability tools (if deployed), e.g. Lens/OpenLens. See [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task] and [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]


See Also:

* [Develop an update plan](./develop_update_plan.md) [Task]
* [Are updates available for my deployed Viya software? A use case for alerting on log data](https://communities.sas.com/t5/SAS-Communities-Library/Are-updates-available-for-my-deployed-Viya-software-A-use-case/ta-p/750916) [Blog]

[Back to checklist](../checklist.md)