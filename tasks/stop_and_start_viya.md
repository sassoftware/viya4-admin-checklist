![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Stop and Start SAS Viya software

<!--
SortString: 0620
Description: Ensure you can scale your SAS Viya deployment to zero, and that you can scale it back up when needed again.
Tags: Regular,Legacy,Done
Topic: SAS Administration
Essential: -
Authors: Ajmal Farzam
Frequency: When not in use
-->
When: After platform changes

It may occasionally be necessary to stop and restart your SAS Viya deployment; for example, to reduce running costs when the deployment is not being used. Some configuration changes and updates may also require one or more resources to be restarted.

Ensure you scale your SAS Viya deployment to use minimal or zero resources when they are not needed, and that you can scale them back up when they are needed again. Also verify that SAS Viya pods can automatically be restarted when required.

Note that restarting or stopping your SAS Viya deployment causes a disruption, which may temporarily impact end-users' ability to use the SAS Viya platform.

* A specific service can be restarted by [deleting its pod](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calchkadm/n00003ongoingtasks00000admin.htm) [Doc]. A new pod will start in its place.

* To stop a specific service without automatically restarting it, its deployment should be [scaled to zero](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calchkadm/n00003ongoingtasks00000admin.htm) [Doc].

* To start a stopped service, scale its deployment back to one replica (the default setting). If you wish to scale up to more than one replica, the recommended approach is to modify the default [Horizontal Pod Autoscaler settings](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm?fromDefault=#n14iqy05lb736yn1e01m2hmzu1xr) [Doc].

SAS provides Kubernetes CronJobs that can perform the scale up/down operations to gracefully start or stop the entire Viya deployment. Administrators can [schedule these jobs](https://communities.sas.com/t5/SAS-Communities-Library/Scheduling-Start-and-Stop-Jobs-for-SAS-Viya/ta-p/759037) [Blog] to run on at regular intervals (they are suspended by default) or they can be used to create new ad-hoc jobs to start and stop the deployment on demand.

The two jobs are named `sas-stop-all` and `sas-start-all`. For ad-hoc stopping or starting, [create a new job](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calchkadm/p17xfmmjjkma1dn1b5dcx3e5ejxq.htm#p0butgo7gtfyi0n14umtfv0voydt) [Doc] (with a unique job name) from the corresponding source cronjob. The job will run immediately to stop/start your SAS Viya deployment.

Refer to [Check the Status of SAS Services](check_service_status.md) to verify that your Viya software has been started or stopped.

See also:
* [Scheduling Start and Stop Jobs for SAS Viya](https://communities.sas.com/t5/SAS-Communities-Library/Scheduling-Start-and-Stop-Jobs-for-SAS-Viya/ta-p/759037) [Doc]
* [Stop and Start SAS Viya's Monitoring and Logging components](./stop_and_start_sas_viya_monitoring_for_kubernetes.md) [Task]

[Back to checklist](../checklist.md)