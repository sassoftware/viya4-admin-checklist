![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Define a Process for Onboarding and Offboarding Users

<!--
SortString: 0300
Description: Document any steps that must be performed when new users are onboarded and offboarded
Tags: Initial,Legacy,Done
Topic: SAS Administration
Essential: Yes
Authors: David Stern,Michael Erickson
-->
When: After platform changes

See Also: [Onboard and Offboard Users](onboard_and_offboard_users.md)

## Define a Process for Onboarding and Offboarding Users

Document any steps that must be performed when new users are onboarded and given access to your SAS Viya deployment.

Users in SAS Viya are added and removed only through one of:

* your SCIM provider, or
* your LDAP provider (for example, Active Directory, OpenLDAP, or something similar)

Consider whether and how you will know when users are added, moved, or removed? Consider group memberships for new or departing users, especially custom group memberships. Does your onboarding or off boarding process need steps to maintain the application of your authorization model for new users? Do you need to create home directories for new users and archive (or delete) home directories for departing users? Do new users require training or orientation? Should they be required to agree to any terms or conditions of use or working practices before gaining access?

Learn about either your SCIM provider, or your LDAP provider, whichever is configured to populate users in your SAS Viya deployment.

If your deployment is populated with users and groups by a SCIM provider, learn how to manage those users and groups in the SCIM product (or alternatively, how they are managed), and learn what user attributes are (and are not) passed to SAS Viya. Since users are pushed to SAS by a SCIM provider, determine how you will know when new users are added, departing users are removed, or significant group memberships change.

If you are using LDAP, know what Distinguished Names, Common Names, Entries, and Attributes are. Learn how to use an LDAP client GUI to view (or edit if you have permission) the LDAP directory used by your SAS Viya deployment. Familiarize yourself with its structure. Again, determine how you will know when users are added and removed, or moved between groups.

If you are using LDAP, review the objectFilter queries in the [sas.identities.providers.ldap.group](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p1t79jdoqkwqc4n15uu4n12svunr.htm) and [sas.identities.providers.ldap.user](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p1t79jdoqkwqc4n15uu4n12svunr.htm) configuration instances for the Identities service on the Configuration page of SAS Environment Manager. Consider adjusting objectFilter queries to modify the groups and users returned to your deployment’s Identities service to exclude unwanted users and groups from the SAS Viya deployment.

You might find Gerry Nelson’s post on the SAS Users blog about [LDAP basics for the SAS Viya Administrator](https://blogs.sas.com/content/sgf/2017/12/06/ldap-basics-for-the-sas-viya-administrator/) helpful, along with the official documentation in the [Identities Service Configuration](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfigref/n0wjds8h1mtrj8n1oirvrx2je7fb.htm) topic. This is mostly a post-installation task, but it is useful for SAS Viya administrators to know about it.

See also: [Onboard and Offboard Users](onboard_and_offboard_users.md)

[Back to checklist](../checklist.md)