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

> NOTE: In SAS Viya you can only restore to the same Release and Cadence that a backup package was created in.

Resources:

* [SAS Viya Backup and Restore: new features add flexibility](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Backup-and-Restore-new-features-add-flexibility/ta-p/920692)[Blog]
* [SAS Viya: Restore a Backup in 2023.10 and later](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Restore-a-Backup-in-2023-10-and-later/ta-p/906300) [Blog]
* [Restore a Viya Backup with SAS Viya Backup and Database Point in Time Restore](https://communities.sas.com/t5/SAS-Communities-Library/Restore-a-Viya-Backup-with-SAS-Viya-Backup-and-Database-Point-in/ta-p/914711)[Blog]
* [A generic method for copying backup packages for migration or disaster recovery](
https://communities.sas.com/t5/SAS-Communities-Library/A-generic-method-for-copying-backup-packages-for-migration-or/ta-p/765158) [Blog]
* [Retaining your SAS Viya Backup](
https://communities.sas.com/t5/SAS-Communities-Library/Retaining-your-SAS-Viya-Backup/ta-p/845138) [Blog]

See Also:

* [Backup and Restore](backup_and_restore.md)
* [Inventory Scan](inventory_scan.md)

[Back to checklist](../checklist.md)
