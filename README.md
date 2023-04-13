![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# SAS Viya Administration Checklist: README.md

This project is for SAS Viya 2020.1 and later. See [Previous Versions](#previous-versions) for earlier versions of SAS.

> **[Direct Link To Checklist](./checklist.md)**

## Table of Contents of this README.md  <!-- omit in toc -->

* [Overview](#overview)
  * [Initial tasks](#initial-tasks)
  * [Regular tasks](#regular-tasks)
  * [What's New](#whats-new)
  * [Installation](#installation)
* [Getting Started](#getting-started)
  * [Applicability to SAS Versions](#applicability-to-sas-versions)
  * [Running](#running)
* [Contributing](#contributing)
* [License](#license)
* [Previous Versions](#previous-versions)
* [Additional Resources](#additional-resources)

## Overview

The [checklist](checklist.md) in this project contains two lists of tasks. There is a suggested frequency for the regular tasks. You, as an IT administrator or a SAS administrator, should consider performing the tasks in these lists for the SAS Viya 2020.1 and later environments that you maintain. Perform all tasks that are relevant to your environment to keep your SAS Viya deployment operating at its best over the long term.

### Initial tasks

The first list contains initial tasks, which are normally performed as one-off activities. They are performed usually shortly before, while, or soon after SAS Viya is deployed on your Kubernetes cluster. Most initial tasks should be reviewed whenever you make significant changes to your deployment (such as adding new Kubernetes nodes, adding new software components, migrating, or upgrading the version of SAS or other major components). Significant project work to deliver custom SAS application functionality based on your deployment often requires at least some of these initial tasks to be repeated or revised.

### Regular tasks

The second list contains regular tasks, which should be performed at different times to keep your platform healthy, secure, and efficient.

Some tasks contain additional commentary. Some tasks contain brief details about how they are performed. You might need to consult other resources for more detail. Some links to documentation and blog posts are included in the commentary for the tasks, but you will need to consult the documentation for further guidance.

In the task descriptions, the words server or service always mean one or more programs. In the case of a SAS Viya server or service, these will be running inside a container in a Kubernetes pod. In the task descriptions, these terms never mean the host node or machine. Often, **service** (or microservice) refers to a SAS Viya software component which runs all the time while the SAS Viya deployment is running. In contrast, **server** often refers to a software component which is started to perform a specific task, and may be stopped when that task is complete. For administrators, this distinction is important only in a few specific situations (for example, when managing log levels and other service- or server-specific configurations). This distinction can otherwise be ignored.

### What's New

[//]: # (**Optional**. If applicable to your project, list new features that users need to be aware of. This section might supplement the Changelog file from the repository and only highlight important changes.)

Everything is new.

[Checklists of administration tasks for previous versions of SAS](#previous-versions) were published as PDF or Word documents.

### Installation

[//]: # (**Required**. Provide step-by-step instructions to install your software project. Use subtopics and screenshots, as appropriate.)

For **general users**, the project is best viewed on GitHub. No installation is necessary.

For **contributors**, we suggest you clone this project from GitHub and edit it using your favorite source code editor. (Please also see the [Contributing](#contributing) section of this README.)

If you wish to contribute, you may find it helpful to be able to run Python3 in a bash terminal, so that you can run the scripts which update documents like the top-level [checklist.md](checklist.md), e.g. [scripts/build_all.py](scripts/build_all.py) (or [scripts/build_from_template.py](scripts/build_from_template.py)). By doing that, you can see if your modified tasks appear as you intend when they are listed in the [checklist.md](checklist.md) tables of tasks.

> Tip: The lead authors/editors maintain this project using [Microsoft Visual Studio Code](https://code.visualstudio.com/) on both:
>
> * Windows with [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) version 2 (WSL2) running [Ubuntu](https://ubuntu.com/), which is the default Linux distribution for WSL2.
> * On MacOS, which supports Linux natively
>
> [Microsoft Visual Studio Code](https://code.visualstudio.com/) is available for both Windows and MacOS. It is convenient to run the project's Python scripts from a bash terminal within VS Code.
>
> The easiest way to get this set up is to follow the instructions in [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial). This walks you through installing:
>
> * VS Code
> * VS Code Python extension
> * Python 3
>
> We also like these VS Code extensions: [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph), [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github), [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint), [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense).
>
> You do not have to use these tools. You can contribute successfully to this project with command-line git and your preferred text editor. It is not necessary to run the project's Python scripts to rebuild the checklist.md document before submitting a pull request. The project owners run the scripts to update checklist.md before merging into the main branch.

## Getting Started

This project does contain some code examples, but it mostly consists of recommendations and suggestions.

If you have not read it already, begin by reading the [Overview](#overview) in this README, followed by [How to use this Checklist](how_to_use_this_checklist.md).

This project is written for a specific [intended audience](intended_audience.md) of SAS and IT administrators, and related roles.

Read about SAS Viya Administration Training and Certification in the [Additional Resources](#additional-resources) section of this README.

### Applicability to SAS Versions

In November 2020, SAS shipped SAS Viya Stable version 2020.1.1. SAS has released [many further versions of SAS Viya since then](https://communities.sas.com/t5/SAS-Viya-Release-Updates/tkb-p/releaseupdates). You can read about [SAS Viya platform cadences and release numbers here](https://communities.sas.com/t5/SAS-Communities-Library/Understanding-SAS-Viya-cadences-and-release-numbers/ta-p/825768).

> As described in the SAS Viya Operations guide > Getting Started > [Frequently Asked Questions](https://go.documentation.sas.com/doc/en/itopscdc/default/itopscon/n0tx1x9gu37i7qn1nuv8inwzrfet.htm):
>
> *[**How frequently is software released?**](https://go.documentation.sas.com/doc/en/itopscdc/default/itopscon/n0tx1x9gu37i7qn1nuv8inwzrfet.htm#n1tjwv96rc8rkln1k6bepxh1qksq)*
>
> *SAS offers the following release cadences for the SAS Viya platform:*
>
> * *On the Stable cadence, software is released monthly. The latest version on the Stable cadence contains the most up-to-date software, including new features, changes to features, and bug fixes.*
> * *On the Long-Term Support cadence, software is released about every six months.*
>
> *Starting in September 2022, the versions for the SAS Viya platform releases use the yyyy.mm format. For more information, see [Release Schedule and Versions](https://go.documentation.sas.com/doc/en/itopscdc/default/itopscon/n0skwn6305faxnn1v0lfhzssr41u.htm).*

To the best of our knowledge, the guidance for all tasks in this project is relevant for all versions of SAS Viya (i.e. stable version 2020.1.1 and later, and LTS version 2020.1 and later), except where specifically noted.

We take no liability for errors or omissions in the content of this document, which is written based on individual consultants’ field experience and shared in this project in good faith.

### Running

[//]: # (**Optional**. Instruct others about the initial tasks to get started using your project after they've installed it. This is a good place to include screenshots, asciinema \(https://asciinema.org/\) recordings, or short usage videos.)

For **general users**, there is nothing to run. This project is intended to be read.

For **contributors**, or users making a their own custom version of the project, if you add or change specific properties of tasks (filename, title, SortString, Description or Tags) you can run the scripts which update documents like the top-level [checklist.md](checklist.md), e.g. [scripts/build_all.py](scripts/build_all.py) (or [scripts/build_from_template.py](scripts/build_from_template.py)). These scripts have usage instructions in their header comments.

[//]: # (### Troubleshooting)

[//]: # (**Optional**. Provide workarounds and solutions to known problems. Organize troubleshooting information using subtopics, as appropriate.)

## Contributing

[//]: # (**Required**. Use the default text below if you accept contributions. If you do not accept contributions \(e.g., a samples project\), note that here.)

We welcome your contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit contributions to this project.

[CONTRIBUTING.md](CONTRIBUTING.md) has instructions for how to write
a task and populate an HTML comment block with appropriate 'metadata' so the
task appears correctly in the main checklist.md and other lists of tasks.

## License

> This project is licensed under the [Apache 2.0 License](LICENSE).

## Previous Versions

There are two previous versions of this checklist, for earlier versions of SAS:

* Checklist of SAS Viya 3 Administration Tasks: https://support.sas.com/resources/papers/checklist-sas-viya-administration-tasks.pdf
* Checklist of SAS 9 Administration Tasks: https://support.sas.com/resources/papers/Platform-Administration-Tasks.pdf

## Additional Resources

[//]: # (**Required**. Include any additional resources that users may need or find useful when using your software. Additional resources might include the following:)

[//]: # (* Documentation links
\* SAS Global Forum papers
\* Blog posts
\* SAS Communities
\* Other SAS Documentation \(Tech Support, Education\))

Familiarize yourself with **at least the topics** in the version of these documents that corresponds to your release of SAS Viya:
* The [SAS Viya Operations Guide](https://go.documentation.sas.com/doc/en/itopscdc/v_023/itopswlcm/home.htm?homeOnFail), which includes the [SAS Viya: Deployment Guide](https://go.documentation.sas.com/doc/en/itopscdc/v_023/dplyml0phy0dkr/titlepage.htm)
* The [SAS Viya Administration Guide](https://go.documentation.sas.com/doc/en/sasadmincdc/v_023/sasadminwlcm/home.htm). This will likely have the most content of interest to a reader of an Administration Checklist.

The [Administration and Deployment](https://communities.sas.com/t5/SAS-Communities-Library/tkb-p/library/label-name/administration%20and%20deployment) label in the SAS Communities Library allows you to find a large selection of searchable blog posts and articles written by SAS Viya experts. High quality content is regularly posted there by members of the [SAS Global Enablement and Learning (GEL)](https://communities.sas.com/t5/tag/GEL/tg-p/board-id/library) team.

We find the [SAS Viya 4 Resource Guide]( https://github.com/sassoftware/viya4-resource-guide) very useful. It describes a set of linked open-source projects (like this one) that support the pre-installation, deployment, and subsequent monitoring and management of SAS Viya platform software.

Familiarize yourself with available [SAS Viya training from SAS](https://support.sas.com/training/us/paths/index.html). The training page can help you find training material on getting started, administration, data management, programming and analytics, SAS Visual Analytics on SAS Viya, and specific SAS Viya solutions such as SAS Visual Investigator. Courses can be taught in a classroom, as a live web class, or as self-paced e-learning.

SAS Viya administrators should be familiar with all administration interfaces to SAS Viya:
* Learn what each of the pages in [SAS Environment Manager](https://go.documentation.sas.com/doc/en/sasadmincdc/v_023/evfun/titlepage.htm) does.
* Learn how to use the [SAS Viya Command-Line Interface](https://go.documentation.sas.com/doc/en/sasadmincdc/v_023/calcli/titlepage.htm).

If you have [SAS Viya Data Preparation](https://go.documentation.sas.com/doc/en/dprepcdc/v_002/dprepwlcm/home.htm?fromDefault=) products, learn how to use [SAS Data Explorer](https://go.documentation.sas.com/doc/en/dprepcdc/v_002/datahub/n01gdrmxl7lhszn1gny5h764yisv.htm), [SAS Data Studio](https://go.documentation.sas.com/doc/en/dprepcdc/v_002/datastudioadv/titlepage.htm), and [SAS Lineage](https://go.documentation.sas.com/doc/en/dprepcdc/v_002/dmlinug/titlepage.htm).
