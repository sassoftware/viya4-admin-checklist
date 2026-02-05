![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure SAS Workload Management

<!--
SortString: 0285
Description: Configure SAS Workload Management
Tags: Initial,New,Done
Topic: SAS Administration
Essential: -
Authors: Ajmal Farzam
-->
When: Initial

SAS Workload Management is enabled by default in new SAS Viya deployments. 

It deploys a 'SAS Workload Orchestrator' component, which provides priority-based queues and advanced scheduling beyond standard Kubernetes, enabling control over job prioritization, resource allocation, and host placement for SAS Viya compute workloads.

With SAS Workload Management enabled, all SAS Compute workloads are sent to the SAS Workload Orchestrator using queues, and are then processed on appropriate nodes as per the configuration. By default, a 'default' queue is provided out-of-the-box, which enables workload orchestration to be leveraged immediately, provided the following conditions are true: 
* At least [one node is labeled](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/p0uuf92gtvxc07n1aikt2s6edz5u.htm#n02uiykco66q9en1ks9lydy8qeml) `workload.sas.com/class=compute`.
* Confirm [ClusterRoles and ClusterRoleBindings](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/p0uuf92gtvxc07n1aikt2s6edz5u.htm#p1xsnqltew06pqn144sf1wfxj816) are applied for accurate node resource visibility. 



## Planning and Implementation
* Review if your environment needs additional custom queues for workload separation (e.g. production vs. batch) or if default scheduling suffices. Configure the following settings as required:
  * queue priorities
  * preemption rules
  * resource requirements
  * resource limits
  * resource compare orders
  * queue users and groups
  * queue administrators
  * auto-scaling rules (for [integration with Kubernetes Cluster Autoscaler](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/n1s5vpyfr4sq3zn1i1dp1aotpzka.htm))
* Inventory workloads, users/groups, and SLAs to map to queues (e.g. high-priority for interactive sessions).
* Identify node pools and labels for custom host types (e.g. GPU nodes, large-memory hosts) for processing specific types of workloads.
* If desired, associate queues to contexts (and create new contexts if required). 
* If migration from an LSF configuration on SAS 9, review [additional considerations](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/p12vqiguvi5woxn1j77lxxy2b4ba.htm). 

Administrators can use [SAS Environment Manager's dedicated *Workload Orchestrator* area](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/p1m8w647qfyrw3n186on4zeiqugg.htm) or the [sas-viya CLI's *workload-orchestrator* plug-in](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/n13qr6sgz64wspn1nd1l5e3wczxj.htm) to modify configuration settings. 

## Monitoring
Set up and utilize monitoring tools and features to ensure SAS Workload Orchestrator is operating as expected and to identify bottlenecks early.

* Monitor jobs, queues, hosts, logs using SAS Environment Manager or using the CLI plug-in. ​Key metrics include queue wait times, job states (pending/running), host utilization, and preemption events.
* Adjust log levels to troubleshoot issues (e.g. pending jobs, restarts).
* Review dedicated [Grafana dashboards](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/p0fv84e6amqsfun1uvfwnh0oevhw.htm) deployed with [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes/tree/main/monitoring), including *SAS Launched Jobs - Node Activity* and *SAS Launched Jobs - User Activity*, which allow filtering by queue, job type, and user for Workload Orchestrator-specific metrics
​


See also:
* [SAS Viya Platform Administration: Workload Management](https://go.documentation.sas.com/doc/en/sasadmincdc/default/wrkldmgmt/titlepage.htm) [Doc]
* [SAS Workload Management](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Workload-Management/ta-p/788892) [Blog]
* [SAS Workload Management on SAS Viya: Deployment Architecture](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Workload-Management-on-SAS-Viya-Deployment-Architecture/ta-p/789816) [Blog]
* [SAS Workload Orchestrator - Associate Kubernetes Cluster Nodes With Queues](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Workload-Orchestrator-Associate-Kubernetes-Cluster-Nodes/ta-p/902538) [Blog]
* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Compute Sessions](./monitor_compute_sessions.md) [Task]

[Back to checklist](../checklist.md)
