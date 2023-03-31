![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure External Access to CAS

<!--
SortString: 0350
Description: Configure access to CAS from outside your SAS Viya deployment
Tags: Initial,New,Done
Topic: CAS
Essential: -
Authors: David Stern
-->
When: Before user access, as needed

As explained in [SAS Viya – Access CAS from Outside the Viya Deployment](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Access-CAS-from-Outside-the-Viya-Deployment/ta-p/847439) [Blog], an HTTP ingress is configured to provide access to each CAS server from outside the Viya deployment using the CAS REST-API. But that's all it allows.

In order to enable SAS 9.4, SAS Viya 3.5, other SAS Viya deployments or open-source programming clients like Python SWAT to get binary access to the CAS server(s) in your SAS Viya deployment, you need to enable the binary service by adding a reference to a patchTransformers to your kustomization.yaml file, and the corresponding transformer to your site-config directory structure.

In order to enable Postman, Jupyter or other HTTP clients to get HTTP access to the CAS server(s) in your SAS Viya deployment, you need to enable the HTTP service in a similar way.

The resources below explain how to do both.

Resources:

* [SAS Viya – Access CAS from Outside the Viya Deployment](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-Access-CAS-from-Outside-the-Viya-Deployment/ta-p/847439) [Blog]
* [Configure External Access to CAS](https://go.documentation.sas.com/doc/en/sasadmincdc/default/dplyml0phy0dkr/n08u2yg8tdkb4jn18u8zsi6yfv3d.htm#n0exq3y1b5gs73n18vi9o78y2dg3) [Doc]

[Back to checklist](../checklist.md)