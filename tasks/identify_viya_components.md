![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Identify Components of SAS and Third-Party Software

<!--
SortString: 0270
Description: Ensure you can identify the components of SAS and third-party software that make up SAS Viya
Tags: Initial,Legacy,Done
Topic: SAS Administration
Essential: -
Authors: David Stern,Michael Erickson
-->
When: After platform changes

## Ensure you can identify the components of SAS and third-party software that make up SAS Viya

SAS Viya deployments contain many components, most of which are part of the SAS software, but sometimes third-party components can be deployed too. By 'component', we may mean:

* A **service**: This is arguably the most useful unit for counting components in a SAS Viya deployment. A SAS Viya deployment may have well over 100 services - some pods host multiple services, so there are typically more running services than pods.
* A **pod**: A SAS Viya deployment typically has well over 100 Kubernetes pods that run continuously, some shorter-lived servers such as those started for SAS Programming Run-time sessions, plus short lived pods which run Kubernetes jobs.
* A **container**: In addition to their main container(s), the practically all SAS Viya pods have two or more init containers; these are containers which run for a short time to perform some initialization when the pod starts, and stop running once they have done their work. A significant minority of SAS Viya pods also have more than one running container throughout their whole lifetime, even after the pod has completed its initialization.

If you are able to, review the list of Kubernetes services defined for your SAS Viya deployment's namespace. You may see some or all of the following services - the list below is only a selection:

* `sas-analytics-*` services (multiple)
* `sas-authorization` - provides general authorization (permissions)
* `sas-batch` - a front-end API to enable other services to run SAS code in batch or in line mode
* `sas-cacheserver`, `sas-cashlocator` - [SAS Cache Locator and Cache Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00001viyainfrsrvs00000admin.htm)
* `sas-cas-*` services (multiple) - SAS Cloud Analytics Server(s) and supporting services
* `sas-compute` - the SAS Compute Server which provides a front-end API to enable other services to run SAS code interactively
* `sas-connect` services (two) - provides SAS/CONNECT support
* `sas-consul-server` - engine for the [SAS Configuration Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00000sasconfigdata0000admin.htm), running Hashicorp Consul
* `sas-crunchy-data-*` (multiple) if deployed is the PostgreSQL database used by [SAS Infrastructure Data Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00000sasinfrdatasrv000admin.htm). If you don't see services with this name, it is probably because you are using another instance of Postgres hosted by your Cloud Provider (e.g. AWS, Azure, GCP) or running separately in OpenShift.
* `sas-data-mining-*` and other `sas-data-*` services (multiple)
* `sas-files` provides file handling and storage APIs - actual file metadata and content is stored in the SAS Infrastructure Data Server, in common with many other services
* `sas-folders` supports the folder structure you see in several SAS Viya applications including SAS Environment Manager, SAS Drive etc.
* `sas-identities` manages users and groups from an LDAP or SCIM source, and also manages custom groups
* `sas-job-*` services provide capabilities for scheduling and running SAS and OS jobs and job flows
* `sas-launcher` is a key part of the SAS Programming Run-Time, which is called by the sas-compute, sas-batch and sas-connect services, and which starts compute, batch and connect servers which actually execute SAS code
* `sas-logon-app` is the service you use when you sign in to SAS Viya, through OIDC single sign-on or by entering a username and password
* `sas-microanalytics-score` is the MAS engine, used for near real-time decision and scoring in IOT applications
* `sas-model-*` services provide model development, management and storage capabilities
* `sas-opendistro` is an instance of Open Distro for ElasticSearch, used for unstructured data and text analytics
* `sas-reports-*` services are used in SAS Visual Analytics, and elsewhere
* `sas-scheduler` is used scheduling system- and user-defined jobs
* `sas-studio-app` runs all editions of SAS Studio
* `sas-transfer` is an important service for uploading and downloading contents for package export and import, migrations etc.
* `sas-visual-analyics` is the SAS Visual Analytics application
* `sas-workflow-*` services support the SAS Viya platform's workflow management capability

## Useful tools for seeing SAS Viya components

* [SAS Viya Environment Manager](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/titlepage.htm?fromDefault=) [Doc]
    * View details of your SAS Viya license and the products included in your order from the SAS Environment Manager > Licensed Products page.
* [Lens](https://k8slens.dev/) or [OpenLens](https://github.com/MuhammedKalkan/OpenLens) [Applications]
* The [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) command-line interface [Doc]

See also: SAS Viya Platform: Overview > [Introduction to the SAS Viya Platform](https://go.documentation.sas.com/doc/en/sasadmincdc/default/viyaov/n00000sasviya000architecture.htm) in the SAS Viya platform administration guide [Doc]

[Back to checklist](../checklist.md)
