![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Monitor Compute Sessions

<!--
SortString: 0660
Description: Use the sas-viya CLI, log and metric monitoring tools to monitor compute sessions
Tags: Regular,New,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
Frequency: Daily or as often as necessary
-->
When: Daily

SAS Administrators should be able to see:

1. Who is running [SAS Compute Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00001viyaprgmsrvs00000admin.htm)
sessions
1. What resources they are consuming, and
1. Whether this use is in line with expectations.

If you do not have [SAS Enterprise Session Monitor](https://www.sas.com/en_us/software/enterprise-session-monitor.html),
monitoring compute (and connect and batch) sessions in SAS Viya is still possible,
but it takes a little effort. You are mostly limited to seeing pod-level and container-level
metrics, once you have identified the pod from log messages. Identifying the pod
is much easier when you have a good log monitoring application, such as
OpenSearch and OpenSearch Dashboards which provide the log monitoring solution in
SAS Viya Monitoring for Kubernetes. Other good Kubernetes log monitoring solutions
should provide similar capability. See [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task] and [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task].

Alternatively, the version of [SAS Enterprise Session Monitor](https://www.sas.com/en_us/software/enterprise-session-monitor.html)
for SAS Viya should make the task of monitoring compute sessions significantly
easier. It has an additional license fee.

## Who is running SAS Compute Server sessions?

The [SAS Viya CLI](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcli/n01xwtcatlinzrn1gztsglukb34a.htm)
has a compute [plug-in](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcli/n1vth8mtb8ipprn1prz5j26p3nvc.htm)
which can list currently-running Compute sessions. For example, assuming you
have already defined a connection profile and authenticated against your SAS
Viya deployment:

```sh
sas-viya compute sessions list
```

Example results when three user sessions are running:

```log
[user@host ~]$ sas-viya compute sessions list
Compute context sessions:
1.  315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000 idle Delilah
2.  c469c7f4-d29b-4ad0-a35d-641b07168ade-ses0000 idle Henrik
3.  623b523b-ed5d-460f-ade7-fe312b5f1c49-ses0000 idle geladm
```

> **Tip**: As with all SAS Viya CLI commands, adding `-h` to the command tells
> it to output context-specific help.

## Which pods are the compute servers hosting those compute sessions running in?

### Find logs for the compute session in your log monitoring tool

The compute session IDs listed in the `compute sessions list` command's output
are potentially useful for correlation with log documents. The session ID shown
in the first output column of the above results appears in numerous log messages
from logsource 'compsrv' which seem to mostly relate to GET and PUT requests.

Here are some example messages from logsource 'compsrv' featuring the example session ID above:

```log
...
Request  [00000010] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/filerefs/_keepalv
Request  [00000008] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/filerefs?limit=100
Request  [00000007] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/data?limit=100
Request  [00000006] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/variables?filter=in(name,'SYSHOSTNAME','SYSVER','SYSVLONG','SYSHOSTINFOLONG','_GITVERSION')
Request  [00000005] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/jobs/1016D580-53C9-974F-89F4-F60AA76057EB/state?wait=30
Request  [00000004] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/jobs/1016D580-53C9-974F-89F4-F60AA76057EB/state
Request  [00000003] >> POST /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/jobs
Request  [00000002] >> GET /compute/sessions/315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000/state
...
```

Those log messages are produced by the SAS Compute Server pod which actually
runs the SAS code. It is this pod whose performance you are most likely to
want to monitor, since it is doing the actual work.

### Find the Pod name

Having found a log document which contains a message with a matching session ID,
your log monitoring application should be able to show you the **name of the Pod**
in which that message was found.

For example, in OpenSearch Dashboards, you can either add the `kube.pod` column
to the table, or expand one of the log documents which contain the session ID
string, and find the value of the log document's `kube.pod` attribute. This
`kube.pod` attribute is not present in the raw kubernetes logs, it is added by
the Fluent Bit agent running on each node.

> **Note**: You may also see some more human-readable messages from logsource
'sas-compute', for example:
>
> ```log
> A session with the ID "315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000" has been created for the context with the ID "8db09547-1b77-40cf-8276-fcb89a768a0c" on the server with the ID "315a2ca8-f4d6-4110-a310-cd904960bb29".
> ```
>
> These messages are from the always-running SAS Compute **Service**, logsource
> 'sas-compute' (not to be confused with an individual temporary SAS Compute **Server**).
> The SAS Compute Service runs all the time, and acts as a broker which client
> applications like SAS Studio can call to request a compute session. If SAS Workload
> Management is not deployed, the Compute Service then calls the Launcher Service
> which starts the Compute Server pod to run the compute session. If SAS
> Workload Management is deployed, it starts the Compute Server pods.
>
> But the point, in the context of monitoring compute servers and sessions,
> is that you should not expect to see much CPU being used by the compute
> service, since it an intermediary, and does not actually execute the SAS code.

### Alternative: Show the pod name in a SAS log message

You can also add a statement to the global compute server autoexec code, or to a
specific compute context's autoexec code, or to an individual SAS program
which writes out the compute session ID and owner, and the 'host' compute server
pod name to the logs:

```sas
%put &SYS_COMPUTE_SESSION_ID;
%put &SYS_COMPUTE_SESSION_OWNER;
%put &_SASHOSTNAME;
```

Example output:

```log
...
80   %put &SYS_COMPUTE_SESSION_ID;
315a2ca8-f4d6-4110-a310-cd904960bb29-ses0000
81   %put &SYS_COMPUTE_SESSION_OWNER;
Delilah
82   %put &_SASHOSTNAME;
sas-compute-server-9b3a1272-0a84-450b-ad33-f4dc7c00c347-tzgfh
...
```

Normally only one SAS session at a time runs in a `sas-compute-server` pod.

## Monitor resource use for a Compute Server pod

Once you have identified the name of a Pod you wish to monitor, you can use your
metric monitoring tools to see the resources used by that pod, including CPU,
memory, network and disk I/O metrics.

If you are not concerned with a specific compute session, but rather want an
overview of all running compute sessions, you can get this by searching for pods
named beginning with `sas-compute-server-`. For connect sessions, pods names
begin with `sas-connect-server-`, and batch server pod names begin `sas-batch-server-`.

See also: [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task] and [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task].

### Monitor compute sessions in SAS Enterprise Session Monitor

[SAS Enterprise Session Monitor](https://www.sas.com/en_us/software/enterprise-session-monitor.html)
is available for SAS Viya. It has an additional license cost. You can
[deploy it](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n13f1d2tegzls6n1vuivngtqyph7.htm)
after deploying SAS Viya.

SAS Enterprise Session Monitor is different from any other metric monitoring
tool, because is designed specifically for monitoring workload at the SAS
*session* level, something which non-SAS tools are unlikely to know about.
Other Kubernetes monitoring tools are limited to reporting container or
pod-level metrics for user workload, or node-level and namespace-level metrics for
an overview of workload on nodes in the compute node pool.

### Monitor compute sessions in SAS Viya Monitoring for Kubernetes, or any other metric monitoring tool

If you have deployed [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes)'
metric monitoring stack, the Grafana dashboard 'General / Kubernetes / Compute
Resources / Pod' can show the pod's CPU and memory usage, requests and limits
over time, together with the pod's network bandwidth, storage I/O usage, and a
few other metrics.

For an overview of compute sessions, try the 'General / Kubernetes /
Compute Resources / Namespace (Pods)' dashboard in Grafana. This dashboard would
allow you to select more than one sas-compute-server, sas-connect-server or
sas-batch-server pod at a time, to see the performance metrics over time for
multiple pods together.

If you have [SAS Workload Management](https://www.sas.com/en_us/software/workload-management.html)
licensed and deployed, you can use the 'SAS Launched Jobs - Node Activity' and
'SAS Launched Jobs - User Activity' Grafana dashboards shipped with the project,
for monitoring launched jobs node and user activity, but these dashboards only
show data from SAS Workload Management, and have no data to show without that product.

Both **Lens** and **OpenLens** have good tools for monitoring pod metrics. See
the Workload > Pod pages in either tool, and filter by namespace and pod name.

If you have another metric monitoring tool deployed and configured for
monitoring your SAS Viya deployment, follow the instructions you have for that
monitoring tool to view SAS Viya pod metrics.

### Pod vs Container Metrics

If there is more
than one running container, you can see metrics for each individual container in
the pod with such a tool too. However, by default there is only one running
container in a compute server pod after it has finished initializing, called
`sas-programming-environment`, so for practical purposes during most of its
lifetime the compute server pod metrics and container metrics are essentially
the same.

See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Monitor Memory, CPU, Network, and Disk Throughput Usage](./monitor_usage.md) [Task]

## Other useful information about compute sessions available in SAS macro variables

Other automatic global SAS macro variables which can be useful for monitoring,
investigation and troubleshooting include:

```sas
%put &_CLIENTAPP;
%put &_CLIENTUSERID;
%put &_CLIENTUSERNAME;
%put &_USERHOME;
%put &SYSUSERID;
%put &SYSVIYARELEASE;
%put &SYSVIYAVERSION;
```

See all automatic and global macro variables by running:

```sas
%put &_all_;
```

[Back to checklist](../checklist.md)