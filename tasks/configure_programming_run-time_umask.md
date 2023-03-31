![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure umask for SAS Programmning run-time servers

<!--
SortString: 0420
Description: Configure umask to e.g. 0002 for SAS Programming Run-Time servers, so that files created by users (including datasets in path-based libraries) are read-write for members of the user's primary POSIX group
Tags: New,Initial,Done
Topic: SAS Programming Run-time
Essential: -
Authors: David Stern
-->
When: After platform changes

## In this task <!-- omit from toc -->

* [Make the main organizational groups owners of their group's directories](#make-the-main-organizational-groups-owners-of-their-groups-directories)
* [Set the setgid bit for each directory](#set-the-setgid-bit-for-each-directory)
* [Using group-ownership and the setgid bit together](#using-group-ownership-and-the-setgid-bit-together)
* [Why you should set UMASK to 0002 for SAS Progamming Run-time users](#why-you-should-set-umask-to-0002-for-sas-progamming-run-time-users)
* [How to set umask to 0002 for SAS Programming Run-time users](#how-to-set-umask-to-0002-for-sas-programming-run-time-users)


If any of your SAS programming run-time libraries are path based, with their
files held on POSIX filesystems, you can use two things in combination to enable
your users to modify (and delete) files created by other users who are a member
of the same group.

Here's how it works.

1. Files and directories all have a user-owner and a group owner.
1. Files and directories have a set of POSIX permissions, with read, write and
1. execute bits for each of
   * the user-owner
   * the group-owner, and
   * 'everyone' or 'other' or 'world' (alternative names for the same thing)
1. An operating system setting called the `umask` controls the permissions that
   newly-created files have. It's a bit complicated - the umask specifies in a
   binary syntax what permissions new files *don't* have; so see the LINUX
   [umask's manual page](https://man7.org/linux/man-pages/man2/umask.2.html) for
   details, and be prepared to concentrate a bit. This is something you may find
   easier to learn about by seeing[some examples]
   (https://www.computerhope.com/unix/uumask.htm).

So, let's put these ideas together.

## Make the main organizational groups owners of their group's directories

If you have directories in a POSIX filesystem for SAS libraries and other files
used from within SAS (and perhaps other applications), make the groups to which
users belong the group-owner of that group's directories.

## Set the setgid bit for each directory

In POSIX filesystems, users can be members of one or more groups, and have one
specific group as their primary group. Users can be members of many other groups
as their secondary groups.

Files created by users (e.g. new datasets in path-based libraries) are normally
created with the user as the file's user-owner, and the user's primary group as
the file's group-owner.

Filesystem administrators can alter this behaviour by setting the ['setgid'
bit](https://linuxconfig.org/how-to-use-special-permissions-the-setuid-setgid-and-sticky-bits) on a directory.

To set the setgid bit on a directory, use the [chmod]
(https://ss64.com/bash/chmod.html) command. Chmod understands two notations for
permissions: a 'mode' notation such as `g+s`, or a 'numeric_mode' notation, such
as `2750`.

Examples:

```sh
chmod g+s /gelcontent # Sets the setgid bit on /gelcontent
chmod 2750 /gelcontent/hr # Sets the setgid bit on /gelcontent/hr, and also user:rwx, group:r-x, world:---
```

You can tell if the setgid bit is set on a directory, because the letter `s`
appears in its permissions string in the place where the group-execute bit would
normally display an `x` in the long-form output of an `ls` command, e.g. the `s`
in the 7th character of `drwxrwsr-x.`

If the setgid bit is set for a directory, the DIRECTORY's group-owner is made
the new file's group-owner, instead of the user's primary group.

> **Note**: People sometimes confuse the setgid bit with the sticky bit.
> The sticky bit is something else entirely, and is not useful in this context.
> See its explanation [here](https://linuxconfig.org/how-to-use-special-permissions-the-setuid-setgid-and-sticky-bits)
> if you want to understand the difference; otherwise you can safely ignore the
> sticky bit.

## Using group-ownership and the setgid bit together

Here's an example:

> **Note**: Notice the Group owner of each directory, and that the setgid bit is
> set in each directory's permissions.

In a fictional organization called gelcorp, all users of the SAS Viya platform
are members of a group called `sasusers`. Two specific groups of users,
`hr` and `sales` have their own file system subdirectories for code and data in the
company-wide /gelcontent file system path, which is mounted as a volume in SAS Programming
Run-time pods. Members of `hr` and `sales` have those groups respectively as their
primary group. They are still members of `sasusers` as one of their secondary groups.

| Filesystem Folder Path | User owner | Group owner | Permissions |
| ---------------------- | ---------- | ----------- | ----------- |
| `/gelcontent` | `sas` | `sasusers` | `drwxr-s---` |
| `/gelcontent/hr` | `sas` | `hr` | `drwxr-s---` |
| `/gelcontent/hr/code` | `sas` | `hr` | `drwxrws---` |
| `/gelcontent/hr/data` | `sas` | `hr` | `drwxrws---` |
| `/gelcontent/sales` | `sas` | `sales` | `drwxr-s---` |
| `/gelcontent/sales/code` | `sas` | `sales` | `drwxrws---` |
| `/gelcontent/sales/data` | `sas` | `sales` | `drwxrws---` |
| `/gelcontent/shared` | `sas` | `sasusers` | `drwxr-s---` |
| `/gelcontent/shared/code` | `sas` | `sasusers` | `drwxrws---` |
| `/gelcontent/shared/data` | `sas` | `sasusers` | `drwxrws---` |

## Why you should set UMASK to 0002 for SAS Progamming Run-time users

The final piece of the puzzle is the default unix UMASK value. By default in
most deployments we see, it has a value of `0022`. This means that files created
by the user have a default permissions pattern of `-rw-r--r--`, in other words
they **are NOT writable** by members of the file's group-owner.

Depending on your preferences, this can be a problem. If you create a dataset,
someone else who is a member of your primary group cannot modify or delete that file.

To solve this, we set the umask environment variable to `0002` before launching
the SAS Programming run-time environment, so that files created by the user have
a default permissions pattern of `-rw-rw-r--`, in other words they **ARE
writable** by members of the file's group-owner.

With that in place, in combination with the group-ownership of the directories
used to store files and the setgid bit on those directories being set, members
of the same group can modify and delete each other's datasets and other files,
which is usually what a SAS administrator would want.

Phew. That was a long-winded explanation for how to achieve something that
seems superficially simple. Now onto the main point of this task.

## How to set umask to 0002 for SAS Programming Run-time users

1. In SAS Environment Manager, signed in as a member of the SAS Administrators
1. group, open the Configuration page.

1. In the Definitions view, select the **sas.compute.server** configuration definition.

1. Edit the **Compute service: startup_commands** configuration instance.

1. At the end of the block of text already in the 'contents' section of this
1. configuration instance, add a line containing the following:

    ```sh
    umask 0002
    ```

1. Click Save.

Add a `umask 0002` line to **each** of these configuration instances:

> Tip: You already did the first of these if you followed the steps above.

| Server Definition | Configuration Instance name |
| ----------------- | ---------------------------- |
| sas.compute.server | Compute Service: startup_commands |
| sas.connect.server | SAS/CONNECT Spawner: startup_commands |
| sas.batch.server | SAS Batch Service: startup_commands |

This should set the umask environment variable to 0002 in all SAS Compute,
Connect and Batch servers launched from now on.

See also:

* [Where to configure the SAS Programming Run-time with broader or narrower
  scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]

[Back to checklist](../checklist.md)