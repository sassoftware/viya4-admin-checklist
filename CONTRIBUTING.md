# How to Contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

## Contents   <!-- omit in toc -->
* [Contributor License Agreement](#contributor-license-agreement)
* [Code reviews](#code-reviews)
* [How to create or modify a task](#how-to-create-or-modify-a-task)
  * [Examples](#examples)
  * [Link to the latest documentation](#link-to-the-latest-documentation)
  * [Links must work outside SAS](#links-must-work-outside-sas)


## Contributor License Agreement

Contributions to this project must be accompanied by a signed
[Contributor Agreement](ContributorAgreement.txt).
You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as
part of the project.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## How to create or modify a task

To write a new task, or to update an existing task, follow the guidance below.

For **contributors**, or users making a their own custom version of the project, if you add or change specific properties of tasks (filename, title, SortString, Description or Tags) you can run the scripts which update documents like the top-level [checklist.md](checklist.md), e.g. [scripts/build_all.py](scripts/build_all.py) (or [scripts/build_from_template.py](scripts/build_from_template.py)). These scripts have usage instructions in their header comments.

### Examples

This project is a checklist of tasks, and the files containing the descriptions of those tasks are its principal deliverable.

Each task is defined in a single [GitHub Flavored Markdown](https://github.github.com/gfm/) file in the tasks subdirectory of the project root. Some tasks are one of a pair, with a one-off Initial task to learn how to do something or set some feature up, and a related Regular task to do that thing, or maintain that feature regularly over time.

Each task file should have these required and optional features:

1. **[Required]**: Give tasks a filename which is unique, fairly short, identifies the main concept of the task and has a .md file extension. Tasks are referred to by their filename (not by their SortString), and so it is preferable not to change a tasks's filename once it has been merged into the project's <code>main</code> branch. If you do change a task's filename, you must also find and similarly change any internal links to the task within this project.

1. **[Required]**: A single level 1 [ATX Heading](https://github.github.com/gfm/#atx-headings) near the top of the file, like this: <code># Task Title</code>

    > The text following the '<code># </code>' becomes the task's title when it is listed in tables of contents. It is rendered in HTML as <code>\<h1\>Task Title\<\/h1\></code>.
    >
    > There should be no more than one level 1 heading in a task file. There can be any number of level 2 to level 6 headings in a task.

1. **[Required]**: An HTML comment block containing a series of name value pairs separated by a colon, like this:
    <pre>
    &lt;!--
    SortString: 042
    Description: The Answer to Life, the Universe and Everything
    Tags: Initial,InProgress,New
    Topic: SAS Administration
    Essential: -
    Authors: Charles Babbage,Douglas Adams,Tim Berners-Lee,John Gruber
    --&gt;</pre>

    The following key-value pairs should all be included, each with the key and all its comma-separated values on one line:

    | Name | Notes on values |
    |------|-----------------|
    | SortString | Used for sorting tasks within checklist tables.</br>Not a key. Avoid written references to tasks by their SortString. Instead, refer to tasks by their markdown filename which should preferably remain constant.</br>*Note: in previous checklists we often referred to tasks by their id, but this is now avoided because task SortStrings are expected to change from time to time. Changing a task's SortString value should never break a reference to the task.*</br>Intended to be used for sorting tasks in a checklist.</br>May change arbitrarily when we re-order tasks.</br>Suggest 3-digit number. |
    | Description | A short description of the task, typically no more than 200-300 characters. If you need a longer description, consider whether this task should be split into two or more smaller tasks. |
    | Tags | A comma-separated list of tags, all on one line, used for filtering tables of content in the checklist.md and other documents generated from templates. The order of these tags is not important.</br>Other tag groups may be added in future, and tasks may be given tags from a new tag group retrospectively.</br></br>Include exactly one tag from each of the following **required** groups:</br><ul><li>`Initial` or `Regular` (temporal adjective tag - if you intend both make two tasks, one for 'define how to do it' and one for 'do it')</li><li>`Backlog`, `InProgress`, `Review` or `Done` status tag for tracking progress in task development. Only tasks tagged as `Done` appear in the main [checklist](checklist.md).</li><li>`Legacy` or `New` for the tasks's provenance. For tasks that had equivalents in earlier checklists for SAS Viya 3 and SAS 9. The detail of these tasks in SAS Viya 2020.1 and later may differ very significantly from their earlier equivalents.</li></ul> |
    | Authors | A comma-separated list full names (*firstname lastname*) of authors who wrote a substantial portion of the words in the task, even if they were copied here from another source. Use this tag - with the author's consent if possible - to acknowledge someone's contribution to the task content and avoid taking undue credit for another author's work. Adding your own name is optional - omit yours if you wish, though git and GitHub can generally identify your contibution to some extent. You should not add your name to the authors list if you only made minor edits to a task, e.g. for spelling, grammar, punctuation, consistency or formatting. It is not necessary to name the authors of material you reference from your task. |
    | Frequency | For all regular tasks, and regular tasks only, specify when we would suggest the task be done. Keep as short as possible. Example values: Hourly, Daily, Weekly, Monthly, Quarterly, Annually, When troubleshooting. Other values are okay, but 'as needed' is a bit too vague: make a suggestion. The reader is free to disagree. |
    | Topic | One of:</br><ul><li>CAS</li><li>Kubernetes & IT Admin</li><li>Observability</li><li>Organization & Governance</li><li>PostgreSQL</li><li>SAS Administration</li><li>SAS Programming Run-time</li></ul> |
    | Essential | One of</br><ul><li>Yes</li><li>-</li></ul>The value '-' means recommended but not absolutely essential, but at a glance it is easier to see the rows with a yes if the rest are marked '-' instead of 'No' or 'Recommended'. |

1. **[Optional]** A `When:` line.

    > When should an administrator (or someone they coordinate with) do this task? A `When:` line is optional but usually included. Omit it if there is no particular time you think the task should be done. However, there is a 'best' time to perform most tasks in the checklist. If you do not include a 'When:' line, someone else may do so later.
    >
    > Examples:
    > * When: After platform changes
    > * When: Before and/or after platform changes and in tandem with organizational changes
    > * When: At the beginning and end of a period of troubleshooting activity
    > * When: Regularly per housekeeping schedule
    >
    > You are free to describe when the task should be done in your own words, if none of the examples above are appropriate to your task.

1. **[Optional]**: Above each of two or more separate ideas, a level 2 to 6 [ATX Heading](https://github.github.com/gfm/#atx-headings).

    * A level 2 subheading looks like this: <code>## Brief description of part of the task</code>
    * A level 3 subheading looks like this: <code>### Brief description of a sub-part the task or subordinate concept</code>
    * ...and so on.

    Subheadings should be different from the task title, and are best included either:

    * if you need multiple subheadings to separate ideas that are part of the same tasks, or
    * if your task represents a single idea, but the task title doesn't adequately describe the task. For example, the title "Security Policy" is pleasingly short and the task document only presents one idea, but the task has one level 2 subheading ("Write and maintain a security policy that covers the SAS Viya deployment"). There are no other level 2 subheadings. This neatly keeps the table of contents entry for the task short, but explains what the task's idea is more clearly.

    If your task title adequately describes the task and the task only presents one idea, omit level 2 and lower subheadings.

1. **[Required]**: Body text describing what the task is, why you should consider doing it and where to find instructions. In order of preference from most to least preferable, you may:
      * Refer to existing instructions, when suitable instructions are publically available. If the existing instructions are only available in the form of unofficial or community-created content such as a blog post or video, consider asking for official SAS public documentation to be written to cover the topic. Not every topic we may write about will be suitable for official SAS public documentation.
      * When suitable instructions are NOT publically available, ask for official documentation to be written and/or write a blog post or other article describing the task and how to do it, and publish it, e.g. in the SAS Communities Library. Then, write (or finish writing) a task here and refer to that post (e.g. using a permalink) in the body the task. If the instructions need to be updated, update your existing post or publish a new one, and where necessary update the references in the task so that they direct the reader to a current version of the instructions.
      * Include instructions directly in the task's body text. This may seem easier, but it has some disadvantages, and is not the preferred approach. Good instructions take time to write and must be maintained. We think it is best to provide instructions in other, established locations, and not to turn this checklist into yet another source of detailed instructions.

1. **[Optional]** One or more `See also:` lines.

    > Your task's body text will usually contain one or more references to other resources. If you like to include links in your text that is fine. But a `See also:` line is another option, which may suit tasks which refer to lists of resources when you do not need to write a story about them. Include a word or short phrase inside square brackets at the end of the link to indicate what sort of resource it is.
    >
    > Here are some examples:
    >
    > * See also: [onboard_and_offboard_users.md](./onboard_and_offboard_users.md) [Task]
    > * See also: The [Jobs and Flows Page](https://documentation.sas.com/doc/en/sasadmincdc/default/evfun/n0b9cf8ru47gp6n1lvamxqwbr3by.htm) in the SAS Viya Environment Manager User's Guide [Doc]
    > * See also: [SAS Demo | Modify non-Default CAS Server Topology in Your Viya Deployment](https://www.youtube.com/watch?v=WxUXaTtZpSE) [Video]
    >
    > A `See also:` line right before the link back to the top-level checklist is a good way to 'pair' your task with a related task, e.g. between a pair of tasks where there is a one-time initial 'set a thing up or learn how to do a thing' task, and an corresponding regular 'do the thing' task. Each task can have a `See also:` line referring the reader to the other in the pair.

1. **[Required]**: A link back to the top-level checklist.md. The Markdown for this link looks like this:

    `[Back to checklist](../checklist.md)`

### Link to the latest documentation

If your task references SAS documentation, edit URLs at `go.documentation.sas.com`, replace the version number in the URL (e.g. `/v_031/`) with 'default' (e.g. `/default/`) to link to the latest version of the documentation. So, for example the URL `https://go.documentation.sas.com/doc/en/sasadmincdc/v_037/k8sag/p1it185kd37v25n1aoybu799tpk4.htm` becomes `https://go.documentation.sas.com/doc/en/sasadmincdc/default/k8sag/p1it185kd37v25n1aoybu799tpk4.htm`. If a new version of this doc page is released in future, the modified URL with 'default' instead of a version number should redirect to the latest version.

### Links must work outside SAS

All URLs you link to should be accessible outside SAS. Avoid linking to pages on SAS-internal sites, such as `sww.sas.com`.
