![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Validate your SAS Viya Deployment

<!--
SortString: 0240
Description: Define a set of tests to validate that your SAS Viya deployment is functioning correctly
Tags: Initial,New,Done
Topic: SAS Administration
Essential: Yes
Authors: David Stern
-->
When: After platform changes

After you initially deployed your SAS Viya platform, and after making changes to your deployment, validate that it is working correctly.

See also [Validating the Deployment](https://go.documentation.sas.com/doc/en/itopscdc/default/dplyml0phy0dkr/n1rkhs5tyjns0xn1qq5x4mzo6sim.htm) in the SAS Viya Platform Operations documentation.


Based on that documentation, and on the suggestions below, design your own validation procedure, and follow it. You may be able to script or otherwise automate some of this validation - see also [Automate your SAS Viya Deployment Process](./automate_environment_creation.md) [Task].

The steps in your validation procedure should ideally be just enough to check the most important components are working, without taking a lot of time or effort. You may choose to add validation tests for components that you have previously found to be problematic in your specific SAS Viya depoloyment. They could include, and are not limited to, the following examples:

## Kubernetes validation

> Tip: Your Kubernetes administrator may need to perform these tasks if you (the SAS administrator) do not have the necessary access or skills.

1. Determine the URLs for key SAS Viya applications in this environment, e.g. SAS Environment Manager, SAS Drive, SAS Studio etc. (Does this URL change when you redeploy a new instance of SAS Viya?)
1. Check the Kubernetes cluster is running.
    * Validate that it has the expected number of nodes, and that they are all 'Ready'.
    * Check that it has the expected number of namespaces, especially the SAS Viya namespaces, and namespaces for any observability tools used to monitor the environment's metrics and logs.


## SAS Viya validation

1. Browse to the URLs for key SAS Viya applications in this environment, e.g. SAS Environment Manager, SAS Drive, SAS Studio etc. For each, if prompted, can you successfully authenticate (or are you successfully authenticated through single sign-on if that is expected)?
1. In SAS Studio, can you successfully run a simple programming statement, e.g. `proc options; run;`. Does it work?
1. In SAS Drive, can you switch to the Reports tab and successfully open the User Activity report in SAS Visual Analytics? Does the report render normally, and contain data?
1. Can you open your log monitoring application. Is it successfully collecting log messages from SAS Viya? Do they look 'normal' (within the rather broad scope of what 'normal' can mean in this context)?
1. In SAS Environment Manager, can you see that the expected data is loaded into memory in CAS, or is visible but not loaded?
1. Can you authenticate to SAS Viya from the sas-viya command-line interface (CLI)? Can you run some basic sas-viya CLI commands successfully?
1. Can you validate the SAS Studio compute context using the sas-viya CLI, e.g. `sas-viya --output text compute ctx validate --name 'SAS Studio compute context'`?
1. Can you submit a SAS Batch job using the sas-viya CLI? Does it run? Does it complete in a reasonable amount of time? Does it produce the expected output?

In addition to the suggested validation steps listed above, you should add tests for other automated and end-user driven activity that is important for your SAS Viya deployment, such as:

* Are there any pods that are 'Pending' or in a 'CrashLoopBackOff' status, or are otherwise not running in Kubernetes, where you would expect them to be running?
* Can you verify that access controls has been applied to data and authorization has been applied to folders, report, models or other objects as intended in your Security Model Design? See also [Authorization Model](./authorization_model.md) [Task].
* Can you access data in key datasets, or view it in key reports or models?
* Can you create a model using SAS Model Manager or SAS Visual Analytics? Can you run the model in SAS Model Studio? Can you create a project in SAS Model Manager and can you add your new model to it? Can you Create a model test in Model Manager, and score it? Can you publish the model to SAS Micro Analytic Service (MAS)? Can you clean up all validation assets you just created?
* Do you see expected messages in the logs?

## Automated Validation with the pyviyatools

ValidateViya is a pyviyatool that runs a series of tests on a Viya environment, validating that it is running as expected. validateviya has a modular design, allowing for the creation of custom tests, the alteration of existing tests, and the removal of unneeded tests. Checkout the [vaildateviya User Guide](https://github.com/sassoftware/pyviyatools/blob/master/validateviya-manual.md) in the [pyviyatools](https://github.com/sassoftware/pyviyatools).


See also:

* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]
* [Authorization Model](./authorization_model.md) [Task]
* [Automate your SAS Viya Deployment Process](./automate_environment_creation.md) [Task]

[Back to checklist](../checklist.md)