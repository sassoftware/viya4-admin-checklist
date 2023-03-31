![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Define Library Connection Data Sources as a Resource in SAS Programming Run-Time Contexts

<!--
SortString: 0390
Description: Compute, Connect and Batch contexts can be associated with Required Resources, the first of which is a Library Connection.
Tags: Initial,New,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
-->
When: After platform changes

Compute, Connect and Batch contexts can be associated with Required Resources, such as a Library Connection.

For the main checklist task describing Compute, Connect and Batch contexts, see [Modify Launcher and SAS Programming Run-Time Server Contexts](./modify_programming_launcher_server_contexts.md) [Task].

## Required Resources

A feature available in SAS Viya 2022.1.3 and later allows SAS Administrators to define Library Connections (also called 'Connections to Data Sources' or 'Data Source Definitions') with the 'Allow all users to view the library connection' option selected. If this option is selected for a Library Connection resource, it is associated with the current compute context as a 'Resource', and will be declared for all compute sessions started under that compute context.

There is a place in SAS/CONNECT contexts and SAS Batch Contexts to specify required resources too.

See Gerry Nelson's SAS Communities library post: [Managing Connections to Data Sources for Compute sessions in SAS Viya](https://communities.sas.com/t5/SAS-Communities-Library/Managing-Connections-to-Data-Sources-and-SAS-Libraries-for/ta-p/825138) [Blog].

Other types of resources associated with contexts may be added in future releases of SAS Viya.

[Back to checklist](../checklist.md)