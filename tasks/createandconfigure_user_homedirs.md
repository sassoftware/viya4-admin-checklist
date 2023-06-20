![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Create and Configure User home-directories

<!--
SortString: 0070
Description: Create and configure user-home directories
Tags: New,Initial,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Gerry Nelson
-->
When: Before user access, update as needed

SAS users are used to having their operating system home-directories available while they work. SAS Viya 4 requires additional configuration to make home directories available. In addition SAS Viya 4 does not support automatic creation of home directories, home directories must be created.

If home directories do not exist:

* Use the provided Technical Support sample script referenced below to create user home directories.

If home directories already exist on shared storage follow the process in the blog post *SAS Viya: making user home directories available to compute*. The process will:

* Mount in a shared location where home directories reside
* Add an annotation to the compute pod template that references the NFS server where the shared location is located
* Update the identites configuration to set the identifier.homeDirectoryPrefix prefix property with the path to the location where the home directories reside
* Configure SAS Studio to be able to see the home-directories

If home-directory (CASUSER path location) access is desired in CAS, host launch must be enabled and the user must be a member of the CASHostAccountRequired Custom Group.

Resources:

* [Sample 68620: Create user home directories from the identities service in SAS® Viya® 2020.x using a script](https://support.sas.com/kb/68/620.html) [Sample Script]
* [SAS Viya: making user home directories available to compute](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-making-user-home-directories-available-to-compute/ta-p/717561) [Blog]
* [CAS Enable Host Launch](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm#n07xq4q4omccg0n1v4lj63i57r62) [Doc]
* [Indentity Management: The CASHostAccountRequired Custom Group](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p0ata1oqy9v7nan188h1k254doxq.htm#p1b0uixk221q3jn19ztuitir62gm) [Doc]

See Also:

* [Home Directories in SAS Viya 4](https://seleritysas.com/blog/2022/05/22/home-directories-in-sas-viya4/) [Blog]
* [Configuration Properties for SAS Studio](https://go.documentation.sas.com/doc/en/webeditorcdc/default/webeditorag/n0ivozv0jsbj2un1bn6c50x95lw7.htm) [Doc]
* [Setting Configuration Properties](https://go.documentation.sas.com/doc/en/webeditorcdc/default/webeditorag/p1croko9cfg78vn1bsv6x390lioz.htm) [Doc]
* [CAS Host Account Required](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p0ata1oqy9v7nan188h1k254doxq.htm#p1b0uixk221q3jn19ztuitir62gm) [Doc]

[Back to checklist](../checklist.md)