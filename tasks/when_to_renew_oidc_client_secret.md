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

Open ID Connect (OIDC) is a federated authentication protocol which allows applications such as SAS Viya to support single sign-on for users who have already authenticated against the third-party e.g. Microsoft Entra ID.

To configure SAS Viya to use OIDC, follow the instructions in the SAS Viya Administration guide > Security > Authentication > Authentication > How To > [Configure OAuth and OIDC](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/n1iyx40th7exrqn1ej8t12gfhm88.htm#p07d0r0biim3xjn1eq0sewh5ehg0).

During the process described in the instructions, you (or an IT administrator) register SAS Viya as a client of the OIDC Identity Provider which creates a clientID and clientSecret. The clientID and clientSecret are used by SAS Logon Manager to authenticate to the OIDC Identity Provider during the authentication processing.

The clientSecret might have a lifetime defined by the OIDC Identity Provider.  For example, Microsoft Entra ID has a maximum lifetime of 2 years, but your organization or IT administrators may choose to limit OIDC clientSecrets to a shorter lifetime - perhaps only 3 or 6 months. Irrespective of the OIDC Identity Provider you should look to cycle the clientSecret on a regular basis.

In SAS Viya, the OIDC clientID and clientSecret can be seen in Environment Manager's Configuration page,  for the SAS Logon Manager service, in the configuration instance '**sas.logon.oauth.providers: ####**', in the properties **relyingPartyId** and **relyingPartySecret**.

The relyingPartySecret must contain the current value of the clientSecret generated in the OIDC Identity Provider.

If the clientSecret expires without being renewed, SAS Viya would no longer be able to authenticate end user sign-ins via OIDC.

To ensure that this does not happen, find out when your OIDC clientSecret for SAS Viya expires, and make sure you act before it expires to have a new clientSecret generated (with a new expiry date), and update the relyingPartySecret in SAS Viya's Environment Manager Configuration page with the new clientSecret. Note the date the new secret expires.

See also: [Renew your OIDC client secret before it expires](./renew_oidc_client_secret.md)

[Back to checklist](../checklist.md)