![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Consider relocating CAS_DISK_CACHE

<!--
SortString: 0330
Description: Relocate the CAS_DISK_CACHE for CAS servers
Tags: Initial,New,Done
Topic: CAS
Essential: -
Authors: Scott McCauley
-->
When: After deployment

The CAS server uses the directory or directories referred to as the CAS Disk Cache as a scratch area. It is associated with the environment variable CASENV_CAS_DISK_CACHE and has two primary purposes:

1. As data is loaded into memory, it is organized in blocks. Each time a block reaches the default block size of 16Mb, the block is copied to the CAS Disk Cache. The copied block can be re-read back into memory quickly if memory use becomes high and the original data must be freed from memory.
1. For a distributed CAS server (MPP), copies of the blocks are transferred to CAS worker pod for fault tolerance. Those copies are also stored in the CAS Disk Cache of the receiving CAS Worker.

A secondary use of the cache is for files that are uploaded to the server. By default, a copy of the file is temporarily stored on the CAS controller in its CAS Disk Cache.

For a more practical discussion of when the CAS_DISK_CACHE is used see [When is CAS_DISK_CACHE used?](https://communities.sas.com/t5/SAS-Communities-Library/When-is-CAS-DISK-CACHE-used/ta-p/631010?search-action-id=91636799068&search-result-uid=631010)

By default, the server is configured to use a directory that is named `/cas/cache` on each controller and worker pod. This directory is provisioned as a Kubernetes emptyDir and uses disk space from the root volume of the Kubernetes node.

The default configuration is acceptable for testing and evaluation, but not for production workloads. If disk space in the root volume of the node becomes low, then Kubernetes begins evicting pods and the pod is unlikely to be rescheduled.

To provision your CAS servers for production use, you should consider relocating the CAS_DISK_CACHE to a larger and possibly better performant location.

Primary resources:

* [SAS Viya Platform Operations: Tune CAS_DISK_CACHE](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm?fromDefault=#p0wtwirnp4uayln19psyon1rkkr9) [Doc]
* [Provisioning CAS_DISK_CACHE for SAS Viya](https://communities.sas.com/t5/SAS-Communities-Library/Provisioning-CAS-DISK-CACHE-for-SAS-Viya/ta-p/603689) [Blog]


See Also:

* [When is CAS_DISK_CACHE used?](https://communities.sas.com/t5/SAS-Communities-Library/When-is-CAS-DISK-CACHE-used/ta-p/631010?search-action-id=91636799068&search-result-uid=631010) [Blog]
* [A New Tool to Monitor CAS_DISK_CACHE Usage](https://communities.sas.com/t5/SAS-Communities-Library/A-New-Tool-to-Monitor-CAS-DISK-CACHE-Usage/ta-p/635320) [Blog]
* [Performance Tuning for the SAS Viya Platform](https://communities.sas.com/t5/SAS-Communities-Library/Performance-Tuning-for-the-SAS-Viya-Platform/ta-p/864106) [Blog]

[Back to checklist](../checklist.md)