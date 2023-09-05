![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Load POSIX attributes

<!--
SortString: 0060
Description: Load POSIX attributes for identities when attributes are not returned from the authentication provider
Tags: New,Initial,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Gerry Nelson
-->
When: Before user access, As needed

Load POSIX attributes for identities when attributes are not returned from the authentication provider.

If users interact with the file system from the SAS Viya, the UID and GID that is used is crucial to the implementation of file system permissions. By default, after release 2022.10 the Viya identities service always provides a generated UID. In this case if existing UIDs and GIDs are desireable, but are not available from the identity provider, the Viya Administrator should load the UIDs and GIDs.

* sas.identities.identifier settings must be updated to support loading UIDs and GIDs
* the identities plug-in of the sas-viya CLI can be used to load UIDs and GID's
* pyviyatools also delivers a number of tools for managing POSIX attributes

Resources:

* [SAS Viya and POSIX attributes (UID and GID)](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-and-POSIX-attributes-UID-and-GID/ta-p/879229#:~:text=POSIX%20attributes%20like%20UID%20and%20GID%2C%20and%20Secondary%20GIDs%20are,files%20on%20shared%20file%20systems.)
* [How to Manage UIDs and GIDs with the Identities Service](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p0sgep5em2jdl1n1rbc9eqdim05t.htm)[Doc]
* [SAS Viya 2022.10 UID and GID Changes](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-2022-10-UID-and-GID-Changes/ta-p/841130)[Blog]

See also:

* [SAS Viya Secondary Groups & POSIX Considerations](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Secondary-Groups-amp-POSIX-Considerations/ta-p/728758)[Blog]
* [Configure umask for SAS Programmning run-time servers](./configure_programming_run-time_umask.md) [Task]
* [Pyviyatools: Set Posix Attributes](https://github.com/sassoftware/pyviyatools/blob/master/setposixattributes.py)[Tool]

[Back to checklist](../checklist.md)