![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Security Policy

<!--
SortString: 0170
Description: Write and maintain a security policy that covers the SAS Viya deployment
Tags: Initial,Legacy,Done
Topic: Organization & Governance
Essential: -
Authors: David Stern
-->
When: Before and/or after platform changes

## Write and maintain a security policy that covers the SAS Viya deployment

Most organizations have an organization-wide security policy. We recommend you include a section in that security policy or write a separate document to define policies specific to the SAS Viya deployment.

This should preferably be defined with the assistance of an experienced SAS architect before SAS software is installed because the installation process involves making several decisions about security. Security features are much less likely to be disruptive if applied during or immediately after installation than if they are applied retrospectively. The security policy should be periodically reviewed and revised as necessary throughout the lifetime of the platform.

The security policy should cover the following tasks:

* How users of the SAS Viya deployment are authenticated (LDAP, OIDC, SAML etc.) and how corporate user identities and group memberships are provided to SAS, e.g. pushed to the SAS Viya identities service by SCIM or pulled from LDAP provider such as Azure Active Directory or its equivalent in your chosen cloud provider.
* Set authorization (access rights and permissions) in SAS Viya, any databases accessed via SAS, Hadoop (for example, Hive), and operating-system-managed assets (for example, files and directories in the file system or files in block storage) used by SAS at a high level. Detailed authorization design is addressed by the security model in the next task.
* Manage certificates for Transport Layer Security.
* Encrypt content at rest (for example, data, files, code, passwords, and data sets stored on disk and data stored in databases).
* Encrypt data in motion (for example, data, credential, and message transmission using Transport Layer Security).
* Adopt standards of encryption and management, complexity, reuse, protection, and lifespan of cryptographic keys, passwords, salts, and so on.
* Protect system integrity (including physical security, availability, backup and recovery objectives, security of power, cooling, and so on).
* Audit.

[Back to checklist](../checklist.md)