![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Select Log & Metric Monitoring and Alerting Solution

<!--
SortString: 0190
Description: Choose a log and metric monitoring and alerting solution
Tags: Initial,New,Done
Topic: Observability
Essential: -
Authors: David Stern
-->
When: After platform changes

See also: [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]

Selecting, deploying or configuring and learning to use a good set of log and metric monitoring and alerting tools is **essential** for SAS Administrators. Read [Why you need a log and metric monitoring solution for the SAS Viya platform](https://communities.sas.com/t5/SAS-Communities-Library/Why-you-need-a-log-and-metric-monitoring-solution-for-the-SAS/ta-p/861725) for more on why.

Decide which of several log and metric monitoring solutions is best suited to your needs. The criteria for this decision are usually some combination of:

* How well-suited the observabilty solution is for monitoring SAS Viya deployments?
* How much configuration effort will it require to be effective, after deployment or after being enabled?
* Does your organization already have a preferred Kubernetes observability tool?
* Do you have a preference for the standard observability tool offered by your cloud hosting provider?

In the absence of other constraints, our recommended tool is [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes) [GitHub]. It is excellent for monitoring log messages and metrics, and has a usable alerting capability. See the project's excellent [documentation](https://go.documentation.sas.com/doc/en/obsrvcdc/default/obsrvdply/n0bzfdp3bn6p4vn1lj9pm2hy8t0q.htm?fromDefault=) [Doc]. It is based on open-source software components, has no license fee, and is configured and populated with dashboards that work well for monitoring SAS Viya deployments, with little or no further customization required.

Alternatively, you or your organization may prefer to use the log and metric monitoring toolsets provided by your cloud service provider. All the major cloud service providers offer their own observability tools:

* **Microsoft Azure and AKS** has [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview), comprised of [Azure Monitor Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics) and [Azure Monitor Logs](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs).
* **Amazon AWS and EKS** has [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), with [Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).
* **Google Cloud Platform and GKE** has [Google Operations Suite](https://cloud.google.com/stackdriver/docs/solutions/gke/observing), with [Cloud Logging](https://cloud.google.com/logging/docs) and [Cloud Monitoring](https://cloud.google.com/monitoring/docs).
* **OpenShift OCP** has the [OpenShift Container Platform Monitoring Stack](https://docs.openshift.com/container-platform/4.10/monitoring/monitoring-overview.html).

Many other observability tools are available, and this market seems to evolve quite rapidly. Examples include:

* [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/), and its ([GitHub repo](http://github.com/kubernetes/dashboard))
* [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/), which are the main tools in the [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes) metric monitoring stack
* [Elasticsearch and Kibana](https://www.elastic.co/kibana/), or the [OpenDistro for ElasticSearch and Kibana](https://opendistro.github.io/for-elasticsearch-docs/docs/kibana/)
* [OpenSearch and OpenSearch Dashboards](https://opensearch.org/docs/latest/dashboards/quickstart-dashboards/), which are the tools used in the [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes) log monitoring stack
* [Datadog](https://www.datadoghq.com/)
* [Logz.io](https://logz.io/blog/implementing-kubernetes-observability/)
* [Splunk](https://www.splunk.com/)

...but there are many other such tools. The important thing is to choose
*something* suitable for your needs, so that you have good visibility of
your metric and log data, and a capability to have the solution send you
alerts when conditions you specify are detected.

When you have made your choice, proceed to [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task].

In addition to this, learn about the useful (if somewhat basic) auditing
capabilities in the SAS Viya platform. See [Examine the User Activity
Report](./examine_user_activity_report.md) [Task].

[Back to checklist](../checklist.md)