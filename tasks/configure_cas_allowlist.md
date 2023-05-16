![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure CAS Allowlist

<!--
SortString: 0340
Description: Configure CAS allowlist for user-defined CAS libraries
Tags: Initial,New,Done
Topic: CAS
Essential: Yes
Authors: Scott McCauley
-->
When: Before user access, as needed

From a CAS server session, all access to file system paths (directories that are
local to the host and to shared file systems) is through caslibs. By default,
all users who lack elevated privileges are denied the ability to create caslibs
outside of the paths that are specified in the default allowlist.

If you plan to allow non-admin users to define caslibs to additional file system paths,
you must add those paths to the CAS allowlist.

Resources:

* [SAS Viya Platform Administration: Paths List](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calserverscas/n05000viyaservers000000admin.htm#n05013viyaservers000000admin) [Doc]
* [SAS Viya Platform Administration: Manage Path Lists (ALlowlists and Denylists)](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/n0mq74h3dneq5on1l5gn4e5mwwc8.htm#p1obp8jdrwsjd2n17whi7txun5sh) [Doc]

See Also:

* [Accessing path-based data from CAS in Viya](https://communities.sas.com/t5/SAS-Communities-Library/Accessing-path-based-data-from-CAS-in-Viya/ta-p/714291) [Blog]
* [Storage for CAS Libraries](caslib_storage.md) [Task]
* [Configure Programming Allowlist](./configure_programming_allowlist.md) [Task]

[Back to checklist](../checklist.md)