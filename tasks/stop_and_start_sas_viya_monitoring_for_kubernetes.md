![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Stop and Start SAS Viya's Monitoring and Logging components

<!--
SortString: 0570
Description: Ensure you can stop the logging and monitoring solution and that you can start it back up when needed again.
Tags: Regular,New,Done
Topic: Observability
Essential: -
Authors: Ajmal Farzam
Frequency: When not in use
-->
When: When not in use

It may occasionally be necessary to stop the optional monitoring and logging components of SAS Viya; for example, to reduce running costs when the SAS Viya deployment is not being used.

Ensure you can scale any SAS Viya-specific monitoring and logging components to use minimal or zero resources when they are not needed, and that you can start them when they are needed again.

The SAS Viya Monitoring for Kubernetes framework consists of several third-party applications, which, in order to provide cluster monitoring and logging capabilities continuously, are not designed to be stopped. Administrators may however wish to stop these components to help reduce operational costs.

Stopping the SAS Viya Monitoring for Kubernetes solution requires you to remove the software components **without deleting the logging and monitoring namespaces**. This ensures that resources required when the solution is restarted (including historical logging and monitoring data) persist and can be re-used.

The recommended sequence of tasks to remove SAS Viya Monitoring for Kubernetes is:
1. Remove SAS Viya monitoring components (for each deployment)
1. Remove cluster monitoring components
1. Remove cluster logging components
Refer to the [official documentation](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/p1izwa0zvjlecxn16lx9ml75wcpl.htm#n0tot3rzd93z01n1lput5nqaxb62) for detailed instructions.

Restarting requires re-deployment of the solution using the same deployment and configuration parameters used for the initial deployment.
The recommended sequence of tasks to re-deploy SAS Viya Monitoring for Kubernetes is:
1. Deploy cluster logging components
1. Deploy cluster monitoring components
1. Deploy SAS Viya monitoring components (for each deployment)
Refer to the [official documentation](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/p1qjh2bv87waebn1svbxmw6kbbbi.htm) for detailed instructions.

After deployment, [verify that the monitoring and logging applications are accessible](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/n14kv5osqkvwf6n1a2pcwvek766z.htm).

See also: [Stop and Start SAS Viya software](./stop_and_start_viya.md)

[Back to checklist](../checklist.md)