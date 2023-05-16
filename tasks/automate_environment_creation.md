![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Automate your SAS Viya Deployment Process

<!--
SortString: 0010
Description: Automate the process of creating and configuring your SAS Viya deployment
Tags: Initial,New,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern
-->
When: During deployment, post-deployment, and after platform changes

> Note: This task has significant costs. In limited circumstances, it has significant benefits. Not all customers will be able to achieve benefits from deployment automation which justify the costs.

## Create or adopt a capability to fully automate deployment of your SAS Viya environment and to configure it and provision content for business use

This capability is most valuable if it is complete and capable of being repeated easily. An automated deployment and post-deployment configuration capability is especially valuable if you have multiple SAS administrators responsible for the same deployment. It helps each administrator to more easily see and understand what they and other administrators have done to change the deployment’s configuration, which is otherwise a complex thing to describe.

It also enables any user with sufficient access to be able to re-run the deployment process, and deploy a new environment (or re-deploy an existing one) in the expected configuration state.

One way to achieve that is to create and maintain a repository of scripted or automated deployment (and pre-deployment and post-deployment) steps in a versioned source-control repository such as git.

## Create and maintain a git and document repository which together maintain a history of your SAS Viya deployment’s configuration

If you do not already have one, create a shared location where you can store:

* human readable documentation describing your SAS Viya deployment
* configuration files, provisioning, setup, deployment, configuration and management scripts used to programmatically create, deploy and manage your SAS Viya deployment

Provide authorized SAS and IT administrators, and project delivery staff working on the SAS Viya deployments in your organization with access to this shared location.

A git repository works very well for this, particularly for text-based documents. Its version history and management features support powerful use cases, such as comparing arbitrary versions of whole-project configuration to see what changed, rolling back to earlier versions in the event of an issue caused by a change and many DevOps related or automation tasks.

### Repository of documentation and references for humans

For the human readable documentation, consider using this shared location to store up-to-date architecture documents, installation checklists, post-installation documents, security models, your own internal versions of this administration checklist, and other documentation describing the structure and operation of your SAS Viya deployment. However, be aware that Git is not so efficient at storing large binary files and files that are not plain text as it is at storing plain text files, and you cannot easily use version control to compare versions of such documents.

Your human readable document repository should include a document named D30_ArchitecturePlan that might have been created for you as part of the SAS Intelligent Platform Implementation methodology.

As an administrator you are encouraged to maintain bookmarks to online versions of:

* the [SAS Viya Platform Administration Guide](https://go.documentation.sas.com/doc/en/sasadmincdc/default/sasadminwlcm/home.htm)
* the [SAS Viya Platform Deployment Guide](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/titlepage.htm?fromDefault=)
* the [SAS Viya Platform Operations Guide](https://go.documentation.sas.com/doc/en/itopscdc/default/itopswlcm/home.htm?homeOnFail)

...and to other references on the support.sas.com website for the versions of SAS Viya that you support. We also suggest SAS administrators maintain bookmarks to articles with the [Administration and Deployment](https://communities.sas.com/t5/SAS-Communities-Library/tkb-p/library/label-name/administration%20and%20deployment) label in the SAS Communities Library or articles tagged as being written by members of the [SAS Global Enablement and Learning (GEL)](https://communities.sas.com/t5/tag/GEL/tg-p/board-id/library) team.

## Consider automating some or all of the following:

* Obtaining license files and software orders
* Provisioning virtual hardware and deploy supporting services like Docker and Kubernetes e.g through Terraform configuration files set up and run in SAS Viya Infrastructure as Code projects for:
    * [Microsoft Azure](https://github.com/sassoftware/viya4-iac-azure)
    * [Amazon Web Services](https://github.com/sassoftware/viya4-iac-aws)
    * [Google Cloud Project](https://github.com/sassoftware/viya4-iac-gcp)
    * Redhat OpenShift
    * [Open source Kuberbetes](https://github.com/sassoftware/viya4-iac-k8s)
* Cloning the [SAS Viya 4 Administration Resource Kit (viya4-ark)](https://github.com/sassoftware/viya4-ark) project, and running the [Pre-Installation Check of SAS Viya System Requirements](https://github.com/sassoftware/viya4-ark/tree/master/pre_install_report) and configuration scripts
* Using [Mirror Manager for SAS Viya](https://support.sas.com/en/documentation/install-center/viya/deployment-tools/4/mirror-manager.html) to create a mirror repository
* Cloning and running the SAS Viya Orchestration CLI to download SAS Viya deployment assets, or using the [SAS Viya Deployment Project](https://github.com/sassoftware/viya4-deployment) on GitHub to do the same. See [Deployment Methods](https://go.documentation.sas.com/doc/en/itopscdc/default/itopscon/p0839p972nrx25n1dq264egtgrcq.htm) in the SAS Viya Platform Operations guide.
* Configuring your deployment assets to pull images from your mirror repository
* Configuring your deployment assets for your own requirements prior to deployment, e.g. for identity and authentication through external services, for access to external data providers
* Deploying an observability solution (such as [SAS Viya Monitoring for Kubernetes](https://github.com/sassoftware/viya4-monitoring-kubernetes)) for monitoring, logging and alerting
* Configuring storage and mounting it
* Deploying SAS Viya
* Performing post-deployment configuration of your SAS Viya deployment, to
    * Create user folders and projects, and secure them
    * Create CAS and Base libraries and load data into them
    * Import user-defined content such as reports, models, data plans, jobs, flows, etc.

Cloud service provider-specific tools such as [Azure DevOps Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) can be a very convenient tool for this sort of task. Other cloud service providers offer similar toolsets.

See also [Validate your SAS Viya Deployment](./validate_deployment.md) [Task]

[Back to checklist](../checklist.md)