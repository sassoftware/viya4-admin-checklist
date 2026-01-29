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

* Choose one of the backup workflows either SAS Viya Application Backup Only or SAS Viya Application Backup and Cloud-Provider for external PostgreSQL 
* Configure the frequency of scheduled backups
* Check the status of scheduled backups
* Learn how to perform an ad-hoc backup
* Configure the retention period for backup packages
* Ensure backup persistent volumes are retained
* Develop an approach for copying/moving backup packages
* [Test the Process to Restore From Backups](./test_restore_process.md)

In addition:

* Consider if a partial backup of content is required. If so consider the approach in the post [Selective backup and restore of SAS Viya Content](https://communities.sas.com/t5/SAS-Communities-Library/Selective-backup-and-restore-of-SAS-Viya-Content/ta-p/968018) 
* Implement enterprise backup tools that cover critical assets in your SAS Viya deployment that the backup and restore function does not back up

Resources:

* [SAS Viya Platform Administration: Backup and Restore](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calbr/titlepage.htm) [Doc]
* [SAS Viya Backup and Restore: new features add flexibility](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Backup-and-Restore-new-features-add-flexibility/ta-p/920692)[Blog]
* [SAS Viya: Restore a Backup in 2023.10 and later](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Restore-a-Backup-in-2023-10-and-later/ta-p/906300) [Blog]
* [Restore a Viya Backup with SAS Viya Backup and Database Point in Time Restore](https://communities.sas.com/t5/SAS-Communities-Library/Restore-a-Viya-Backup-with-SAS-Viya-Backup-and-Database-Point-in/ta-p/914711)[Blog]
* [A generic method for copying backup packages for migration or disaster recovery](
https://communities.sas.com/t5/SAS-Communities-Library/A-generic-method-for-copying-backup-packages-for-migration-or/ta-p/765158) [Blog]
* [Retaining your SAS Viya Backup](
https://communities.sas.com/t5/SAS-Communities-Library/Retaining-your-SAS-Viya-Backup/ta-p/845138) [Blog]
[Selective backup and restore of SAS Viya Content](https://communities.sas.com/t5/SAS-Communities-Library/Selective-backup-and-restore-of-SAS-Viya-Content/ta-p/968018) [Blog]

See Also:

* [Test the Process to Restore From Backups](./test_restore_process.md) [Task]


[Back to checklist](../checklist.md)
