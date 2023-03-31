![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Understand how to Check the Status of Services

<!--
SortString: 0210
Description: Ensure you know how to check the status of all SAS Viya services ad hoc at any time
Tags: Initial,Legacy,Done
Topic: Observability
Essential: -
Authors: David Stern,Michael Erickson
-->
When: After platform changes

See Also: [Check the Status of SAS Services](check_service_status.md)

## Ensure you know how to check the status of all SAS Viya servers ad hoc at any time

Know how to check whether all your SAS Viya services are running, by looking at the result of one or more tests of the services' health.

It can also be helpful to look at the health of the SAS Viya pods which host those services.

Example tools to use for these checks include:

* The status and logs of the SAS Readiness pod. See [Assessing SAS Viya Readiness](https://communities.sas.com/t5/SAS-Communities-Library/Assessing-SAS-Viya-Readiness/ta-p/723203) [Blog].
* The kubernetes CLI, [kubectl](https://kubernetes.io/docs/reference/kubectl/) [Doc], e.g. `kubectl get svc`, `kubectl get pod` and variations which filter the results of those
  * Exec-ing into pods to see what processes are running in them, e.g.:
    * `kubectl exec -it $(kubectl get pod -l launcher.sas.com/username=some_username --output=jsonpath={.items..metadata.name} ) -- some_bash_command` where some_username is the name of a user who has launched a SAS Compute Server running a SAS Compute session, and some_bash_command is a command like `top`, or `ps -ef` which can reveal something about processes running inside the pod. Here is that command to look at the top-CPU-consuming processes inside a compute server pod, for a user called geladm:</br>`kubectl exec -it $(kubectl get pod -l launcher.sas.com/username=geladm --output=jsonpath={.items..metadata.name} ) -- top`
* [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes) [App] includes Grafana dashboards which give some insight into the status of services, pods and nodes on your SAS Viya platform. See also the documentation pages for this project in SAS's Help Center: [About SAS Viya Monitoring for Kubernetes](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/n0bzfdp3bn6p4vn1lj9pm2hy8t0q.htm?fromDefault=) [Doc]
* [Lens](https://k8slens.dev/) [App], [OpenLens](https://github.com/MuhammedKalkan/OpenLens) [App], or [K9s](https://k9scli.io/) [App]
* Observability tools provided by your cloud provider. See [Monitoring and Logging on Cloud-Provider Platforms](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/n0lzjee544jib9n1dj4wc0fhuc36.htm) [Doc]
* SAS Environment Manager includes a Servers page which can indicate the status of CAS servers.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Check the Status of SAS Services](./check_service_status.md) [Task]

[Back to checklist](../checklist.md)