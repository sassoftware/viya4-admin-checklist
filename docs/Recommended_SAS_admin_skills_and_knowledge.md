![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Recommended Skills and Knowledge for SAS Viya Administrators

## Kubernetes

SAS Viya 2020.1 and later runs on Kubernetes. A working knowledge of [Kubernetes
concepts](https://kubernetes.io/docs/home/) is essential for SAS Administrators, including [Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) such as :

* Pods
* Deployments, controllers, statefulsets, daemonsets
* Nodes, how nodes can be labelled to manage workload placement
* Namespaces
* Jobs and cronjobs
* Volumes, volumemounts
* Persistant volumes and persistant volume claims
* Secrets and configmaps
* [kubectl](https://kubernetes.io/docs/reference/kubectl/), the Kubernetes command-line tool
* kube config files

We would encourage all SAS Administrators to complete at least an introductory course in Kubernetes from your favourite training provider, or from one of the sources on this page: https://kubernetes.io/training/.

You should also become familiar with at least one Kubernetes user interface, such as Lens, OpenLens, K9s or [the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/).

## Know which SAS Viya deployment method was used

While it is not usually up to the SAS Administrator to decide how SAS Viya should be deployed, you should still find out which deployment method is used for *your* SAS Viya deployment, and familiarize yourself with how it works. This will help you discuss customizations that could be made to your deployment with whoever does deploy and maintain it.

If you are the SAS administrator for an on-demand instance of SAS Viya hosted by SAS or by a cloud service provider, which neither you nor anyone in your organization deploys, it is not as important to know which deployment method was used.

However, if you or anyone else in your organization deploys the instance of SAS Viya which you manage, you should know that there are several [Deployment Methods](https://go.documentation.sas.com/doc/en/itopscdc/default/itopscon/p0839p972nrx25n1dq264egtgrcq.htm) that can be used to deploy SAS Viya. These have gradually evolved since SAS Viya 2020.1 was first released, and may continue to develop and change. At the time of writing the four available methods are:

* Deployment using the [SAS Viya 4 Platform Deployment Operator](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/p127f6y30iimr6n17x2xe9vlt54q.htm#p0lhaw04t8hfhjn1cn1gadt5gbph)
* Deployment using the [sas-orchestration command running inside a Docker container](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/p127f6y30iimr6n17x2xe9vlt54q.htm#p18cfbdx5dzwoan1qsvtitxg2nir)
* Deployment using [Kubernetes commands](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/p127f6y30iimr6n17x2xe9vlt54q.htm#p0n0x0jvog312an1wggpgnam1jsw) (i.e. kubectl apply)
* Deployment using the [SAS Viya 4 Deployment](http://github.com/sassoftware/viya4-deployment) GitHub project

For an on-site deployment, may be able to learn which method was (and is) used from project documentation, or by asking the architect or deployment specialist who deployed and/or maintains your SAS Viya deployment.

Once you have identified the deployment method used, it is useful to be aware of how customizations to your deployment are made, even if you are not going to make those customizations yourself.

## Label Kubernetes nodes to manage workload placement

Read the SAS Viya Platform Operations guide's section on Deployment > Pre-Installation Tasks > [Plan the Workload Placement](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/p0om33z572ycnan1c1ecfwqntf24.htm). This explains the four main SAS Viya workload classes (stateless, stateful, cas and compute), and why you need to plan to distrubute workload across different nodes in your Kubernetes cluster so that each type of workload has the resources it requires, and so that different types of SAS Viya services/pods do not compete with each other for resources in an undesirable way. It explains how labels, and taints are used to manage where pods will run, due to their tolerations.

Also note that the page linked above says:

> **IMPORTANT** SAS strongly recommends labeling and tainting all your nodes, especially the CAS nodes. [...]

## Know how to customize your SAS Viya platform deployment

Customizing many aspects of your SAS Viya platform deployment is done during initial deployment, or by re-deploying the software.

See [Initial kustomization.yaml File](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n0g237aqo6pz1in1t19wjb94j9bi.htm), [Common Customizations](https://go.documentation.sas.com/doc/en/itopscdc/v_037/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm) and [Modify Existing Customizations in a Deployment](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n1f2q6pp0gjheqn1jl204vptrubs.htm) in the SAS Viya Platform Operations documentation.

[Back to checklist](../checklist.md)