![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure Common Programming Run-Time Autoexec Statements

<!--
SortString: 0370
Description: Configure statements in SAS Programming Run-Time Autoexec code blocks, to set commonly used SAS options for macro programming, performance tuning, use of mail servers and pre-assigning SAS libraries.
Tags: Initial,New,Done
Topic: SAS Programming Run-time
Essential: Yes
Authors: David Stern
-->
When: After platform changes

It is common to customize your SAS Programming Run-Time environment to better suit your organization's particular needs, using some combination of useful SAS statemments in autoexec code blogs. These statements are executed as SAS sessions are initialized, so that their effects are already in place by the time your users' program statements run.

## What autoexec statements should be added where?

Consider:

* Which autoexec statements are useful and represent good value for their resource costs (e.g. do they increase session startup time, consume memory etc.) ?
* To which SAS Programming Run-Time Sessions do you wish them to apply - what is their scope?

## Example autoexec statements - this is NOT a list of required or recommended statements

The following SAS statements are examples of the kind of statements commonly used by customers in autoexec code. This is NOT a list of recommended statements - you do not have to apply each of these in your environment, and you may not like what some of them do! The list of examples below is intended to illustrate the variety and breadth of things an administrator can adjust if desired.

| Topic | Examples | What these can be used for |
| ----- | -------- | -------------------------- |
| Custom SAS macros | `%macro exist(dsn);`</br>`%global exist;`</br>`%if %sysfunc(exist(&dsn)) %then`</br>&nbsp;&nbsp;&nbsp;&nbsp;`%let exist=YES;`</br>`%else %let exist=NO;`</br>`%mend exist;`| SAS macros that are widely used in many of your SAS programs. Instead of defining the same macro in many programs, why not add them directly, or via some other method ([%include](https://blogs.sas.com/content/sastraining/2015/07/07/macros-tip-include-vs-macro-language/), [autocall macro libraries](https://go.documentation.sas.com/doc/en/pgmsascdc/default/mcrolref/n1o5fkxq0gqdpcn1xs3ksdks69tf.htm)) to all Programming Run-Time sessions where they might be useful?</br></br>See more examples for inspiration in [Advanced Macro Topics: Utilities and Examples](https://support.sas.com/resources/papers/proceedings/proceedings/sugi23/Advtutor/p49.pdf) [Paper], or search the web for something like "useful SAS utility macros". |
| FULLSTIMER option | `option fullstimer;`</br></br>(or `option nofullstimer;`) | The SAS System provides the FULLSTIMER option to collect performance statistics on each SAS step, and for the job as a whole and place them in the SAS log. This makes SAS program log output longer and more verbose.</br></br>See [FULLSTIMER SAS Option](https://support.sas.com/rnd/scalability/tools/fullstim/index.html) for a detailed explanation. |
| SAS Macro Debugging Options and `%put` statements | `option mlogic;`</br>`option mprint;`</br>`option symbolgen;`</br></br>(or `option nomlogic;`</br>`option nomprint;`</br>`option nosymbolgen;`)</br></br>`%put _all_;`</br></br>`%put `*macro_variable*`;`| Prints detail of what macro calls resolve to and the values of  macro variables at run time to the SAS program logs. Makes macro log output more verbose. </br></br>See [Debugging Techniques](https://go.documentation.sas.com/doc/en/pgmsascdc/default/mcrolref/p0otchmpun25uan1hxsxld63s6e8.htm) [Doc] |
| SORTSIZE= System Option and MEMSIZE System Option | `option sortsize=2G;`</br></br>`option memsize max;`| See [SORTSIZE= System Option](https://go.documentation.sas.com/doc/en/pgmsascdc/default/lesysoptsref/n0ipa8xt1ma3h7n1wqjqr99679pg.htm) and [MEMSIZE System Option](https://go.documentation.sas.com/doc/en/pgmsascdc/default/lesysoptsref/n09y5anvvpzrmnn0ztkyf59qgzvr.htm), and do not modify these values until you understand what you are doing. If used correctly, these tuning parameters can greatly improve program performance and stability. If used incorrrectly they can adversely affect performance and stability. </br></br>*Must be used carefully in combination with adjustments to memory requests and limits in Programming Run-Time PodTemplates* |
| Mail server options | `options emailsys=smtp emailhost=mailhost.company.com emailport=25;` | Configure corporate mail server access, to allow SAS programs to send email. End users may not know what values to provide for these options, whereas a SAS Administrator can find out and set them for everyone. |
| Pre-assign commonly-used libraries | `libname hrdata "/gelcontent/gelcorp/hr/data";` | Assign a library at the compute context, or global compute server level.</br></br>This method of globally pre-assigning a library is one of several valid methods available to the SAS Administrator. |


## Where will you add your preferred autoexec statements?

The task [Modify Launcher and SAS Programming Run-Time Server Contexts](./modify_programming_launcher_server_contexts.md) [Task] describes several places where configurations settings can be applied. In this task, we focus primarily on:

* Global Compute/Connect/Batch Server configuration instances' **autoexec** code blocks
* Compute/Connect/Batch contexts' **autoexec** code blocks

### Globally for a service

If you want all compute, connect or batch sessions to be impacted by an autoexec statement, you should place it in the respective server's configuration instance defining its autoexec code.

See [Server Configuration Instances](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calsrvpgm/n08002viyaprgmsrvs00000admin.htm) for a list of configuration instances, and notice those for autoexec_code in particular.

Step by step instructions for how to modify any of them are given in [Edit Configuration Instances](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p19rd04uy9qnlkn10vwoajl66nxq.htm#n0p8gxdvtd6o8un16ky5a8z1u7io) - scroll down a little from that section heading to see the steps.

> **Note**: SAS Viya has no 'universal' autoexec code block which would apply to all three of compute, connect and batch servers, but with a bit of effort, you can make your own. If you have a shared volume mounted into each type of server, you could place a file containing your 'global' autoexec statements on that shared volume, with appropriate read-only permissions for most users, and %include the same file in each of your deployment's compute, connect and/or batch autoexec code blocks.

## For a single compute, connect or batch context

If you want only compute, connect or batch sessions running under specific contexts to be impacted by an autoexec statement, place the statement in the relevant context's specific autoexec code block.

Step by step instructions for how to modify any of them are given in [Edit a Context](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p1dkdadd9rkbmdn1fpv562l2p5vy.htm#p1pknmcnbw3s3in1t6bnhmwh2x57) in the SAS Environment Manager's user guide.

You may alternatively prefer to create a new Compute, Connect or Batch context. Contexts can be available to all authenticated users, or to selected users only. See:

* [Create a Compute Context](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p1dkdadd9rkbmdn1fpv562l2p5vy.htm#n0bw1won3jn0axn1brl67tielej1)
* [Create a Batch Context](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p1dkdadd9rkbmdn1fpv562l2p5vy.htm#n1jfwrc1erypt2n1vizqmgt4g9r6)
* [Create a Connect Context](https://go.documentation.sas.com/doc/en/sasadmincdc/default/evfun/p1dkdadd9rkbmdn1fpv562l2p5vy.htm#n0hv55468frsy1n182u5uwwqbvgz)

See also [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog], which describes the places where configurations settings can be applied, and discusses why you might choose each one.

[Back to checklist](../checklist.md)