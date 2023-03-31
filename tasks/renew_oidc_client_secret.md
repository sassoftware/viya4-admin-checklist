![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Renew your OIDC client secret

<!--
SortString: 0480
Description: If your SAS Viya deployment is configured to use OIDC, renew your OIDC client secret before it expires.
Tags: Regular,New,Done
Authors: Stuart Rogers,David Stern
Topic: Kubernetes & IT Admin
Essential: -
Frequency: When secret changes
-->

## Renew your OIDC client secret before it expires

The expiry date for an OIDC ClientSecret can be seen in the Azure Portal in the Azure Active Directory page for your Reporting Environment, under Certificates & Secrets. On the Client Secrets tab, see the 'Expires' column.

In SAS Viya, the OIDC ClientID and ClientSecret can be seen in Environment Manager's Configuration page, for the SAS Logon Manager service, in the configuration instance '**sas.logon.oauth.providers: azure**', in the properties **relyingPartyId** and **relyingPartySecret**. This does not show the secret's expiry date.

Before your OIDC client secret expires, work with your IT administrator to have them generate a new client secret, and replace the **relyingPartySecret** with that client secret.

General instructions for setting up Azure AD for OIDC can be found in the SAS Viya Administration guide > Security > Authentication > Authentication > Concepts > [Configure Azure AD for OIDC](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/p1i1pi9jk2nkkqn1rkh3t5elvc9y.htm#n1hp4d6pixslt8n1cm03kw8le8wm).

Note the date the new secret expires, so that you can renew it again before it expires.

See also: [Know when to renew your OIDC client secret](./when_to_renew_oidc_client_secret.md)

[Back to checklist](../checklist.md)