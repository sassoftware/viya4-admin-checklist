![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Set location for SAS Work and other Programming Run-Time Temporary Files

<!--
SortString: 0360
Description: Move SAS Work and other Programming Run-Time Temporary Files to a better location than the default
Tags: Initial,Legacy,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
-->
When: After platform changes

## Read this excellent pair of SAS Communities posts about SAS Work

Hans Joachim-Edert has published two posts about SAS Work storage in the SAS Communities Library. They use examples in an Azure AKS deployment, but the ideas he explains apply to all SAS Viya deployments, and the posts are a fantastic explanation of the considerations.

* [Some SASWORK storage options for SAS Viya on Kubernetes](https://communities.sas.com/t5/SAS-Communities-Library/Some-SASWORK-storage-options-for-SAS-Viya-on-Kubernetes/ta-p/839275) [Blog]
* [Using generic ephemeral volumes for SASWORK storage on Azure managed Kubernetes (AKS)](https://communities.sas.com/t5/SAS-Communities-Library/Using-generic-ephemeral-volumes-for-SASWORK-storage-on-Azure/ta-p/839257) [Blog]

## SAS Programming Run-Time processes create temporary files

During normal use, SAS Programming Run-Time processes creates temporary files in a volume named 'viya', mounted in each launched SAS Programming Run-time server pod. These temporary files are only intended to exist while the programming session is running, and intended to be deleted before the process (and the pod) terminates. These temporary files include:

* A directory for the SAS WORK library, and temporary dataset files inside it.
    > The WORK library is a core component of the SAS Programming Run-Time, for two reasons:
    > * The speed with which SAS work datasets and other files are written and read from the WORK library is a critical factor in the performance of most SAS programs.
    > * SAS work datasets can be large, and may require more storage space than the default temporary file volume has available to it.
* Files in directories named log, spool, run and tmp, depending to some extent on what SAS programming statements and procedures are run. These are less visible to SAS programmers, but they exist and should be considered alongside the files required for the SAS WORK library.

## Temporary Files are normally cleaned up automatically

When a Programming Run-Time session ends normally, the temporary files in these directories are (supposed to be) deleted, though some of the directories can remain. These directories are very small on disk, and not excessive in number. However, if a Programming Run-Time session crashes - usually a rare event - these files can be left behind and must eventually be cleaned up by a SAS Administrator to recover disk space and reduce the chance that sensitive data remains on a disk.

> NOTE: In some configurations, the temporary files are not always cleaned up, and removing them **becomes the SAS Administrator's responsability**.

At the time of writing, there is no official SAS equivalent to the [SAS 9 and SAS Viya 3 cleanwork utility](https://go.documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/hostunx/n13ozwpq7az8v6n1s77r8c2zp9d1.htm) [Doc]. You may need to make your own or use an unofficial tool someone else has created.

For both these reasons, cleaning up temporary files left behind after SAS programming run-time processes crash can be a necessary a houskeeping task for administrators looking after a SAS Viya deployment.

## Defining the location for SAS Work and other Programming Run-Time Files is an architecture task, not a SAS Administration task

If your organization will use the SAS Programming Run-Time in a way where its performance is important, then a part of the **architecture** work for the environment should be to define where these temporary files should be located for optimal SAS Programming Run-Time performance. This task is normally done before the SAS Administrator does most of their work, but SAS Administrators should know that there is a choice to be made in this aspect of host Kubernetes cluster's hardware design, and should work with the solution architects to make an optimal choice before deployment of a SAS Viya instance.

Sometimes the need to improve SAS Programming Run-Time performance or capacity by relocating these temporary files to faster or larger storage will be identified *after* initial deployment, and a *change* to the host architecture must be made to accommodate higher-performance storage for SAS Work and other Programming Run-Time temporary files. This change should consider:

* input/output performance that supports sufficiently fast sequential reads and writes, in keeping with the environment's sizing and architectural design goals
* capacity suitable for the size of temporary data sets that may be created in SAS Work
* cleanup of temporary files left-behind after programming sessions end

This is also explained in the official SAS Administration guide documentation, under [Configure External Storage Class](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n0k315nlna2awln119phkhua1na2.htm) [Doc].

## Save money by only mounting fast temporary storage for SAS Programming Run-Time Pods which need it

Faster storage is quite a lot more expensive than cheaper storage. If all your SAS Programming Run-Time workload will be similar in size, then you can change the storage which backs your /viya volumes to whatever type is optimal for your needs, and you are done.

Most SAS deployments run a varity of SAS program workload, and only some of it really needs to have high-performance of large-capacity storage for SAS Programming Run-Time temporary files. Consider putting more than one copy of the example patchTransformer in `$deploy/sas-bases/examples/sas-programming-environment/storage/change-viya-volume-storage-class.yaml`, each of which targets a subset of your podTemplates. If you are using multiuple podTemplates, you might want a separate copy of this patchtransformer for each one. This allows you to control which podTemplates have the more expensive, fast, high-capacity storage mounted as their viya volume, and which do not. If the fast storage is only available on some Kubernetes nodes, do this in conjunction with some method to have Programming Run-time pods which need the more expensive storage to be scheduled on Kubernetes nodes where it is available.

## Set the SAS Work Path to point to alternative storage

If the alternative SAS Work Path is used only for some SAS Programming Run-Time sessions, and not all, it may be that you need to change the path for the SAS Work library from its default location.

See [Setting the SASWORK path in SAS Viya](https://communities.sas.com/t5/SAS-Communities-Library/Setting-the-SASWORK-path-in-SAS-Viya/ta-p/612432) for more on that.

## References

* Hans-Joachim Edert's SAS Communities Library post [Some SASWORK storage options for SAS Viya on Kubernetes](https://communities.sas.com/t5/SAS-Communities-Library/Some-SASWORK-storage-options-for-SAS-Viya-on-Kubernetes/ta-p/839275) [Blog]
* Hans-Joachim Edert's SAS Communities Library post [Using generic ephemeral volumes for SASWORK storage on Azure managed Kubernetes (AKS)](https://communities.sas.com/t5/SAS-Communities-Library/Using-generic-ephemeral-volumes-for-SASWORK-storage-on-Azure/ta-p/839257) [Blog]
* [Configure External Storage Class](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n0k315nlna2awln119phkhua1na2.htm) [Doc], which says to read the README file at `$deploy/sas-bases/examples/sas-programming-environment/storage/README.md` (for Markdown) or `$deploy/sas-bases/docs/sas_programming_environment_storage_tasks.htm` (for HTML).
* [SAS Viya temporary files (SASWORK and CAS Disk Cache) in Azure](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-temporary-files-SASWORK-and-CAS-Disk-Cache-in-Azure/ta-p/783581) [Blog]
* [SAS Viya Temporary Storage on Red Hat OpenShift – Part 1](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Temporary-Storage-on-Red-Hat-OpenShift-Part-1/ta-p/858834) [Blog], and [SAS Viya Temporary Storage on Red Hat OpenShift – Part 2: CAS DISK CACHE](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Temporary-Storage-on-Red-Hat-OpenShift-Part-2-CAS-DISK/ta-p/859250) [Blog]
* [Take care of your Viya storage before it takes care of you – Part 1: Planning ahead and anticipating](https://communities.sas.com/t5/SAS-Communities-Library/Take-care-of-your-Viya-storage-before-it-takes-care-of-you-Part/ta-p/815886) [Blog]
* SAS Viya Platform Administration > Tuning > Tuning Programming Resources and Programs > [Storage for Programming Pods](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/n1d39n9afq8a5un17r94wj63u1up.htm#p1jxvhyy4vao3bn1g4t0ez8imawh) [Doc]

[Back to checklist](../checklist.md)