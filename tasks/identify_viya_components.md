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

* A **service**: This is arguably the most useful unit for counting components in a SAS Viya deployment. A SAS Viya deployment may have over 150 services (in the Kubernetes networking meaning of the term), though because some pods host multiple services, there are more services than pods.
* A **pod**: A SAS Viya deployment typically has over 100 Kubernetes pods that run continuously, plus some shorter-lived pods which run servers such as those started for SAS Programming Run-time sessions, plus short lived pods which run other types of Kubernetes jobs and tasks (backups, imports migrations etc.).
* A **container**: In addition to their main container(s), the practically all SAS Viya pods have two or more init containers; these are containers which run for a short time to perform some initialization when the pod starts, and stop running once they have done their work. A significant minority of SAS Viya pods also have more than one running container throughout their whole lifetime, even after the pod has completed its initialization.

If you are able to, review the list of Kubernetes services defined for your SAS Viya deployment's namespace. You may see some or all of the following services - the list below is only a selection:

* `sas-analytics-*` services (multiple)
* `sas-arke` - a message broker proxy
* `sas-authorization` - provides general authorization (permissions)
* `sas-batch` - a front-end to enable other services to run SAS code in batch or in line mode
* `sas-cas-*` services (multiple) - SAS Cloud Analytics Server(s) and supporting services
* `sas-compute` - the SAS Compute Server which provides a front-end API to enable other services to run SAS code interactively
* `sas-configuration` and `sas-consul-server` - the [SAS Configuration Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00000sasconfigdata0000admin.htm?fromDefault=), based on Hashicorp Consul
* `sas-connect` services (two) - provides SAS/CONNECT support
* `sas-crunchy-*` (multiple) if deployed is the PostgreSQL database used by [SAS Infrastructure Data Server (Platform PostgreSQL)](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/n00000sasinfrdatasrv000admin.htm?fromDefault=). If you don't see services with this name, it is probably because you are using another instance of Postgres hosted by your Cloud Provider (e.g. AWS, Azure, GCP) or running separately in OpenShift.
* `sas-data-mining-*` and other `sas-data-*` services (multiple)
* `sas-files` provides file handling and storage APIs - in common with many other services, the actual file metadata and content is stored in the SAS Infrastructure Data Server
* `sas-folders` supports the folder structure you see in several SAS Viya applications including SAS Environment Manager, SAS Drive etc.
* `sas-gen-ai-gateway` - supports generative AI integration for [SAS Viya Copilot](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p01y7i47bsmr8dn153kufzh7mia6.htm) [Doc]
* `sas-identities` manages users and groups from an LDAP or SCIM source, and also manages custom groups
* `sas-information-catalog-app` provides the web interface for SAS Information Catalog
* `sas-job-*` services provide capabilities for scheduling and running SAS and OS jobs and job flows, including SAS Job Execution Server
* `sas-landing-app` - the landing page for a SAS Viya deployment
* `sas-launcher` is a key part of the SAS Programming Run-Time, which is called by the sas-compute, sas-batch and sas-connect services, and which starts compute, batch and connect servers which actually execute SAS code
* `sas-logon-app` is the service you use when you sign in to SAS Viya, through OIDC single sign-on or by entering a username and password
* `sas-microanalytics-score` is the MAS engine, used for near real-time decision and scoring in Internet of Things (IOT) and other applications
* `sas-model-*` services provide model development, management and storage capabilities
* `sas-opendistro` is an instance of Open Distro for ElasticSearch, used for unstructured data and text analytics
* `sas-readiness` periodically polls other services in SAS Viya to see if they are responsive
* `sas-redis-server` - [SAS Redis Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvinf/p07zdbfbdi338nn13a37u396on0x.htm) - distributed cache server
* `sas-report-*` services are used in SAS Visual Analytics, and elsewhere
* `sas-scheduler` is used scheduling system- and user-defined jobs
* `sas-studio-app` runs SAS Studio
* `sas-transfer` is an important service for uploading and downloading contents for package export and import, migrations etc.
* `sas-visual-analyics` is the SAS Visual Analytics application
* `sas-workflow-*` services support the SAS Viya platform's workflow management capability
* `sas-workload-orchestrator-*` (multiple) provide SAS Workload Management and orchestration capability and the functionality behind the Workload Orchestrator page in SAS Environment Manager

## Useful tools for seeing SAS Viya components

* [SAS Viya Environment Manager](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/titlepage.htm?fromDefault=) [Doc]
    * View details of your SAS Viya license and the products included in your order from the SAS Environment Manager > Licensed Products page.
* [Lens](https://k8slens.dev/), [Freelens](https://freelensapp.github.io/) [Applications], graphical UIs for managing Kubernetes clusters
* [k9s](https://k9scli.io/), a terminal based UI to interact with your Kubernetes clusters
* The [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) command-line interface [Doc]

See also: SAS Viya Platform: Overview > [Introduction to the SAS Viya Platform](https://go.documentation.sas.com/doc/en/sasadmincdc/default/viyaov/n00000sasviya000architecture.htm) in the SAS Viya Platform Administration guide [Doc]

[Back to checklist](../checklist.md)
