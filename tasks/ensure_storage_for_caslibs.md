![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Ensure You Have Provided Sufficient Storage for Path-Based Caslibs

<!--
SortString: 0080
Description: Ensure you have provided sufficient filesystem storage of an appropriate type for path-based caslibs.
Tags: Initial,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern,Michael Erickson
-->
When: Pre-install, post-install, and after platform changes.

## Ensure you have provided sufficient filesystem storage of an appropriate type for path-based caslibs.

Users will store data in the Public caslib unless you alter its permissions to prevent them from doing so. You should allocate sufficient disk space to the volume backing the Public and other caslibs to ensure they do not run out of space. Ensure the size and type of storage provided are suitable and appropriately optimized. You may need to create new persistent volumes or shared drives, and use overlays as described in [Mount hostPaths and Data Connectors for the CAS Server](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm#p04621fwoqi0k2n1cls8yhrx7ksb).

You might require expert support or advice to get optimal results from the sizing, selection, and configuration of this storage and to allow for its size to change in the future. Your SAS architect and Kubernetes administrator can assist you with this.

[Back to checklist](../checklist.md)