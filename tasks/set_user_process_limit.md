![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Set User Process Limit

<!--
SortString: 0430
Description: Set the maximum number of launched compute, connect or batch programming run-time pods each user may run simultaneously
Tags: Initial,New,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
-->
When: After platform changes

By default, SAS Viya is configured to allow each user to run 10 launched SAS
Programming Run-Time (i.e. the sum of SAS Compute, SAS Connect and SAS Batch)
sessions/pods at the same time - 10 total across all launched pods. This is
intended to prevent users from starting an excessive number of SAS compute
servers at the same time, denying access to compute resources to other users.

See [Limit a user’s simultaneous compute server processes in SAS Viya 2021.1 and later](https://communities.sas.com/t5/SAS-Communities-Library/Limit-a-user-s-simultaneous-compute-server-processes-in-SAS-Viya/ta-p/761820) [Blog] for a detailed explanation.

See your current user process limit:

```sh
kubectl describe deploy sas-launcher | grep SAS_LAUNCHER_USER_PROCESS_LIMIT
```

Example results, showing default values:

```log
SAS_LAUNCHER_USER_PROCESS_LIMIT:                10
SAS_LAUNCHER_USER_PROCESS_LIMIT_ENABLED:        true
```

As that blog post describes, there are two ways to change the limit. A quick,
non-persistant method sets a new value for  SAS_LAUNCHER_USER_PROCESS_LIMIT which
will not persist if SAS Viya is redeployed, and a slightly more involved method
which involves redeploying SAS Viya, but would persist if SAS Viya is
redeployed.

Example kubectl command (the first, non-persistant method) to change the user
process limit on the fly:

```sh
kubectl set env deploy sas-launcher SAS_LAUNCHER_USER_PROCESS_LIMIT=5
```

You can find instructions for changing your user process limit the second, more
persistant way in your deployment directory (`$deploy`), in the README file at `$deploy/sas-bases/examples/sas-launcher/configure/README.md` (for Markdown format) or at `$deploy/sas-bases/docs/configuration_settings_for_sas_launcher_service.htm` (for HTML format).

When possible, the second method is preferable in a production
Kubernetes cluster.

Both methods require Kubernetes administrator access (to modify the sas-launcher
Kubernetes deployment or to modify the kustomization.yaml file and site-config
overlays), and therefore as a SAS Administrator, you may need to work with your
Kubernetes administrator to implement and changes you require, if you are not
a Kubernetes administrator for the cluster in which SAS Viya is deployed yourself.

There is also a SAS_LAUNCHER_SUPER_USER_PROCESS_LIMIT for members of a SAS Viya custom group named `LauncherSuperUsers`, which (a little like `CASHostAccountRequired`) does not exist 'out of the box'. If you create a group of that name, and add users to it, a separate limit applies to those users:

```sh
kubectl describe deploy sas-launcher | grep SAS_LAUNCHER_SUPER_USER_PROCESS_LIMIT
```

Example results, showing default values:

```log
SAS_LAUNCHER_SUPER_USER_PROCESS_LIMIT:          15
SAS_LAUNCHER_SUPER_USER_PROCESS_LIMIT_ENABLED:  true
```

See the documentation for this feature at:

* SAS Viya Administration > Servers and Services > Programming Run-Time Environment > Programming Run-Time Servers > SAS Launcher Service > [Configure Denial-of-Service Protection](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00002viyaprgmsrvs00000admin.htm#p0dvcvne6of1run1b1sl0z1j303r).


[Back to checklist](../checklist.md)