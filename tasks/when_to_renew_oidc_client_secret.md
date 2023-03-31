![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Know when to renew your OIDC client secret

<!--
SortString: 0100
Description: Open ID Connect uses expiring client secrets with a maximum lifetime of 2 years. If your SAS Viya deployment is configured to use OIDC, ensure that you know when this client secret expires so that you can renew it before it does.
Tags: Initial,New,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Stuart Rogers,David Stern
-->

## Know when to renew your OIDC client secret

Open ID Connect (OIDC) is a federated authentication protocol, somewhat like SAML, which allows applications such as SAS Viya to support single sign-on for users who have already authenticated against e.g. Azure Active Directory.

To configure SAS Viya to use OIDC, follow the instructions in the SAS Viya Administration guide > Security > Authentication > Authentication > Concepts > [Configure Azure AD for OIDC](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/p1i1pi9jk2nkkqn1rkh3t5elvc9y.htm#n1hp4d6pixslt8n1cm03kw8le8wm).

During the process described in the instructions, you (or an IT administrator) register SAS Viya as a client of OIDC which creates a clientID, and you then generate a ClientSecret which the client (SAS Viya's SAS Logon Manager service) will use to authenticate when making authentication requests.

That ClientSecret has a maximum lifetime of 2 years, but your organzation or IT administrators may choose to limit OIDC ClientSecrets to a shorter lifetime - perhaps only 3 or 6 months.

The expiry date for an OIDC ClientSecret can be seen in the Azure Portal in the Azure Active Directory page for your Reporting Environment, under Certificates & Secrets. On the Client Secrets tab, see the 'Expires' column.

In SAS Viya, the OIDC ClientID and ClientSecret can be seen in Environment Manager's Configuration page,  for the SAS Logon Manager service, in the configuration instance '**sas.logon.oauth.providers: azure**', in the properties **relyingPartyId** and **relyingPartySecret**.

The relyingPartySecret must contain the current value of the ClientSecret generated in Azure Active Directory.

If the ClientSecret expires without being renewed, SAS Viya would no longer be able to authenticate end user sign-ins via OIDC.

To ensure that this does not happen, find out when your OIDC ClientSecret for SAS VIya expores, and make sure you act before it expires to have a new ClientSecret generated (with a new expiry date), and update the relyingPartySecret in SAS Viya's Environment Manager Configuration page with the new ClientSecret. Note the date the new secret expires.

See also: [Renew your OIDC client secret before it expires](./renew_oidc_client_secret.md)

[Back to checklist](../checklist.md)