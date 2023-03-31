![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Secure the sasboot password

<!--
SortString: 0310
Description: Disable the sasboot password reset feature after you have finished setting up identities and initial administrators
Tags: Initial,New,Done
Topic: SAS Administration
Essential: -
Authors: David Stern
-->
When: Before user access, as needed

## Disable the Password Reset Feature

From the documentation linked below:

*When you are finished setting up SCIM or LDAP and the initial administrative users, you should reset the password for the sasboot user. For additional security, you can then disable the password reset feature. This action prevents password reset links from being written to the log each time the SASLogon service is restarted.*

## Reset the sasboot Password

From the documentation linked below:

*After you disable this feature, you can still change the sasboot password if the existing password is known.*

Resources:

* [How to Secure the sasboot Password](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p0pqmcgf79tt3on1nz35a15gcfj7.htm) [Doc]

[Back to checklist](../checklist.md)