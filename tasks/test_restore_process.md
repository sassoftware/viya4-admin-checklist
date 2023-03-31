![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Test the Process to Restore From Backups

<!--
SortString: 0640
Description: Periodically test the process to restore from backups
Tags: Regular,Legacy,Done
Topic: SAS Administration
Essential: -
Authors: Gerry Nelson
Frequency: Monthly
-->
When: Regularly per housekeeping schedule

## Periodically test the process to restore from backups

See Also: [Backup and Restore](./backup_and_restore.md) [Task]

Backups are only useful if they can be restored. You should test backups and rehearse the procedure defined in the backup and recovery strategy to restore them. The test process should cover:

* Making the candidate backup package available for restore
* Performing an inventory scan before the restore
* Restoring the Backup
* Performing an Inventory scan after the restore
* Validating the success of the restore

> NOTE: In SAS Viya 4 you can only restore to the same Release and Cadence that a backup package was created in.

Resources:

* [Backup and Restore](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calbr/n1607whucnyc02n1eo6tbvl1tzcs.htm) [Doc]
* [A first look and Backup and Restore in SAS Viya on Kubernetes](https://communities.sas.com/t5/SAS-Communities-Library/A-first-look-and-Backup-and-Restore-in-SAS-Viya-on-Kubernetes/ta-p/740634) [Blog]
* [A generic method for copying backup packages for migration or disaster recovery](
https://communities.sas.com/t5/SAS-Communities-Library/A-generic-method-for-copying-backup-packages-for-migration-or/ta-p/765158)[Blog]
* [Retaining your SAS Viya Backup](
https://communities.sas.com/t5/SAS-Communities-Library/Retaining-your-SAS-Viya-Backup/ta-p/845138)[Blog]

See Also:

* [Backup and Restore](backup_and_restore.md)
* [Inventory Scan](inventory_scan.md)

[Back to checklist](../checklist.md)
