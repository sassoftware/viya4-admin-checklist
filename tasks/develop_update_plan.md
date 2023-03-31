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

The SAS Viya administrator may be required to regularly apply (or liaise with another person who will apply) updates the SAS Viya platform. Developing a robust process for applying updates is important for ensuring that updates are successful performed with minimal disruption, and that your Viya platform stays within the Standard Support window. These should be consolidated into an update plan.

An update plan should include:

* Instructions for how to check the deployed version of SAS Viya software. The recommended method is to run the [SAS Update Checker report](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm) [Doc].
* Instructions for how to [check whether updates are available](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm) [Doc] and how to subscribe to [update notifications](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0dyk8rscirt5an1g4nd0f0gtp0c.htm#p0xm4ml6u9vyrqn1h0s70pxlzxyu) [Doc].
* An agreed frequency for performing version updates and applying patch updates, i.e. how frequently to perform the steps in the task [Keep your Software Current](./keep_software_current.md).
* A plan for scheduling downtime for applying updates and communicating the schedule with end users.
* Agreed plans for liaising with stakeholders supporting the update, including the Kubernetes cluster administrator and support personnel.
* A runbook of required update tasks for [upgrading to new versions](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc] as well as for [applying patch updates](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]. The runbook should include all documented pre-requisite and post-update tasks, including reviewing requirements, taking backups and completing applicable tasks outlined in [Deployment Notes](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplynotes/titlepage.htm) [Doc]. For an overview of the process and related tasks, see [Keep your Software Current](./keep_software_current.md) [Task].
* A processes to follow and contacts SAS technical support, to use in the event of problems encountered during updates.

See also:
* [Keep your Software Current](./keep_software_current.md) [Task]
* [Best Practices and Guidelines for Updating Software](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0hm2t63wm8qcqn1iqs6y8vw8y81.htm) [Doc]
* [Apply a Patch Update](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p0954mgxmsddrmn1klrphsbnqasm.htm) [Doc]
* [Update to a New Version](https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p043aa4ghwwom6n1beyfifdgkve7.htm) [Doc]

[Back to checklist](../checklist.md)