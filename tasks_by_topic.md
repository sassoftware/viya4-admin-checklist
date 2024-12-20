![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# SAS Viya Administration Tasks by Topic

> Please read the **[Project README](./README.md)** if you have not done so already.

This alternative form of the main [checklist](./checklist.md) lists tasks grouped by topic. In alphabetical order, topics currently used are:

* [CAS](#cas)
* [Kubernetes \& IT Admin](#kubernetes--it-admin)
* [Observability](#observability)
* [Organization \& Governance](#organization--governance)
* [PostgreSQL](#postgresql)
* [SAS Administration](#sas-administration)
* [SAS Programming Run-time](#sas-programming-run-time)


## CAS

> *5 tasks in topic CAS*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0320 | [Secure Default Caslibs, especially the Public Caslib](tasks/secure_default_caslibs.md) | Review and change default access controls on default CAS libraries |  |
| 0330 | [Consider relocating CAS_DISK_CACHE](tasks/relocate_cas_disk_cache.md) | Relocate the CAS_DISK_CACHE for CAS servers |  |
| 0340 | [Configure CAS Allowlist](tasks/configure_cas_allowlist.md) | Configure CAS allowlist for user-defined CAS libraries |  |
| 0350 | [Configure External Access to CAS](tasks/configure_cas_external_access.md) | Configure access to CAS from outside your SAS Viya deployment |  |
| 0650 | [Configure CAS server startup to load data](tasks/cas_server_startup.md) | Configure CAS server startup to load data | Monthly |

## Kubernetes & IT Admin

> *17 tasks in topic Kubernetes & IT Admin*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0010 | [Automate your SAS Viya Deployment Process](tasks/automate_environment_creation.md) | Automate the process of creating and configuring your SAS Viya deployment |  |
| 0020 | [Install the SAS Viya CLI](tasks/install_sas_viya_cli.md) | Ensure you have installed the sas-viya cli and its plugins. |  |
| 0030 | [Develop an update plan](tasks/develop_update_plan.md) | Develop an update plan: outline tasks required before, during and after an update |  |
| 0040 | [Maintain a Secure Password Database](tasks/maintain_password_database.md) | Maintain a secure and encrypted password-protected password database using an appropriate software tool or service |  |
| 0050 | [Update TLS certificates](tasks/encryption_with_public_ca_signed_tls_certificates.md) | Generate new or renew expiring TLS certificates used for encryption of data in transit. |  |
| 0060 | [Load POSIX attributes](tasks/load_posix_attributes.md) | Load POSIX attributes for identities when attributes are not returned from the authentication provider |  |
| 0070 | [Create and Configure User home-directories](tasks/createandconfigure_user_homedirs.md) | Create and configure user-home directories |  |
| 0080 | [Ensure You Have Provided Sufficient Storage for Path-Based Caslibs](tasks/ensure_storage_for_caslibs.md) | Ensure you have provided sufficient filesystem storage of an appropriate type for path-based caslibs. |  |
| 0090 | [Define a Process for Updating External Credentials](tasks/process_for_updating_external_credentials.md) | Define a when and how you will update credentials that are stored in SAS Viya for external systems such as databases, when they change |  |
| 0100 | [Know when to renew your OIDC client secret](tasks/when_to_renew_oidc_client_secret.md) | Open ID Connect uses expiring client secrets with a maximum lifetime of 2 years. If your SAS Viya deployment is configured to use OIDC, ensure that you know when this client secret expires so that you can renew it before it does. |  |
| 0110 | [Configure Open Source Integration](tasks/configure_open_source_integration.md) | Configure open source integration |  |
| 0120 | [Review Tuning Recommendations](tasks/tuning_recommendations.md) | Review SAS Viya platform tuning recommendations and apply as needed |  |
| 0130 | [Configure CORS and CSRF settings](tasks/configure_cors_and_csrf.md) | Configure the SAS Viya platform's Cross-Origin Resource Sharing (CORS) and Cross-Site Request Forgery (CSRF) settings for deployments behind a DNS alias or proxy, and for SAS Visual Analytics |  |
| 0460 | [Renew your SAS Viya License](tasks/update_licenses.md) | Obtain and apply a new SAS Viya platform license before your existing license expires | Annually |
| 0470 | [Update the SAS Viya CLI](tasks/update_sas_viya_cli.md) | Ensure you have installed the sas-viya cli and its plugins | Quarterly |
| 0480 | [Renew your OIDC client secret](tasks/renew_oidc_client_secret.md) | If your SAS Viya deployment is configured to use OIDC, renew your OIDC client secret before it expires. | When secret changes |
| 0490 | [Update External Credentials](tasks/update_external_credentials.md) | When external credentials change, follow your defined process to update them in SAS Viya | When credentials change |

## Observability

> *13 tasks in topic Observability*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0190 | [Select Log & Metric Monitoring and Alerting Solution](tasks/select_monitoring_solution.md) | Choose a log and metric monitoring and alerting solution |  |
| 0200 | [Set Up Monitoring and Alerting](tasks/observability_monitoring_and_alerting.md) | Learn how to deploy, update and use either SAS Viya Monitoring for Kubernetes or a cloud provider's observability tools to leverage logging, monitoring and alerting capabilties in your Viya platform. |  |
| 0210 | [Understand how to Check the Status of Services](tasks/how_to_check_service_status.md) | Ensure you know how to check the status of all SAS Viya services ad hoc at any time |  |
| 0220 | [Configure audit record archival](tasks/audit_record_archival.md) | Configure and schedule the archiving of SAS Viya audit records. |  |
| 0230 | [Enable job to purge archived audit records](tasks/purge_archived_audit_records.md) | Enable the routine purging of archived audit records from the archive location (PV) |  |
| 0500 | [Check the Status of SAS services](tasks/check_service_status.md) | Regularly check the status of SAS services | Daily |
| 0510 | [Monitor Memory, CPU, Network, and Disk Throughput Usage](tasks/monitor_usage.md) | Monitor memory usage, CPU usage, network I/O usage, disk throughput usage, input/output operations per second (IOPS), etc | Daily |
| 0520 | [Monitor Log Messages](tasks/monitor_logs.md) | Monitor log messages | Daily |
| 0530 | [Examine the User Activity Report](tasks/examine_user_activity_report.md) | Examine the user activity report | Weekly |
| 0540 | [Change log levels](tasks/change_log_levels.md) | Change the log threshold for a SAS component or service, to increase or decrease the detail of log messages it produces | When troubleshooting |
| 0550 | [Monitor Storage Space](tasks/monitor_storage_space.md) | Monitor the disk space used for SAS Viya | Weekly |
| 0560 | [Monitor Observability Storage](tasks/monitor_observabilty_storage.md) | Monitor the disk or other storage space used for the log and metric monitoring tools, and other observability tools deployed to monitor SAS Viya | Weekly |
| 0570 | [Stop and Start SAS Viya's Monitoring and Logging components](tasks/stop_and_start_sas_viya_monitoring_for_kubernetes.md) | Ensure you can stop the logging and monitoring solution and that you can start it back up when needed again. | When not in use |

## Organization & Governance

> *5 tasks in topic Organization & Governance*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0140 | [Service Level Agreement](tasks/sla.md) | For enterprise-scale deployments, define a Service Level Agreement (SLA) |  |
| 0150 | [Define your organization’s SAS support team structure, roles, and responsibilities](tasks/define_org_support_structure.md) | Define your organization’s SAS support team structure, roles, and responsibilities |  |
| 0160 | [Premium Support](tasks/premium_support.md) | Consider whether you require premium or customized support for your SAS deployment |  |
| 0170 | [Security Policy](tasks/security_policy.md) | Write and maintain a security policy that covers the SAS Viya deployment |  |
| 0180 | [Authorization Model](tasks/authorization_model.md) | Write and maintain a security model or an authorization model |  |

## PostgreSQL

> *2 tasks in topic PostgreSQL*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0670 | [Manage content stored in PostgreSQL](tasks/manage_postgresql_content.md) | Manage content stored in PostgresQL | Monthly |
| 0680 | [Maintain SAS Infrastructure Data Server](tasks/maintain_postgresql_server.md) | Perform routine maintenance on the SAS Infrastructure Data Server | Monthly |

## SAS Administration

> *16 tasks in topic SAS Administration*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0240 | [Validate your SAS Viya Deployment](tasks/validate_deployment.md) | Define a set of tests to validate that your SAS Viya deployment is functioning correctly |  |
| 0250 | [Define a backup and restore strategy](tasks/backup_and_restore.md) | Define a backup and restore strategy |  |
| 0260 | [Know how to Contact SAS Technical Support for Help](tasks/contact_SAS_technical_support.md) | Ensure all SAS platform administration staff know how to contact SAS Technical Support for help |  |
| 0270 | [Identify Components of SAS and Third-Party Software](tasks/identify_viya_components.md) | Ensure you can identify the components of SAS and third-party software that make up SAS Viya |  |
| 0280 | [Decide approach to applying updates](tasks/decide_update_approach.md) | Decide how and when your SAS Viya software will be updated |  |
| 0290 | [Configure SAS Studio Preferences](tasks/configure_sas_studio_preferences.md) | Configure SAS Studio Preferences |  |
| 0300 | [Define a Process for Onboarding and Offboarding Users](tasks/process_for_onboarding_and_offboarding_users.md) | Document any steps that must be performed when new users are onboarded and offboarded |  |
| 0310 | [Secure the sasboot password](tasks/secure_sasboot_password.md) | Disable the sasboot password reset feature after you have finished setting up identities and initial administrators |  |
| 0450 | [Design and Maintain a Schedule of SAS Administration Housekeeping Activities](tasks/maintain_housekeeping_schedule.md) | Design and maintain a schedule of SAS Viya platform administration housekeeping activities, specifying when regular tasks should be performed. |  |
| 0580 | [Onboard and Offboard Users](tasks/onboard_and_offboard_users.md) | Onboard new users and offboard old users | Weekly |
| 0590 | [Keep your Software Current](tasks/keep_software_current.md) | Keep your software current with patch and version updates to stay within Standard Support guidelines. | Monthly |
| 0600 | [Regularly Re-Validate your SAS Viya Deployment](tasks/validate_deployment_regularly.md) | Run a set of tests to validate that your SAS Viya deployment is functioning correctly | Weekly |
| 0610 | [Periodically Run an Inventory Scan on the Viya Environment](tasks/inventory_scan.md) | Periodically Run an Inventory Scan on the Viya Environment | Monthly |
| 0620 | [Stop and Start SAS Viya software](tasks/stop_and_start_viya.md) | Ensure you can scale your SAS Viya deployment to zero, and that you can scale it back up when needed again. | When not in use |
| 0630 | [Inspect the Status of Scheduled Jobs](tasks/inspect_job_status.md) | Inspect the status of scheduled jobs | Daily |
| 0640 | [Test the Process to Restore From Backups](tasks/test_restore_process.md) | Periodically test the process to restore from backups | Monthly |

## SAS Programming Run-time

> *10 tasks in topic SAS Programming Run-time*

| # ▴ | Title | Description | Frequency |
|---|---|---|---|
| 0360 | [Set location for SAS Work and other Programming Run-Time Temporary Files](tasks/move_sas_work_and_spre_temporary_files_location.md) | Move SAS Work and other Programming Run-Time Temporary Files to a better location than the default |  |
| 0370 | [Configure Common Programming Run-Time Autoexec Statements](tasks/common_programming_run-time_options.md) | Configure statements in SAS Programming Run-Time Autoexec code blocks, to set commonly used SAS options for macro programming, performance tuning, use of mail servers and pre-assigning SAS libraries. |  |
| 0380 | [Modify Launcher and SAS Programming Run-Time Server Contexts](tasks/modify_programming_launcher_server_contexts.md) | Modify Launcher and Server contexts for SAS Compute Server, SAS Connect Server and SAS Batch Server |  |
| 0390 | [Define Library Connection Data Sources as a Resource in SAS Programming Run-Time Contexts](tasks/manage_connections_to_data_sources.md) | Compute, Connect and Batch contexts can be associated with Required Resources, the first of which is a Library Connection. |  |
| 0400 | [Configure lockdown for SAS Programming run-time servers](tasks/configure_lockdown.md) | Configure lockdown for SAS Programming Run-Time servers |  |
| 0410 | [Configure Programming Allowlist](tasks/configure_programming_allowlist.md) | Configure SAS Programming Run-Time for user-defined paths |  |
| 0420 | [Configure umask for SAS Programmning run-time servers](tasks/configure_programming_run-time_umask.md) | Configure umask to e.g. 0002 for SAS Programming Run-Time servers, so that files created by users (including datasets in path-based libraries) are read-write for members of the user's primary POSIX group |  |
| 0430 | [Set User Process Limit](tasks/set_user_process_limit.md) | Set the maximum number of launched compute, connect or batch programming run-time pods each user may run simultaneously |  |
| 0440 | [Tune the Programming Run-Time](tasks/tune_programming_run-time.md) | Tune the SAS Viya Platform Programming Run-time for better performance with your workload |  |
| 0660 | [Monitor Compute Sessions](tasks/monitor_compute_sessions.md) | Use the sas-viya CLI, log and metric monitoring tools to monitor compute sessions | Daily or as often as necessary |

</br>Generated by build_from_template.py on: 19 Dec 2024 13:58:07.</br>
