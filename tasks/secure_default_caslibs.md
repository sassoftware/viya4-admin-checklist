![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Secure Default Caslibs, especially the Public Caslib

<!--
SortString: 0320
Description: Review and change default access controls on default CAS libraries
Tags: Initial,New,Done
Topic: CAS
Essential: -
Authors: David Stern
-->
When: Before user access, as needed

When SAS Viya is first installed, it is configured with at least one CAS server (named `cas-shared-default`). You may define additional CAS servers.

Each CAS server is initialized with several CAS libraries (caslibs) 'out of the
box'. The exact set of these libraries depends on which SAS Viya products or
solutions are installed and configured to use that CAS server. Some examples are
listed below:

> **Notes**:
> * This is not an exhaustive list.
> * Not all of these caslibs will necessarily be created on all CAS servers.
> * Default CAS Access controls are described in summary here.
> * The default CAS Access controls may be changed in future. This table was correct when last reviewed. You should inspect the actual access controls on your SAS Viya Platform's CAS servers.

| CASLib name | Description | Default permissions, and comments on those permissions |
| ----------- | ----------- | ----- |
| AppData | Stores application specific data, required by the application. | Read-only for users (including SAS Administrators) by default.</br>Full control for the `sasapp` internal account. |
| CASUSER(*username*) | Personal File System Caslib | Unlike other libraries in this list, CASUSER(*username*) is a private caslib, and each user may have their own.</br>All data associated with a user's caslib is stored in a specific CASUSER path location on the CAS controller.</br>Can be disabled by ensuring there is no writeable path for the CASUSER path location.</br>Normal access controls do not apply within CAS, each is only accessible to the users themselves. However, if the CASUSER path is accessible by other users, or by the users themselves from outside CAS, this library represents a potential route for users to export sensitive data.</br>Therefore **requires careful consideration** in regulated or secure environments. |
| Formats | Stores user defined formats. | Read-Write for users.</br>Full control for administrators and the SAS System Account. |
| **ModelPerformanceData** | **Stores performance data output for the Model Management service.** | **This library is of potential concern for SAS Administrators in production environments.**</br>Full control for all authenticated users. |
| Models | Stores models created by Visual Analytics for use in other analytics or SAS Studio. | Read-only for users (including SAS Administrators) by default.</br>Full control for the `sasapp` internal account.|
| **ModelStore** | **Stores analytic stores for models that are registered in the common model repository.** | **This library is of potential concern for SAS Administrators in production environments.**</br>Full control for all authenticated users. |
| ProductData | Stores product data supplied by SAS. | Read-only for SAS Administrators.</br>Full control for the `sasapp` internal account. |
| **Public** | **Shared and writeable caslib, accessible to all users.** | **This library is of potential concern for SAS Administrators in production environments.**</br>Full control for all authenticated users.</br>Consider restricting user access to this library to avoid enabling users to share sensitive data without proper access controls. |
| ReferenceData | Stores application specific data per CAS server, required by the application. | Read-only, but including DropTable for Authenticated Users.</br>Read-Write custom permissions for SAS Administrators. |
| Samples | Stores sample data, supplied by SAS. | Read-only for Authenticated Users.</br>Limited Read-Write for SAS Administrators, who can create and drop tables, but cannot insert or update data in them.</br>Full control for the `sasapp` internal account. |
| SystemData | Stores application generated data, used for general reporting. | Limited Read-Write for SAS Administrators, who can create and drop tables, but cannot insert or update data in them.</br>Full control for the `sasapp` internal account. |
| VAModels | Library for ASTORE objects used within a SAS Visual Analytics report. | Limited Read-Write for Authenticated Users, who can create and drop tables, but cannot insert or update data in them.</br>Full control for the `sasapp` internal account.|

As a SAS Administrator, you are likely responsible for defining or interpreting
a [Security Policy](./security_policy.md), and for defining and implementing a
SAS Viya [Authorization Model](./authorization_model.md). That authorization
model must consider what access you intend users in general, and in each of your
organization's user groups, to these 'out of the box' CAS libraries, and in
particular to 'wide open' caslibs, such as the **ModelPerformanceData**,
**ModelStore** and **Public** CAS libraries.

Remember to consider the storage space you provide for user-writeable CASlibs,
and to educate your users about managing the amount of data they store in
user-writeable shared or public CASlibs so that they do not become full, which
may prevent production data from being written to them.

Resources:

* [SAS Viya Platform Administration: Data > CAS Fundamentals > Caslibs](https://go.documentation.sas.com/doc/en/sasadmincdc/default/casfun/n1i11h5hggxv65n1m5i4nw9s5cli.htm) [Doc]
* [SAS Viya Platform Administration: Security > Fundamentals > Authorization Fundamentals > CAS Authorization](https://go.documentation.sas.com/doc/en/sasadmincdc/default/caliam/p1aj6r7s98uvkgn1trql7qz29a3b.htm) [Doc]
* [SAS Viya Platform Administration: Security > Authorization > CAS Authorization](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthzcas/titlepage.htm) [Doc]

See Also:

* [Accessing path-based data from CAS in Viya](https://communities.sas.com/t5/SAS-Communities-Library/Accessing-path-based-data-from-CAS-in-Viya/ta-p/714291) [Blog]
* [Storage for CAS Libraries](caslib_storage.md) [Task]
* [Personal, Predefined, and Manually Added Caslibs](https://go.documentation.sas.com/doc/en/sasadmincdc/default/casfun/n1i11h5hggxv65n1m5i4nw9s5cli.htm#n160mqjgfcayphn1st2iguedbuyt) [Doc]
* [The CASHostAccountRequired Custom Group](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calids/p0ata1oqy9v7nan188h1k254doxq.htm?fromDefault=#p1b0uixk221q3jn19ztuitir62gm)


[Back to checklist](../checklist.md)