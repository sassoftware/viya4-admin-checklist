![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Renew your SAS Viya License

<!--
SortString: 0460
Description: Obtain and apply a new SAS Viya platform license before your existing license expires
Tags: Regular,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Ajmal Farzam
Frequency: Annually
-->
When: Before your license expires

Usage of SAS Viya software is controlled by a license file. The license is deployed at the time of initial deployment. When upgrading your platform to a new cadence version, you are required to download new deployment assets, which will contain a new license. It may ocassionally be necessary to renew the license outside of the update process; for example, when adding or removing products from your SAS order, or when you wish to extend expiration dates on existing products without updating your platform to a new version.

Deployment assets from my.sas.com include a license file in JWT format. Licenses can also be downloaded separately from the portal.

License updates require changes to your Kubernetes cluster, and elevated cluster permissions are therefore required.

Product expiration dates can be queried using the [SAS Viya CLI](https://documentation.sas.com/doc/en/sasadmincdc/default/callicense/p1xwu0rnjoktmon1f8zukzv1n7f6.htm?fromDefault=) [Doc] or using [SAS Environment Manager](https://documentation.sas.com/doc/en/sasadmincdc/default/evfun/p0lrqikrv31620n1eo3wzh4ydajk.htm) [Doc].

To apply a new license, follow the documented [instructions](https://documentation.sas.com/doc/en/sasadmincdc/default/callicense/n14rkqa3cycmd0n1ub50k47x7lbb.htm) corresponding to the method you used to originally deploy your software.

[Back to checklist](../checklist.md)