![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Tune the Programming Run-Time

<!--
SortString: 0440
Description: Tune the SAS Viya Platform Programming Run-time for better performance with your workload
Tags: Initial,New,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
-->
When: After platform changes

Review [Tuning Programming Resources and Programs](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/n1d39n9afq8a5un17r94wj63u1up.htm)
[Doc], and consider which of the actions it outlines may improve performance
sufficiently to justify the effort and cost, specifically for your SAS Viya deployment.

## Ways in which the SAS Viya Programming Runtime that can be tuned for performance

1. Provide **faster and/or larger capacity storage** for temporary files and datasets:
    * [Storage for Programming Pods](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/n1d39n9afq8a5un17r94wj63u1up.htm#p1jxvhyy4vao3bn1g4t0ez8imawh) [Doc]
    * [Set location for SAS Work and other Programming Run-Time Temporary Files](./move_sas_work_and_spre_temporary_files_location.md) [Task]

1. **Pre-start compute server pods**, reducing the time to start compute sessions:
    * Two other changes are prerequisites for pre-starting a pool of available compute server pods. These changes may also be useful in their own right:
        *  First, compute sessions running with a given compute context must run as a shared service account.
        *  Second, compute sessions in that same compute context must be made reusable.
    * See [Modifying Compute Resource Usage](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/n1d39n9afq8a5un17r94wj63u1up.htm#p1uaorpzhfu8jgn1sfcykyy9mg6l) [Doc] Which gives an overview of the steps, in context of the other tuning recommendations.
    * See [SAS Compute: Server, Service and Contexts: How To](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p059rp0q82tvpzn1hk9x26486do5.htm) [Doc] which details the steps for both the two pre-requisites, and for how to configure a pool of available compute servers.
    * The SAS Communities Library post [Add, update and remove compute context attributes with new pyviyatools](https://communities.sas.com/t5/SAS-Communities-Library/Add-update-and-remove-compute-context-attributes-with-new/ta-p/805531) [Blog] describes a pair of [pyviyatools](https://github.com/sassoftware/pyviyatools) [GitHub] which can help you automate these customizations.

1. Consider using **SAS Viya Compute Tasks** as a fast, lightweight way to execute short SAS programs via a single HTTP request, somewhat similar to (but not directly a replacement for) stored processes in SAS 9. Compute Tasks must run under a reusable compute context.

    * See [Work with Compute Tasks](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p059rp0q82tvpzn1hk9x26486do5.htm#p15k0mdva527esn1vvo46oowrvgf) [Doc]
    * See [Using Compute Tasks in SAS Viya: Concepts, API and Examples](https://communities.sas.com/t5/SAS-Communities-Library/Using-Compute-Tasks-in-SAS-Viya-Concepts-API-and-Examples/ta-p/976304) [Blog]

1. Pre-start **re-usable batch servers**, reducing the time to start batch jobs:
    * SAS Batch servers can be configured as reusable. See [Reusable Batch Servers](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p1jq0pjtv8azvdn1jnrm4054xjh8.htm?fromDefault=#p11zabgy12zfton1bkl20ga33jx6) [Doc]
    * See [SAS Viya High Throughput Batch Processing: Part 1 – Reusable Batch Servers](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-High-Throughput-Batch-Processing-Part-1-Reusable-Batch/ta-p/946855) [Blog]
    * See [SAS Viya High Throughput Batch Processing: Part 2 – Optimized I/O](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-High-Throughput-Batch-Processing-Part-2-Optimized-I-O/ta-p/947175) [Blog]
    * See [SAS Viya High Throughput Batch Processing: Part 3 – Performance Testing] (https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-High-Throughput-Batch-Processing-Part-3-Performance/ta-p/949393) [Blog]

1. Enable your programs to use **multithreading**, and tune thread count.
    * See [Program Options to Optimize Performance](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/n1d39n9afq8a5un17r94wj63u1up.htm#n068wr87gcls35n1f907qjqhe1vh) [Doc] and also the 'Compute Server Multithreading' section immediately below that.

1. Adjust the **CPU and memory requests and limits** for launched SAS Programming Run-time pods. See:
    * SAS Viya Platform Administration guide > Servers and Services > Programming Run-Time Environment > Programming Run-Time Servers > SAS Launcher Service > [Manage Requests and Limits for CPU and Memory](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p13s80dnwif55xn1tzhp55mrxit4.htm#n122hqrs2ddqe9n19g34jfrftz4t) [Doc] explains how to change resource requests and limits in SAS Viya configuration instances accessible to the SAS Administrator through SAS Environment manager. This is usually our preferred way to do it.
    * SAS Viya Platform Operations guide > Servers and Services > Programming Run-Time Servers > [Manage Requests and Limits for CPU and Memory](https://go.documentation.sas.com/doc/en/itopscdc/default/itopssrv/p0wvl5nf1lvyzfn16pqdgf9tybuo.htm#n0u9kbsqdgyoean1ofbds3oe4wq5) [Doc] explains how to change resource requests and limits through Kubernetes overlays, which can be a viable alternative way to do it in some situations where the Kubernetes Administrator should manage the requests and limits.
    * Though you can combine both approaches, the requests and limits set in Kubernetes overlays using the second method linked above take precedence. We recommend you do not use both methods above in the same SAS Viya deployment, as doing so could be confusing to you or other administrators.

    > **Note**: You should read both of the above sections of documentation. While they have identical section titles and discuss the same overall concept, they are quite distinct.

1. Resize your Kubernetes cluster's **Compute node pool** to better suit the CPU and memory requirements of your organization's SAS Programming Run-time pods.

    Consider working with your solution architect and Kubernetes administrator to implement a cluster autoscaler for your compute node pool, so that additional nodes are provisioned in the node pool when it is under heavy load, and unnecessary nodes are removed when under light load. See the first part of [The SAS Workload Management Approach to Autoscaling](https://communities.sas.com/t5/SAS-Communities-Library/The-SAS-Workload-Management-Approach-to-Autoscaling/ta-p/825986) [Blog] for more on this.

   As SAS Administrator, you should be prepared to provide them with information about:

   * the number of SAS compute, connect and batch sessions/pods your deployment typically runs in a given period of time
   * how long each typically runs for
   * how much CPU and memory the sessions typically use, and
   * the variations you see in each of those typical values.

   Your solution architect and Kubernetes administrator would then be more able to optimize the size of your SAS Viya platform compute node pool by:

    * Adjusting the number of nodes in the Compute node pool
    * Adjusting the size of the nodes in the Compute node pool, in terms of number of CPUs and available memory each has

    This sort of sizing should of course be performed before initial deployment. If your deployment's initial sizings were based on estimates of the workload, or your use of the SAS Viya platform has evolved since those estimates were made, then with real usage data you may be able to improve on them significantly.

See also [Performance Tuning for the SAS Viya Platform](https://communities.sas.com/t5/SAS-Communities-Library/Performance-Tuning-for-the-SAS-Viya-Platform/ta-p/864106) [Blog] and [SAS Viya Platform Administration: Tuning](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/titlepage.htm) [Doc].

[Back to checklist](../checklist.md)