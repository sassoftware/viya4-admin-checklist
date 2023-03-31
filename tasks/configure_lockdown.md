![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure lockdown for SAS Programming run-time servers

<!--
SortString: 0400
Description: Configure lockdown for SAS Programming Run-Time servers
Tags: New,Initial,Done
Topic: SAS Programming Run-time
Essential: -
Authors: Scott McCauley,David Stern
-->
When: Before user access, as needed

By the time they execute user-written code, the SAS Programming Run-time Servers (compute, batch, and connect) are in a locked-down state. The SAS Viya platform does not support a way to disable LOCKDOWN.

When a SAS Programming run-time server and session starts up, it performs
initialization steps such as applying SAS options and processing SAS statements
in server-level and context-level autoexec files. All of these are managed by
SAS Administrators and are not subject to LOCKDOWN restrictions.

At the end of those initialization steps, every SAS Programming run-time session
enters a locked-down state, before it executes any user-written programming
statements (including any user autoexec statements). A SAS session in the locked
down state has the following restrictions:

* limited file system access
  * All access to local files and directories is validated through the lockdown path list. The lockdown path list specifies which host file resources are available when a SAS session is in the locked-down state. This list includes the default system directories and files.

* limited SAS language features
  * The following SAS language features are disabled:
    * DATA step Java Object javaobj
    * PROC JAVAINFO
    * PROC PYTHON
    * SAS functions: ADDR, ADDRLONG, PEEK, PEEKLONG, PEEKC, PEEKCLONG, POKE, POKELONG, and MODULE

The most common adjustment to the lockdown settings is the need to add additional file system paths to the lockdown path list. See [Configure SAS Programming Run-Time Allowlist](./configure_programming_allowlist.md) [Task].

Resource:

* [SAS Viya Platform Administration: Programming Run-Time Servers - References](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/p04d9diqt9cjqnn1auxc3yl1ifef.htm) [Doc]

See Also:

* [Modify Launcher and SAS Programming Run-Time Server Contexts](modify_programming_launcher_server_contexts.md) [Task]
* [Configure Open Source Integration](configure_open_source_integration.md) [Task]
* [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]
* [Configure SAS Programming Run-Time Allowlist](./configure_programming_allowlist.md) [Task]

[Back to checklist](../checklist.md)