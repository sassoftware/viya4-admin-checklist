![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Modify Launcher and SAS Programming Run-Time Server Contexts

<!--
SortString: 0380
Description: Modify Launcher and Server contexts for SAS Compute Server, SAS Connect Server and SAS Batch Server
Tags: Initial,Legacy,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern,Michael Erickson
-->
When: After platform changes

Understanding what the [SAS Programming Run-Time Environment](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n01000viyaprgmsrvs00000admin.htm) is (see below) will help you understand whether or not you might need to customize it for your business needs. Familiarize yourself with the configuration settings you can access through Launcher, Compute, Connect and Batch Contexts. Customize those settings you need to for your business needs. Review these customizations against your needs after platform changes, e.g. updates and upgrades to your SAS Viya deployment (which may introduce new SAS programming run-time customization options) or in response to changes in business requirements for SAS programming.

See also: [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]

## About The SAS Programming Run-Time

The [SAS Viya platform's Programming Run-Time Environment](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n01000viyaprgmsrvs00000admin.htm) is the set of components which work together to run SAS programs. It is primarily made up of:
* A [SAS Launcher Service](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00002viyaprgmsrvs00000admin.htm), that provides API endpoints for 'launching' (running) SAS Compute Server, SAS Connect Server and SAS Batch Server pods - the pods that contain the sas-programming-environment container, which run the processes that actually execute SAS programs
* A [SAS Compute Service](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00001viyaprgmsrvs00000admin.htm#n05002viyaprgmsrvs00000admin) which provides API endpoints for requesting a SAS Compute Server session. It calls the SAS Launcher Service to ask it to start a SAS Compute Server pod, each of which runs one instance of the SAS Compute Server process. Once a SAS Compute Server pod has started up and registered itself with the SAS Compute Service, the SAS Compute Service will send code to it to be run, and will receive back execution status (pending, running, finished etc.), along with SAS log output, results etc. The SAS Compute Service can start (via the SAS Launcher) as many SAS Compute Servers as it needs to, running at the same time. When SAS Compute Server processes finish, their pods usually terminate (unless they are configured to be re-usable). In contrast, only one instance of the SAS Compute Service usually runs at a time, and it remains running even when no SAS Compute sessions are currently active.
* A [SAS/CONNECT Spawner](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n00005viyaprgmsrvs00000admin.htm) which serves several functions, including providing API endpoints for requesting a launched SAS/CONNECT Server session. When these are used it uses the SAS Launcher Service to start a SAS Connect Server pod, which runs for as long as the SAS Connect session lasts.
* A [SAS Batch Service](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n0h9w6up3rf2a8n1j68cgh3u74f8.htm) which calls the SAS Launcher Service to launches SAS Batch Servers pods which to process SAS programs in a batch mode, and which run for as long as the SAS Batch session lasts.

> **Note**: This is one of the few topics where it is worth paying attention to the difference between `service` and `server`:
>
> * SAS Programming Run-Time `services` run all the time that your SAS Viya deployment is running. There can be just one pod for each service, though you can run multiple pods for services if you want higher availability or load balancing. The services above act as a broker which other SAS Viya components can call when they want to start,  manage, communicate with and stop individual SAS Programming Run-Time servers.
> * SAS Programming Run-Time `servers` are temporary things, started on demand to host individual SAS compute, connect and batch programming sessions. They usually terminate when the programming session ends. There is often one Programming Run-time pod per server, where each of these pods supports one SAS programming session, though there are exceptions to this.
>
Like most SAS Viya servers, the services above including the SAS/CONNECT Spawner have configuration settings, which can be managed in the SAS Configuration Server, or using the [configuration plug-in](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfig/p0rtltqk08n6y6n1hts1n4ypqfao.htm?fromDefault=) [Doc] for the [sas-viya CLI](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcli/titlepage.htm) [Doc].

However, unlike most SAS Viya servers, each of the services above supports SAS Programming-Run Time sessions running under a several different **contexts**. Contexts allow for variation in the way the service is configured, to support a variety of use cases e.g. different resource use, different locales, different pre-defined formats, libraries or macros, and more. SAS Viya supports access controls for contexts - a SAS Administrator can manage who gets access to each context, so it is possible to create contexts for specific groups of users.


## Launcher Contexts

SAS Launcher Contexts are specifications that apply environmental settings, define values for configuration attributes, and specify access constraints on launched Programming Run-Time pods. See SAS Viya Platform Administration > Servers and Services > Programming Run-Time Environment > Server Contexts > Concepts > [Launcher Contexts](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcontexts/n05013viyaprgmsrvs00000admin.htm#n05008viyaprgmsrvs00000admin) for a brief explanation.

In practice, a launcher context has fewer settings that a SAS Administrator might modify than Compute Connect or Batch contexts. These include the name of the pod template used to launch pods, and variables that specify character encoding and locale. A launcher context can also specify shell commands that run on startup, or a SAS Workload orchestrator queue. Many SAS Launcher Contexts are defined out-of-the-box.

We expect it will be relatively unusual that a SAS Viya administrators would need to modify their deployment's Launcher Contexts, except perhaps to change the default character encoding or locale. Modifying Compute, and to a lesser extent Connect or Batch contexts, is likely to be more common.

## Server Contexts

Server contexts are grouped by SAS Programing Run-Time Server type, into Compute Contexts, Connect Contexts and Batch Contexts.

### SAS Compute Contexts

Multiple Compute Contexts are provided out-of-the-box with a SAS Viya deployment, and there are separate compute contexts for SAS Studio, SAS Model Manager, SAS Job Execution, Data Mining and other uses. They allow finer-grained control of configuration settings to be applied to SAS Compute sessions running under a that specific context, while not affecting the other contexts.

You can also [create your own compute context](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p1dkdadd9rkbmdn1fpv562l2p5vy.htm#n0hv55468frsy1n182u5uwwqbvgz) [Doc], if you have business reasons to grant e.g. members of one group access to compute contexts with more memory than others, or to compute contexts that run as a service account rather than as the user.

Compute contexts provide a place to [specify attributes](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcontexts/p1a8po37wdvhkon1bvetgejmiznk.htm?fromDefault=) [Doc] that modify the behaviour of a compute session. Examples include **runServerAs**, used to run sessions under the context as another user, **reuseServerProcesses** used to make compute servers reusable, or **serverMinAvailable**, used to pre-start a pool of available servers. There are many other attributes you can set.

Compute contexts also have a place to define additional SAS autoexec statements, SAS options or a SAS Workload Management queue.

### SAS/CONNECT Service Contexts

Implementing a similar idea to Compute Server Contexts, as of SAS Viya LTS 2022.09, by default there is only one Connect Context, named default-launcher. It specifies an associated launcher context, SAS Workload Management queue (if applicable), and provides a place to specify SAS Options.

See [SAS/CONNECT Service Contexts](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calcontexts/n05013viyaprgmsrvs00000admin.htm#p00s7juncln5ckn1eambzovrt39l) [Doc] for more detail.

### SAS Batch Contexts

Again implementing a similar idea to SAS Compute Contexts, as of SAS Viya LTS 2022.09, by default there are only two Batch Contexts, named default and default-cmd.

Each specifies an associated Launcher Context, and can specify a SAS Workload Orchestrator queue, and SAS options.

## Further reading

See also:

* [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]
* [Configure Programming Allowlist](./configure_programming_allowlist.md) [Task]
* [Define Library Connection Data Sources as a Resource in SAS Programming Run-Time Contexts](./manage_connections_to_data_sources.md) [Task]

[Back to checklist](../checklist.md)