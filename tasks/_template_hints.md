![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

<!-- Give tasks a filename which is unique, fairly short, identifies the main concept of the task and has a .md file extension. Tasks are referred to by their filename (not by their SortString), and so it is preferable not to change a tasks's filename once it has been merged into the project's `main` branch. If you do change a task's filename, you must also find and similarly change any internal links to the task within this project. -->

# Template <!-- Title that will appear in checklist tables: keep it very short, < 50 chars is great. There must be exactly one level 1 heading like this in a task file, and it must be in this position, near the top. -->

<!--
SortString:
Description:
Tags:
Topic:
Essential:
Authors:
-->

When:
<!--
    When should an administrator (or someone they coordinate with) do this task? The 'When:' line is optional but usually included. Omit it if there is no particular time you think the task should be done. However, there is a 'best' time to perform most tasks in the checklist. If you do not include a 'When:' line, someone else may do so later.
    Examples:
      When: After platform changes
      When: Before and/or after platform changes and in tandem with organizational changes
      When: At the beginning and end of a period of troubleshooting activity
      When: Regularly per housekeeping schedule
    You are free to describe when the task should be done in your own words, if none of the examples above are appropriate to your task.
-->

## Subheading
<!--
    Above each of two or more separate ideas, a level 2 to 6 ATX Heading (https://github.github.com/gfm/#atx-headings).

    * A level 2 subheading looks like this: ## Brief description of part of the task
    * A level 3 subheading looks like this: ### Brief description of a sub-part the task or subordinate concept
    * ...and so on.

    Subheadings should be different from the task title, and are best included either:

    * if you need multiple subheadings to separate ideas that are part of the same tasks, or
    * if your task represents a single idea, but the task title doesn't adequately describe the task. For example, the title "Security Policy" is pleasingly short and the task document only presents one idea, but the task has one level 2 subheading ("Write and maintain a security policy that covers the SAS Viya deployment"). There are no other level 2 subheadings. This neatly keeps the table of contents entry for the task short, but explains what the task's idea is more clearly.

    If your task title adequately describes the task and the task only presents one idea, omit level 2 and lower subheadings.
-->

What, why, where to find instructions

<!--
Body text describing what the task is, why you should consider doing it and where to find instructions. In order of preference from most to least preferable, you may:

    Refer to existing instructions, when suitable instructions are publically available. If the existing instructions are only available in the form of unofficial or community-created content such as a blog post or video, consider asking for official SAS public documentation to be written to cover the topic. Not every topic we may write about will be suitable for official SAS public documentation.

    When suitable instructions are NOT publically available, ask for official documentation to be written and/or write a blog post or other article describing the task and how to do it, and publish it, e.g. in the SAS Communities Library. Then, write (or finish writing) a task here and refer to that post (e.g. using a permalink) in the body the task. If the instructions need to be updated, update your existing post or publish a new one, and where necessary update the references in the task so that they direct the reader to a current version of the instructions.

    Include instructions directly in the task's body text. This may seem easier, but it has some disadvantages, and is not the preferred approach. Good instructions take time to write and must be maintained. We think it is best to provide instructions in other, established locations, and not to turn this checklist into yet another source of detailed instructions.
-->

See also:

<!--
    Including one or more 'See also:' lines is optional.

    Your task's body text will usually contain one or more references to other resources. If you like to include links in your text that is fine. But a 'See also:' line is another option, which may suit tasks which refer to lists of resources when you do not need to write a story about them. Include a word or short phrase inside square brackets at the end of the link to indicate what sort of resource it is.

    Here are some examples:

    See also: [onboard_and_offboard_users.md](./onboard_and_offboard_users.md) [Task]
    See also: The [Jobs and Flows Page](https://documentation.sas.com/doc/en/sasadmincdc/default/evfun/n0b9cf8ru47gp6n1lvamxqwbr3by.htm) in the SAS Viya Environment Manager User's Guide [Doc]
    See also: [SAS Demo | Modify non-Default CAS Server Topology in Your Viya Deployment](https://www.youtube.com/watch?v=WxUXaTtZpSE) [Video]

    A 'See also:' line right before the link back to the top-level checklist is a good way to 'pair' your task with a related task, e.g. between a pair of tasks where there is a one-time initial 'set a thing up or learn how to do a thing' task, and an corresponding regular 'do the thing' task. Each task can have a 'See also:' line referring the reader to the other in the pair.

-->

[Back to checklist](../checklist.md)

<!--
    The following key-value pairs should all be included in the HTML comment section near the top of your task, each with the key and all its comma-separated values on one line.
SortString:
    Not a key. Avoid written references to tasks by their SortString. (Note: in previous checklists we often referred to tasks by their id, but this is now avoided because task SortStrings are expected to change from time to time). Changing a task's SortString value should never break a reference to the task.
    Intended to be used for sorting tasks in a checklist.
    May change arbitrarily when we re-order tasks.
    Suggest 3-digit number.
Description:
    A short description of the task, typically no more than 200-300 characters. If you need a longer description, consider whether this task should be split into two or more smaller tasks.
Tags:
    A comma-separated list of tags, all on one line, used for filtering tables of content in the checklist.md and other documents generated from templates. The order of these tags is not important.
    Other tag groups may be added in future, and tasks may be given tags from a new tag group retrospectively.
    Include exactly one tag from each of the following required groups:
        Temporal adjective: Initial or Regular (pick one - if you intend both make two tasks, one for 'define how to do it' and one for 'do it'):
            Initial
            Regular
        Status (for tracking progress in task development; only tasks tagged as `Done` appear in the main checklist.md):
            Backlog
            InProgress
            Review
            Done
        Provenance (New for tasks that are completely new for SAS Viya 2021.1 and later. Legacy for tasks that had equivalents in earlier checklists for SAS Viya 3 and SAS 9. The detail of these tasks in SAS Viya 2020.1 and later may differ very significantly from their earlier equivalents.):
            Legacy
            New
    There are currently no tag groups for which it makes sense to tag a task with more than one tag from the same group.
Authors:
    A comma-separated list full names (*firstname lastname*) of authors who wrote a substantial portion of the words in the task, even if they were copied here from another source. Use this tag - with the author's consent if possible - to acknowledge someone's contribution to the task content and avoid taking undue credit for another author's work. Adding your own name is optional - omit yours if you wish, though git and GitHub can generally identify your contibution to some extent. You should not add your name to the authors list if you only made minor edits to a task, e.g. for spelling, grammar, punctuation, consistency or formatting. It is not necessary to name the authors of material you reference from your task.
Frequency:
    For all regular tasks, and regular tasks only, specify when we would suggest the task be done. Keep as short as possible. Example values: Hourly, Daily, Weekly, Monthly, Quarterly, Annually, When troubleshooting. Other values are okay, but 'as needed' is a bit too vague: make a suggestion. The reader is free to disagree.
Topic:
    One of:
      CAS
      Kubernetes & IT Admin
      Observability
      Organization & Governance
      PostgreSQL
      SAS Administration
      SAS Programming Run-time
Essential:
    Either 'Yes' or '-', meaning recommended but not absolutely essential.
-->

<!-- Note: In other projects we use git branches for work in progress, and submit merge requests/pull requests to move work to the main branch when it is finished.

In this project, we do that too, but we also tag tasks as being Backlog, InProgress, Review or Done, so that we can also generate a status.md file to see the status of all tasks which have been at least added to the backlog. The scripts can reasonably be run in any branch, but we anticipate they are most useful in the validation branch, where they give the writers visibility of tasks that are on each stage of their lifecycle.

There are three types of branch used in this project:
* Personal work branches, named to include the owner's username, e.g. sasgnn_work. Other project contribuors than the owner will rarely look at these branches.
* The validation branch, used by project contributors for sharing work they have done, reviewing tasks, and running the build scripts to update checklist.md, status.md and any other task lists that might be added in future.
* The main branch, which is treated as public. End users - readers - will normally only look at this branch.

Git branches should be used for work on tasks, but changes (at whatever stage in their lifecycle) can be merged early and often into validation. This enables other developers to see what each task's current status is. It is perfectly sensible for tasks in the validation branch to be tagged with any status tag - Backlog, InProgress, Review, or Done. It's fine to have tasks that are placeholders or stubs (Backlog), or are incomplete (InProgress) etc. in any branch.

The status of a task in the main branch of this project, according to the status tag in its .md file is the authoritative record of its status in the task-writing lifecycle.

When enough tasks are in the Done state, the checklist_template.md will be modified to only show tasks that are Done. We do this by changing e.g. strTagFilter=Initial to strTagFilter=Initial;Done for the Initial Tasks table, and similar for the Regular tasks table, per the comments in the checklist_template.md. In the early stages of this project, checklist_template.md does not restrict its tables to showing Done tasks, so that there is something to see.

-->