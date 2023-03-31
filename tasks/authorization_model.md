![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Authorization Model

<!--
SortString: 0180
Description: Write and maintain a security model or an authorization model
Tags: Initial,Legacy,Done
Topic: Organization & Governance
Essential: Yes
Authors: David Stern,Michael Erickson
-->
When: Before and/or after platform changes and in tandem with organizational changes

## Write and maintain a security model or an authorization model

A documented authorization model implements certain requirements of your security policy and describes how users should be organized into groups. Groups determine their access to resources such as SAS Viya content, data, and application functionality. Define how users, groups and where relevant, service accounts will be added to, updated in, and removed from the SAS Viya deployment, i.e. using SCIM or LDAP.

Define what operating-specific settings and rights are required for each group of users of the SAS Viya deployment.

There are several major components of a security model for the SAS Viya deployment. You should maintain two documents each representing part of your security model. The first is a relatively static document that defines the overall principals and guidelines for how users are managed and granted or denied permissions. But, it avoids user-specific detail. This document can however define access that groups should be granted to resources such as folders and their content (e.g. reports), data, application functionality (including applications themselves, functionality within applications, maps and scheduling capability) and also to CAS libraries and tables.

The second is a more frequently changing living record of the specific state in which users and groups (within the context of the SAS Viya deployment) should currently be. Record your authorization design in a way that is suitable for change tracking in e.g. markdown, and store it in a version-control repository such as git. Doing so enables you to identify what changes were made by whom, when with greater reliability and less effort than manually documenting changes. Consider using this document to drive automation of some elements of user and group configuration, such as the creation, deletion and membership of certain SAS Viya custom groups.

Users and groups in SAS Viya are defined either:
* in SCIM, where the SCIM provider pushes identity information to SAS Viya's identities service, or
* in an external LDAP directory server such as Active Directory and loaded by the SAS Viya Identities service.

Additional custom groups are defined and managed by the Identities service. They can also be managed through the SAS Environment Manager > Users page and through the [`sas-viya` command-line interface](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcli/titlepage.htm)'s [`identities` plug-in](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p16ecdrk53y0cmn10e0wajcvi7xy.htm?fromDefault=).

See [SAS Viya Platform Administration: Identity Management](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/titlepage.htm) or more on managing identities, including how to configure SCIM and LDAP.

See [SAS Viya Platform Administration: Orientation to Authorization](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthz/titlepage.htm) for a guide to the CAS authorization system and the SAS Viya general authorization system, which are used together in SAS Viya deployments.

[Back to checklist](../checklist.md)