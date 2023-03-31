![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Define a Process for Updating External Credentials

<!--
SortString: 0090
Description: Define a when and how you will update credentials that are stored in SAS Viya for external systems such as databases, when they change
Tags: Initial,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern
-->
When: After platform changes

If you store any credentials to external databases or other systems in
Authentication, Connection or Encryption Domains, establish a
procedure to ensure the credentials are changed whenever the passwords are
changed in the external database or other system.

Database credentials (such as usernames and passwords, access
tokens and keys etc.) should be accessible only by a limited group of
administrators. The same goes for ESRI Premium Services credentials, access keys,
encryption keys and other credentials.

The process to update them could be that the database or service administrator shares the
credentials with a SAS administrator or the database/service administrator has their own
SAS administrator account. Your process should state who will use (and if
necessary, *how* to use) the Credentials view on the Domains page of SAS Environment
Manager to update each credential, when a database password changes.

Credentials might be stored in an Authentication Domain, Connection Domain or
Encryption Domain, or they may be stored in some other secret or location in
your system as defined by the products and solutions deployed.
See [SAS Viya Administration > Securtity > Authentication >
External Credentials: Concepts](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcredentials/p1ntkxcd5ts4k1n1dboal0ywea70.htm?fromDefault=) for more information.

See Also: [Update External Credentials](./update_external_credentials.md)

[Back to checklist](../checklist.md)