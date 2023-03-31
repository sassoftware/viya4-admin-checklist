![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Decide approach to applying updates

<!--
SortString: 0280
Description: Decide how and when your SAS Viya software will be updated
Tags: Initial,New,Done
Topic: SAS Administration
Essential: -
Authors: Ajmal Farzam
-->
When: Initial

## Version Updates

SAS offers [two release cadences](https://go.documentation.sas.com/doc/en/sasadmincdc/default/itopscon/n0skwn6305faxnn1v0lfhzssr41u.htm) [Doc] so that the latest features and fixes can be applied at different intervals depending on business needs:

* The **Stable** cadence delivers monthly version updates to deployed SAS Viya software
* The **Long-Term Support** (LTS) cadence delivers six-monthly version updates to deployed SAS Viya software.

Refer to the [SAS Technical Support and Policies](https://support.sas.com/en/technical-support/services-policies.html#Viyastart) to understand expectations and support windows for each cadence.
To stay within the Standard Support level, which covers the current version and the three previous versions, you must perform regular updates (at least every four months on Stable cadence, and at least every 24 months on LTS cadence) to the deployed version (new *version* number) of your SAS Viya platform. Refer to [Updating to a Supported Version of the Same Cadence](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p168scdc52dssjn18eothkwcb7vy.htm#n1mldi1axcla70n1l28ropuftdb4) [Doc] for more information. See [Updating to a Supported Version on a Different Cadence](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p168scdc52dssjn18eothkwcb7vy.htm#p0ozgbwlx5t15cn1ggaigmyyx6pl) [Doc] for information on switching from one cadence to another.

SAS provides [different methods and tools](https://go.documentation.sas.com/doc/en/sasadmincdc/default/itopscon/p0839p972nrx25n1dq264egtgrcq.htm) [Doc] for deploying and updating the software. Updates should be performed using the same deployment method used to initially deploy the platform.

Updates are disruptive and may include manual steps. Consult the documentation including [Deployment Notes](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplynotes/titlepage.htm) [Doc] for your target and interim version for required tasks. The required sequence of tasks should be incorporated into an [update plan](./develop_update_plan.md) [Task].

## Patch Updates

Critical bug fixes and security vulnerability fixes are delivered as patch updates (new *release* number) as soon as they are ready on both cadences. Apply patch updates as soon as they become available.

If the SAS Deployment Operator is deployed, it can be used to automatically deploy patch updates. As an initial task, decide whether [automatic updates will be configured for patch updates](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplyml0phy0dkr/p13z9dnyxyi28yn131dnppnwpics.htm) [Doc]. If enabled, the SAS Deployment Operator automatically applies any `cadenceRelease` (patch) updates *within* the selected `cadenceName` and `cadenceVersion`. Note, however, that **patch updates may require manual steps to be performed**. As a precaution, always consult the documentation and refer to the README.md files in the root directory of the deployment assets for the release number you are updating to. The operator automatically checks for updates daily (configurable). Refer to [Manage Updates](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplyml0phy0dkr/p13z9dnyxyi28yn131dnppnwpics.htm) [Doc] for more information. The tasks required to apply patch updates should be included in your [update plan](./develop_update_plan.md) [Task].

See also:

* [Apply a Patch Update](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]
* [Update to a New Version](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc]

[Back to checklist](../checklist.md)