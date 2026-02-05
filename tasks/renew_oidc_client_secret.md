![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Renew your OIDC client secret before it expires

<!--
SortString: 0480
Description: If your SAS Viya deployment is configured to use OIDC, renew your OIDC client secret before it expires.
Tags: Regular,New,Done
Authors: Stuart Rogers,David Stern
Topic: Kubernetes & IT Admin
Essential: -
Frequency: When secret changes
-->

In SAS Viya, the OIDC ClientID and ClientSecret can be seen in Environment Manager's Configuration page, for the SAS Logon Manager service, in the configuration instance '**sas.logon.oauth.providers: ####**', in the properties **relyingPartyId** and **relyingPartySecret**. This does not show the secret's expiry date. If you are using Microsoft Entra ID as your OpenID Connect provider, this does have an expiry date.  You can see Microsoft Entra ID’s expiry date in the Azure Portal under the Certificates & Secrets settings for the application registration.

Before your OIDC client secret expires, work with your IT administrator to have them generate a new client secret, and replace the **relyingPartySecret** with that client secret.

General instructions for setting up OIDC can be found in the SAS Viya Administration guide > Security > Authentication > Authentication > How To > [Configure OAauth and OIDC](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/n1iyx40th7exrqn1ej8t12gfhm88.htm#p07d0r0biim3xjn1eq0sewh5ehg0) [Doc].

Note the date the new secret expires, so that you can renew it again before it expires.

See also: [Know when to renew your OIDC client secret](./when_to_renew_oidc_client_secret.md) [Task]

[Back to checklist](../checklist.md)