![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Define a backup and restore strategy

<!--
SortString: 0250
Description: Define a backup and restore strategy
Tags: Initial,New,Done
Topic: SAS Administration
Essential: Yes
Authors: David Stern,Michael Erickson,Gerry Nelson
-->
When: After platform changes

Define a strategy for creating, preserving and restoring Viya Backups. Backups are critical in Enterprise Software. In SAS Viya a good backup is key to protecting your environment and supporting the restoration of lost content or a complete environment. SAS Viya 4 supports backup and restore using native Kubernetes technologies. The primary resource for implementing your backup stragegy is the SAS Viya Platform Backup documentation [here](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calbr/titlepage.htm). Your backup strategy should include the steps to:

* Configure the frequency of scheduled backups
* Check the status of scheduled backups
* Learn how to perform an ad-hoc backup
* Configure the retention period for backup packages
* Ensure backup persistent volumes are retained
* Develop an approach for copying/moving backup packages
* [Test the Process to Restore From Backups](./test_restore_process.md)

In addition:

* Consider if a partial backup of content is required
* Implement enterprise backup tools that cover critical assets in your SAS Viya deployment that the backup and restore function does not back up

Resources:

* [SAS Viya Platform Administration: Backup and Restore](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calbr/titlepage.htm) [Doc]
* [A first look and Backup and Restore in SAS Viya on Kubernetes](https://communities.sas.com/t5/SAS-Communities-Library/A-first-look-and-Backup-and-Restore-in-SAS-Viya-on-Kubernetes/ta-p/740634) [Blog]
* [A generic method for copying backup packages for migration or disaster recovery](
https://communities.sas.com/t5/SAS-Communities-Library/A-generic-method-for-copying-backup-packages-for-migration-or/ta-p/765158) [Blog]
* [Retaining your SAS Viya Backup](
https://communities.sas.com/t5/SAS-Communities-Library/Retaining-your-SAS-Viya-Backup/ta-p/845138) [Blog]

See Also:

* [Test the Process to Restore From Backups](./test_restore_process.md) [Task]


[Back to checklist](../checklist.md)
