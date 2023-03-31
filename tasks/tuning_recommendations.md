![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Review Tuning Recommendations

<!--
SortString: 0120
Description: Review SAS Viya platform tuning recommendations and apply as needed
Tags: New,Initial,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Scott McCauley
-->
When: After platform changes

## Review tuning recommendations and apply as needed

After you have deployed the SAS Viya platform, you might need to modify individual components for scalability and performance. The [SAS Viya Platform Administration: Tuning](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/titlepage.htm) guide describes tuning methodologies that are appropriate for the SAS Viya platform in a Kubernetes environment.

Tuning for scalability often targets the ability of a component to adapt to a greater or lesser intensity of use or volume of use while meeting business requirements. Common objectives of scaling a component or system include increasing the capacity for growth, improving the speed or processing efficiency of the component, or rebalancing the load on components.

Performance requirements are usually identified in terms of transaction response time, number of transactions per second, throughput, resource utilization, total cost per transaction, availability, and more. When the performance of SAS components lags, you can often change some settings to address the situation.

Be aware that many of the tuning recommendations in the guide involve upgraded or additional resources. As a result, some of these recommendations are likely to result in increased costs from your cloud provider.

The SAS Viya Platform Administration: Tuning guide offers tuning recommendations for:

* Provisioning Hardware for Performance
* Managing Cluster Resources
* Tuning the CAS Server
* Tuning Programming Resources and Programs
* Tuning the OpenSearch Component
* Tuning the LDAP Connection Pool
* Tuning the JDBC Connection Pool
* Tuning the PostgreSQL Server
* Tuning SAS Visual Analytics

Primary resource:

* [SAS Viya Platform Administration: Tuning](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caltuning/titlepage.htm) [Doc]

See also:

* [Tune the Programming Run-Time](./tune_programming_run-time.md) [Task]
* [Where to configure the SAS Programming Run-time with broader or narrower scope](https://communities.sas.com/t5/SAS-Communities-Library/Where-to-configure-the-SAS-Programming-Run-time-with-broader-or/ta-p/846124) [Blog]
* [Exploring Kubernetes Autoscalers for real-time SAS environments](https://communities.sas.com/t5/SAS-Communities-Library/Exploring-Kubernetes-Autoscalers-for-real-time-SAS-environments/ta-p/839538) [Blog]
* [Tuning the authentication timeout for long-running jobs
](https://communities.sas.com/t5/SAS-Communities-Library/Tuning-the-authentication-timeout-for-long-running-jobs/ta-p/834148) [Blog]
* [The SAS Workload Management Approach to Autoscaling](https://communities.sas.com/t5/SAS-Communities-Library/The-SAS-Workload-Management-Approach-to-Autoscaling/ta-p/825986) [Blog]
* [Performance Tuning for the SAS Viya Platform](https://communities.sas.com/t5/SAS-Communities-Library/Performance-Tuning-for-the-SAS-Viya-Platform/ta-p/864106) [Blog]

[Back to checklist](../checklist.md)