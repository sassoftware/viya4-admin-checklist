![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure Programming Allowlist

<!--
SortString: 0410
Description: Configure SAS Programming Run-Time for user-defined paths
Tags: Initial,New,Done
Topic: SAS Programming Run-time
Essential: Yes
Authors: David Stern
-->
When: Before user access, as needed

## About the allowlist (LOCKDOWN paths list)

As described in [Configure lockdown for SAS Programming run-time servers](./configure_lockdown.md)
[Task], once it has finished initialization, a SAS programming run-time session
enters a **locked down state**, in which it has limited file system access. All
access to local files and directories is validated through the lockdown path list.

As described in the [LOCKDOWN Statement](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p04d9diqt9cjqnn1auxc3yl1ifef.htm#n1o97m3ngxddujn1c3y352rt68x4) [Doc],
in order to access a file system path which is not in that allowlist, you (as
SAS Administrator) can do one of two things, in the global compute server (or
connect server or batch server) autoexec, or in the compute, connect or batch
context autoexec:

> Note: Only SAS Administrators have access to modify these settings.

1. Define a reference to an external file using a statement such as FILENAME,
   FILE, INFILE, %INCLUDE or define a path-based library with a LIBNAME
   statement. For example:

    ```sas
    filename test "/path/to/test.dat";
    libname mylib "/path/to/mydata";
    ```

    Because these statements are executed before the compute, connect or batch
    session enters the locked down state, access to the file system paths they
    reference is allowed through the resulting fileref or libref.

1. Add paths or specific files to the lockdown allowlist, which allows non-Admin
1. users to later define their own references to these paths or files, using
1. fileref or library declarations in their own code. For example:

    ```sas
    lockdown path='/path/to/directory1';
    lockdown path='/path/to/directory2';
    lockdown file='/path/to/file.dat';
    ```

After doing one of these things, users will be able to access the paths or
specific files in the paths list.

### Hide the lockdown paths allowlist from users

Note that users with access to SAS Environment Manager or the sas-viya CLI can
see the server and context autoexec blocks, even if they cannot modify them.
[Example 1](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p04d9diqt9cjqnn1auxc3yl1ifef.htm#p0lqdljyx1zz5on1ahgz9lxgc5wa)
in the [References](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p04d9diqt9cjqnn1auxc3yl1ifef.htm)
section for the Programming Run-Time Servers, shows how you can use a text file
in a path which is inaccessible to users (and may be inaccessible after servers
enter the locked down state), to define the lockdown paths list. This
effectively hides the paths list from users.

## List the lockdown paths allowlist

There is a LOCKDOWN command to list the files in the paths list. However, once a
compute session has entered the locked down state, you can no longer run
LOCKDOWN statements. So users get an error if they try to run a `lockdown list;`
statement. This is generally a good thing: you many not want users to know
which paths are in the lockdown paths list. However, as an administrator, you
need to be able to view it.

The solution is for an administrator to (at least temporarily) add a `lockdown list;` statement to either:

* a compute context autoexec code block, or
* the global compute server autoexec code block

It is best to add a `lockdown list;` statement after any other lockdown (path or
file) statements have been processed, so that you get the list of paths after
these statements have been processed.

However, even if you do this, the resulting log messages are not normally
shown to the end user in e.g. SAS Studio program log output.

You can see them by starting a SAS Studio session as a specific user (e.g. in
the following example, that user is `geladm`), so that `lockdown list;`
statement will run during initialization of the compute session running under
the SAS Studio Compute Context. Then,  while the SAS Studio session is still
running, this kubectl command will show the pod name:

```sh
kubectl get pods -l launcher.sas.com/requested-by-client=sas.studio,launcher.sas.com/username=geladm --field-selector status.phase=Running --sort-by=.metadata.creationTimestamp --output=jsonpath={.items..metadata.name}
```

> Tip: Remember to replace the username `geladm` in the command above with the
> username of the user who started the SAS Studio session.

The kubectl command below then incorporates the command above (remember to
replace `geladm` with the correct username again). It gets the pod name from the
subcommand inside the `$()`, and then uses kubectl logs to list log messages,
and grep to focus on log messages containing the locked down paths list:

```sh
kubectl logs $(kubectl get pods -l launcher.sas.com/requested-by-client=sas.studio,launcher.sas.com/username=geladm --field-selector status.phase=Running --sort-by=.metadata.creationTimestamp --output=jsonpath={.items..metadata.name}) -c 'sas-programming-environment' | grep -i -B 3 -A 25 'These pathnames can be accessed when SAS is in the lockdown state'
```

The resulting output in JSON format can be a little hard for a human to read,
but it does contain all the lockdown paths.

Viewing the resulting logs in a better log monitoring application, such as SAS
Viya Monitoring for Kubernetes' log monitoring tool, ElasticSearch Dashboards,
can make the messages much easier to read. Here is the relevant part of a CSV
exported from OpenSearch Dashboards:

> Note: In the results below, the paths `/gelcontent` and `/mnt/gelcontent` have
> been added to the lockdown paths list. The rest of the paths shown are the default.

```log
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,NOTE: AUTOEXEC processing completed.
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,NOTE: These pathnames can be accessed when SAS is in the lockdown state:
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/opt/sas/viya/home/share/fonts
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/usr/lib/jvm/java-11-openjdk-11.0.17.0.8-2.el8_6.x86_64/lib/fonts
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/opt/sas/viya/home/SASFoundation
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/security/trustedcerts.pem
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/security/tls.crt
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/usr/local/share/lua/5.2
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/usr/local/lib/lua/5.2
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/compute_data
"Mar 9, 2023 @ 15:42:27.436",INFO,compsrv,/opt/sas/viya/home/share/refdata/qkb
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/rdutil
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/sasuser
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/tmp
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/shared/gelcontent/home/Delilah
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/sashelp
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/opt/sas/viya/home/commonfiles
"Mar 9, 2023 @ 15:42:27.437",INFO,compsrv,/opt/sas/viya/config/data/modelsvr/astore
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/opt/sas/viya/config/data/modelsvr/resources
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/opt/sas/viya/config/var
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/config
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/opt/sas/viya/home/sas-pyconfig
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/gelcontent
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/opt/sas/viya/home/lib64
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,/mnt/gelcontent
"Mar 9, 2023 @ 15:42:27.438",INFO,compsrv,NOTE: The LOCKDOWN option has been set. SAS is now in the lockdown state.
```

> Note: The paths shown are as seen by the compute server process running INSIDE
> a compute server pod. They are NOT accessing the host machine on which the pod
> is running in Kubernetes and Docker.

> Note: Remember to comment out or remove the `lockdown list;` statement if you
> do not wish the paths list to be normally visible to users with access to
> your log monitoring solution.

See also:

* [LOCKDOWN statement](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p04d9diqt9cjqnn1auxc3yl1ifef.htm#n1o97m3ngxddujn1c3y352rt68x4) [Doc]
* [Lock Down the SAS Compute Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00001viyaprgmsrvs00000admin.htm#n0wbsg2g8p1x2rn15e2rwocylxr7) [Doc]
* [Lock Down the SAS/CONNECT Server](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00005viyaprgmsrvs00000admin.htm#n03031viyaservers000000admin) [Doc]
* [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]
* [Configure CAS Allowlist](./configure_cas_allowlist.md) [Task]
* [Select Log & Metric Monitoring and Alerting Solution](./select_monitoring_solution.md) [Task]
* [Set Up Monitoring and Alerting](./observability_monitoring_and_alerting.md) [Task]


[Back to checklist](../checklist.md)