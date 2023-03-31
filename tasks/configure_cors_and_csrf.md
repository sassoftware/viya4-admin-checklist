![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Configure CORS and CSRF settings

<!--
SortString: 0130
Description: Configure the SAS Viya platform's Cross-Origin Resource Sharing (CORS) and Cross-Site Request Forgery (CSRF) settings for deployments behind a DNS alias or proxy, and for SAS Visual Analytics
Tags: Initial,New,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern
-->
When: After platform changes

There are two reasons to configure the SAS Viya platform's settings for CORS and
CSRF:

1. You want to configure a proxy or DNS alias e.g. to allow a consistent alias
   to be used, and have traffic directed to whichever deployment should
   currently provide SAS Viya under that alias without users noticing much difference.
1. You wish to embed content from other web servers in a SAS Visual Analytics
   report, or the other way around.

## Configure CORS and CSRF for general SAS Viya services

Follow instructions in the SAS Viya Platform Administration guide > Configuration Properties > Concepts > [sas.commons.web.security.cors](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfig/n05000sasconfiguration0admin.htm#n0pcapysmu0r5qn1u8vokynl82ez) and immediately below that, [sas.commons.web.security.csrf](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfig/n05000sasconfiguration0admin.htm#n0uaa7r6b3x7iin1vmxcgl5b51h0).

## Configure CORS specifically for CAS

For our deployments which have an alias, we use a patchTransformer to set an
environment variable for CAS called `TKHTTP_CORS_ALLOWED_ORIGINS`, and assign it
a comma-separated list of CORS allowed origins. In our scripting, we first
define environment variables something like this:

```sh
NS=namespace_name
FQDN=k8s_ingress_hostname_fqdn
DOMAIN=the.organization.com
```

...and then use those environment variables in place of `${NS}`, `${FQDN}` and
`${DOMAIN}` to generate a patchtransformer YAML file something like this, so
that each of the aliases we might use to direct traffic to a given SAS Viya
deployment are among the list of comma-separated values for `TKHTTP_CORS_ALLOWED_ORIGINS`:

```yaml
apiVersion: builtin
kind: PatchTransformer
metadata:
  name: cas-add-environment-variables
patch: |-
  - op: add
    path: /spec/controllerTemplate/spec/containers/0/env/-
    value:
      name: TKHTTP_CORS_ALLOWED_ORIGINS
      value: "https://localhost:3000,https://${NS}.${FQDN},https://alias1.${DOMAIN},https://alias2.${DOMAIN},https://alias3.${DOMAIN}"
target:
  group: viya.sas.com
  kind: CASDeployment
  name: .*
  version: v1alpha1

```

We include the example above because it is often convenient to specify several
possible aliases for a single environment. However, it doesn't need to be so
complicated; a single hard-coded value for the TKHTTP_CORS_ALLOWED_ORIGINS base
url is also just fine if you only plan to use one alias.

## Configure CORS and CSRF for SAS Visual Analytics report integration

The blog post [All about CORS and CSRF for developing web applications with the
SAS Visual Analytics SDK](https://communities.sas.com/t5/SAS-Communities-Library/All-about-CORS-and-CSRF-for-developing-web-applications-with-the/ta-p/791124),
discusses how to correctly configure the same `sas.commons.web.security.cors`
and `sas.commons.web.security.csrf` configuration settings so that web
applications developed with the [SAS Visual Analytics SDK](https://developer.sas.com/guides/visual-analytics-sdk.html)
running on other servers, or using content from other servers, work and are not
blocked by the users' browser.

## Resources:

* [SAS Cloud Analytic Services: Reference](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calserverscas/n08000viyaservers000000admin.htm) [Doc], specifically the description of `env.TKHTTP_CORS_ALLOWED_ORIGINS` under [CAS Environment Variables Reference](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calserverscas/n08000viyaservers000000admin.htm#n08052viyaservers000000admin) [Doc]
* [sas.commons.web.security.cors](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfig/n05000sasconfiguration0admin.htm#n0pcapysmu0r5qn1u8vokynl82ez) [Doc]
* [sas.commons.web.security.csrf](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfig/n05000sasconfiguration0admin.htm#n0uaa7r6b3x7iin1vmxcgl5b51h0) [Doc]
* [All about CORS and CSRF for developing web applications with the SAS Visual Analytics SDK](https://communities.sas.com/t5/SAS-Communities-Library/All-about-CORS-and-CSRF-for-developing-web-applications-with-the/ta-p/791124) [Blog]

[Back to checklist](../checklist.md)