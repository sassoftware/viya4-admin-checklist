![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Develop an update plan

<!--
SortString: 0030
Description: Develop an update plan: outline tasks required before, during and after an update
Tags: Initial,New,Done
Topic: Kubernetes & IT Admin
Essential: Yes
Authors: Ajmal Farzam
-->
When: Initial

The SAS Viya administrator will be required to routinely apply (or liaise with another party who will apply) patch updates and version updates to the SAS Viya platform. Developing a robust process for applying updates is important for ensuring that updates are successfully performed with minimal disruption, and that the SAS Viya platform stays within the Standard Support window. These should be consolidated into an update plan.

An update plan should include:

* Instructions to check the deployed version of SAS Viya software. The recommended method is to run the [SAS Update Checker report](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm) [Doc].
* Instructions to [check whether updates are available](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm) [Doc] and how to subscribe to [update notifications](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0dyk8rscirt5an1g4nd0f0gtp0c.htm#p0xm4ml6u9vyrqn1h0s70pxlzxyu) [Doc].
* Steps to validate [supported update paths](https://go.documentation.sas.com/doc/en/sasadmincdc/default/itopsup/p1lam22gz8zj8gn1b51yczorenun.htm) [Doc]. 
* An agreed frequency for updating local mirror registries (if applicable), performing version updates and applying patch updates (i.e. how frequently to perform the steps in the [Keep your Software Current](./keep_software_current.md) task).
* A plan for scheduling downtime for applying updates and communicating the schedule with end users.
* Agreed plans for liaising with stakeholders supporting the update, including the Kubernetes cluster administrator and support personnel.
* A runbook of required update tasks for [upgrading to new versions](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc] as well as for [applying patch updates](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]. The runbook should include all documented pre-requisite and post-update tasks, including completing the [pre-update checklist](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1sv25bpu9fl2xn1ecj5j89dxubt.htm), reviewing requirements, taking backups and completing applicable tasks outlined in [Deployment Notes](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplynotes/titlepage.htm) [Doc] and the [What's New](https://go.documentation.sas.com/doc/en/sasadmincdc/default/itopswn/titlepage.htm) section for the target version. For an overview of the process and related tasks, see [Keep your Software Current](./keep_software_current.md) [Task].
* If you are operating in air-gapped site with no internet access, ensure that your plan includes steps for checking for updates (e.g. using a proxy), obtaining deployment assets, updating deployment tools (e.g. sas-orchestration or SAS Deployment Operator) and updating your local mirror registry prior to performing any updates.
* Recovery and rollback procedures, including [SAS Technical Support](https://support.sas.com/en/technical-support.html) information, to use in the event of problems encountered during updates.

See also:
* [Keep your Software Current](./keep_software_current.md) [Task]
* [Best Practices and Guidelines for Updating Software](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0hm2t63wm8qcqn1iqs6y8vw8y81.htm) [Doc]
* [Apply a Patch Update](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]
* [Update to a New Version](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc]
* [Checking for SAS Viya Updates at Dark Site Environments](https://communities.sas.com/t5/SAS-Communities-Library/Checking-for-SAS-Viya-Updates-at-Dark-Site-Environments/ta-p/981869) [Blog]

[Back to checklist](../checklist.md)