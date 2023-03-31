![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# SAS Viya Administration Checklist

> Please read the **[Project README](./README.md)** if you have not done so already.

This checklist lists both [initial](#initial-task-checklist) tasks, and [regular](#regular-task-checklist) tasks.

Alternatively, view the same [tasks grouped by topic](./tasks_by_topic.md).

See also:

* [Recommended Tools](./docs/Recommended_SAS_admin_tools.md)
* [Recommended Skills and Knowledge](./docs/Recommended_SAS_admin_skills_and_knowledge.md)

## Initial Task Checklist

This table lists larger tasks. You should consider performing them once. You
should revisit these tasks if major elements of SAS Viya change or your business
requirements change. Tasks in this checklist do not need to be repeated on a
regular scheduled basis.




> *45 tasks tagged as Initial;Done*

| # ▴ | Title | Description | Topic | Essential |
|---|---|---|---|---|
| 0010 | [Automate your SAS Viya Deployment Process](tasks/automate_environment_creation.md) | Automate the process of creating and configuring your SAS Viya deployment | Kubernetes & IT Admin | Yes |
| 0020 | [Install the SAS Viya CLI](tasks/install_sas_viya_cli.md) | Ensure you have installed the sas-viya cli and its plugins. | Kubernetes & IT Admin | - |
| 0030 | [Develop an update plan](tasks/develop_update_plan.md) | Develop an update plan: outline tasks required before, during and after an update | Kubernetes & IT Admin | Yes |
| 0040 | [Maintain a Secure Password Database](tasks/maintain_password_database.md) | Maintain a secure and encrypted password-protected password database using an appropriate software tool or service | Kubernetes & IT Admin | - |
| 0050 | [Use customer-provided certificates](tasks/encryption_with_customer_provided_certificates.md) | Generate new or renew expiring TLS certificates used for encryption of data in transit. | Kubernetes & IT Admin | - |
| 0060 | [Load POSIX attributes](tasks/load_posix_attributes.md) | Load POSIX attributes for identities when attributes are not returned from the authentication provider | Kubernetes & IT Admin | - |
| 0070 | [Create and Configure User home-directories](tasks/createandconfigure_user_homedirs.md) | Create and configure user-home directories | Kubernetes & IT Admin | - |
| 0080 | [Ensure You Have Provided Sufficient Storage for Path-Based Caslibs](tasks/ensure_storage_for_caslibs.md) | Ensure you have provided sufficient filesystem storage of an appropriate type for path-based caslibs. | Kubernetes & IT Admin | - |
| 0090 | [Define a Process for Updating External Credentials](tasks/process_for_updating_external_credentials.md) | Define a when and how you will update credentials that are stored in SAS Viya for external systems such as databases, when they change | Kubernetes & IT Admin | - |
| 0100 | [Know when to renew your OIDC client secret](tasks/when_to_renew_oidc_client_secret.md) | Open ID Connect uses expiring client secrets with a maximum lifetime of 2 years. If your SAS Viya deployment is configured to use OIDC, ensure that you know when this client secret expires so that you can renew it before it does. | Kubernetes & IT Admin | - |
| 0110 | [Configure Open Source Integration](tasks/configure_open_source_integration.md) | Configure open source integration | Kubernetes & IT Admin | - |
| 0120 | [Review Tuning Recommendations](tasks/tuning_recommendations.md) | Review SAS Viya platform tuning recommendations and apply as needed | Kubernetes & IT Admin | - |
| 0130 | [Configure CORS and CSRF settings](tasks/configure_cors_and_csrf.md) | Configure the SAS Viya platform's Cross-Origin Resource Sharing (CORS) and Cross-Site Request Forgery (CSRF) settings for deployments behind a DNS alias or proxy, and for SAS Visual Analytics | Kubernetes & IT Admin | - |
| 0140 | [Service Level Agreement](tasks/sla.md) | For enterprise-scale deployments, define a Service Level Agreement (SLA) | Organization & Governance | - |
| 0150 | [Define your organization’s SAS support team structure, roles, and responsibilities](tasks/define_org_support_structure.md) | Define your organization’s SAS support team structure, roles, and responsibilities | Organization & Governance | - |
| 0160 | [Premium Support](tasks/premium_support.md) | Consider whether you require premium or customized support for your SAS deployment | Organization & Governance | - |
| 0170 | [Security Policy](tasks/security_policy.md) | Write and maintain a security policy that covers the SAS Viya deployment | Organization & Governance | - |
| 0180 | [Authorization Model](tasks/authorization_model.md) | Write and maintain a security model or an authorization model | Organization & Governance | Yes |
| 0190 | [Select Log & Metric Monitoring and Alerting Solution](tasks/select_monitoring_solution.md) | Choose a log and metric monitoring and alerting solution | Observability | Yes |
| 0200 | [Set Up Monitoring and Alerting](tasks/observability_monitoring_and_alerting.md) | Learn how to deploy, update and use either SAS Viya Monitoring for Kubernetes or a cloud provider's observability tools to leverage logging, monitoring and alerting capabilties in your Viya platform. | Observability | Yes |
| 0210 | [Understand how to Check the Status of Services](tasks/how_to_check_service_status.md) | Ensure you know how to check the status of all SAS Viya services ad hoc at any time | Observability | - |
| 0220 | [Configure audit record archival](tasks/audit_record_archival.md) | Configure and schedule the archiving of SAS Viya audit records. | Observability | - |
| 0230 | [Enable job to purge archived audit records](tasks/purge_archived_audit_records.md) | Enable the routine purging of archived audit records from the archive location (PV) | Observability | - |
| 0240 | [Validate your SAS Viya Deployment](tasks/validate_deployment.md) | Define a set of tests to validate that your SAS Viya deployment is functioning correctly | SAS Administration | - |
| 0250 | [Define a backup and restore strategy](tasks/backup_and_restore.md) | Define a backup and restore strategy | SAS Administration | Yes |
| 0260 | [Know how to Contact SAS Technical Support for Help](tasks/contact_SAS_technical_support.md) | Ensure all SAS platform administration staff know how to contact SAS Technical Support for help | SAS Administration | - |
| 0270 | [Identify Components of SAS and Third-Party Software](tasks/identify_viya_components.md) | Ensure you can identify the components of SAS and third-party software that make up SAS Viya | SAS Administration | - |
| 0280 | [Decide approach to applying updates](tasks/decide_update_approach.md) | Decide how and when your SAS Viya software will be updated | SAS Administration | - |
| 0290 | [Configure SAS Studio Preferences](tasks/configure_sas_studio_preferences.md) | Configure SAS Studio Preferences | SAS Administration | - |
| 0300 | [Define a Process for Onboarding and Offboarding Users](tasks/process_for_onboarding_and_offboarding_users.md) | Document any steps that must be performed when new users are onboarded and offboarded | SAS Administration | - |
| 0310 | [Secure the sasboot password](tasks/secure_sasboot_password.md) | Disable the sasboot password reset feature after you have finished setting up identities and initial administrators | SAS Administration | - |
| 0320 | [Secure Default Caslibs, especially the Public Caslib](tasks/secure_default_caslibs.md) | Review and change default access controls on default CAS libraries | CAS | - |
| 0330 | [Consider relocating CAS_DISK_CACHE](tasks/relocate_cas_disk_cache.md) | Relocate the CAS_DISK_CACHE for CAS servers | CAS | Yes |
| 0340 | [Configure CAS Allowlist](tasks/configure_cas_allowlist.md) | Configure CAS allowlist for user-defined CAS libraries | CAS | - |
| 0350 | [Configure External Access to CAS](tasks/configure_cas_external_access.md) | Configure access to CAS from outside your SAS Viya deployment | CAS | - |
| 0360 | [Set location for SAS Work and other Programming Run-Time Temporary Files](tasks/move_sas_work_and_spre_temporary_files_location.md) | Move SAS Work and other Programming Run-Time Temporary Files to a better location than the default | SAS Programming Run-time | Yes |
| 0370 | [Configure Common Programming Run-Time Autoexec Statements](tasks/common_programming_run-time_options.md) | Configure statements in SAS Programming Run-Time Autoexec code blocks, to set commonly used SAS options for macro programming, performance tuning, use of mail servers and pre-assigning SAS libraries. | SAS Programming Run-time | - |
| 0380 | [Modify Launcher and SAS Programming Run-Time Server Contexts](tasks/modify_programming_launcher_server_contexts.md) | Modify Launcher and Server contexts for SAS Compute Server, SAS Connect Server and SAS Batch Server | SAS Programming Run-time | - |
| 0390 | [Define Library Connection Data Sources as a Resource in SAS Programming Run-Time Contexts](tasks/manage_connections_to_data_sources.md) | Compute, Connect and Batch contexts can be associated with Required Resources, the first of which is a Library Connection. | SAS Programming Run-time | - |
| 0400 | [Configure lockdown for SAS Programming run-time servers](tasks/configure_lockdown.md) | Configure lockdown for SAS Programming Run-Time servers | SAS Programming Run-time | - |
| 0410 | [Configure Programming Allowlist](tasks/configure_programming_allowlist.md) | Configure SAS Programming Run-Time for user-defined paths | SAS Programming Run-time | - |
| 0420 | [Configure umask for SAS Programmning run-time servers](tasks/configure_programming_run-time_umask.md) | Configure umask to e.g. 0002 for SAS Programming Run-Time servers, so that files created by users (including datasets in path-based libraries) are read-write for members of the user's primary POSIX group | SAS Programming Run-time | - |
| 0430 | [Set User Process Limit](tasks/set_user_process_limit.md) | Set the maximum number of launched compute, connect or batch programming run-time pods each user may run simultaneously | SAS Programming Run-time | - |
| 0440 | [Tune the Programming Run-Time](tasks/tune_programming_run-time.md) | Tune the SAS Viya Platform Programming Run-time for better performance with your workload | SAS Programming Run-time | - |
| 0450 | [Design and Maintain a Schedule of SAS Administration Housekeeping Activities](tasks/maintain_housekeeping_schedule.md) | Design and maintain a schedule of SAS Viya platform administration housekeeping activities, specifying when regular tasks should be performed. | SAS Administration | Yes |

## Regular Task Checklist

This table lists smaller tasks that should be repeated on a regular basis. See the suggested frequency table for an example of when you might run each of these tasks.

> *22 tasks tagged as Regular;Done*

| # ▴ | Title | Description | Frequency | Topic | Essential |
|---|---|---|---|---|---|
| 0460 | [Renew your SAS Viya License](tasks/update_licenses.md) | Obtain and apply a new SAS Viya platform license before your existing license expires | Annually | Kubernetes & IT Admin | - |
| 0470 | [Update the SAS Viya CLI](tasks/update_sas_viya_cli.md) | Ensure you have installed the sas-viya cli and its plugins | Quarterly | Kubernetes & IT Admin | - |
| 0480 | [Renew your OIDC client secret](tasks/renew_oidc_client_secret.md) | If your SAS Viya deployment is configured to use OIDC, renew your OIDC client secret before it expires. | When secret changes | Kubernetes & IT Admin | - |
| 0490 | [Update External Credentials](tasks/update_external_credentials.md) | When external credentials change, follow your defined process to update them in SAS Viya | When credentials change | Kubernetes & IT Admin | - |
| 0500 | [Check the Status of SAS services](tasks/check_service_status.md) | Regularly check the status of SAS services | Daily | Observability | - |
| 0510 | [Monitor Memory, CPU, Network, and Disk Throughput Usage](tasks/monitor_usage.md) | Monitor memory usage, CPU usage, network I/O usage, disk throughput usage, input/output operations per second (IOPS), etc | Daily | Observability | - |
| 0520 | [Monitor Log Messages](tasks/monitor_logs.md) | Monitor log messages | Daily | Observability | - |
| 0530 | [Examine the User Activity Report](tasks/examine_user_activity_report.md) | Examine the user activity report | Weekly | Observability | - |
| 0540 | [Change log levels](tasks/change_log_levels.md) | Change the log threshold for a SAS component or service, to increase or decrease the detail of log messages it produces | When troubleshooting | Observability | - |
| 0550 | [Monitor Storage Space](tasks/monitor_storage_space.md) | Monitor the disk space used for SAS Viya | Weekly | Observability | - |
| 0560 | [Monitor Observability Storage](tasks/monitor_observabilty_storage.md) | Monitor the disk or other storage space used for the log and metric monitoring tools, and other observability tools deployed to monitor SAS Viya | Weekly | Observability | - |
| 0570 | [Stop and Start SAS Viya's Monitoring and Logging components](tasks/stop_and_start_sas_viya_monitoring_for_kubernetes.md) | Ensure you can stop the logging and monitoring solution and that you can start it back up when needed again. | When not in use | Observability | - |
| 0580 | [Onboard and Offboard Users](tasks/onboard_and_offboard_users.md) | Onboard new users and offboard old users | Weekly | SAS Administration | - |
| 0590 | [Keep your Software Current](tasks/keep_software_current.md) | Keep your software current with patch and version updates to stay within Standard Support guidelines. | Monthly | SAS Administration | - |
| 0600 | [Regularly Re-Validate your SAS Viya Deployment](tasks/validate_deployment_regularly.md) | Run a set of tests to validate that your SAS Viya deployment is functioning correctly |  | SAS Administration | - |
| 0620 | [Stop and Start SAS Viya software](tasks/stop_and_start_viya.md) | Ensure you can scale your SAS Viya deployment to zero, and that you can scale it back up when needed again. | When not in use | SAS Administration | - |
| 0630 | [Inspect the Status of Scheduled Jobs](tasks/inspect_job_status.md) | Inspect the status of scheduled jobs | Daily | SAS Administration | - |
| 0640 | [Test the Process to Restore From Backups](tasks/test_restore_process.md) | Periodically test the process to restore from backups | Monthly | SAS Administration | - |
| 0650 | [Configure CAS server startup to load data](tasks/cas_server_startup.md) | Configure CAS server startup to load data | Monthly | CAS | Yes |
| 0660 | [Monitor Compute Sessions](tasks/monitor_compute_sessions.md) | Use the sas-viya CLI, log and metric monitoring tools to monitor compute sessions | Daily or as often as necessary | SAS Programming Run-time | - |
| 0670 | [Manage content stored in PostgreSQL](tasks/manage_postgresql_content.md) | Manage content stored in PostgresQL | Monthly | PostgreSQL | - |
| 0680 | [Maintain SAS Infrastructure Data Server](tasks/maintain_postgresql_server.md) | Perform routine maintenance on the SAS Infrastructure Data Server | Monthly | PostgreSQL | - |

</br>Generated by build_from_template.py on: 20 Mar 2023 21:08:53.</br>
