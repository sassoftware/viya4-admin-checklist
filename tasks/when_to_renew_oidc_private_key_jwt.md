![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Know when to renew OIDC Private Key JWT

<!--
SortString: 0105
Description: If your SAS Viya deployment is configured to use OIDC, ensure that you know when renew the private key JSON web tokens.
Tags: Initial,New,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Stuart Rogers,David Stern
-->

Open ID Connect (OIDC) is a federated authentication protocol, which allows applications such as SAS Viya to support single sign-on for users who have already authenticated against the third-party e.g. Microsoft Entra ID.  SAS Logon Manager can use a private key JSON web token (JWT) to authenticate to the OpenID Connect provider.

Using the private key JSON web tokens (JWTs) requires the OpenID Connect provider to be given the public key to validate the signatures on the JWTs.  OKTA can use the automatically generated public key, which is generated on first launch of SAS Logon Manager.  Since this is a public key there is no expiry date associated with the key.  Which means that you do not have to refresh the signing keys on a specific timescale.

Alternatively, if you use Microsoft Entra ID as your OIDC provider you need to provide a X.509 certificate containing the public key.  Microsoft Entra ID uses the certificate to validate the signature on the JWTs.  Since this is a certificate contains the public key, this does have a specific expiry date after which it is no longer valid.

Therefore, you will need to know when this certificate expires.  You can see if your environment is using a signing certificate by looking at the sas.logon.jwt settings for the signingCert attribute.  This will contain the signing certificate, which you can inspect to validate the expiry date.

To configure SAS Viya to use **JWT Client Authentication with Microsoft Entra ID**, follow the instructions in the SAS Viya Administration guide > Security > Authentication > Authentication > How To > [Configure JWT Client Authentication](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/n1iyx40th7exrqn1ej8t12gfhm88.htm#p1u2r0v4g85n73n1aw161bg1apli) [Doc].  Alternatively, for **OKTA** follow the instructions in the SAS Viya Administration guide > Security > Authentication > Authentication > How To > [Configure JWT Client Authentication](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthmdl/n1iyx40th7exrqn1ej8t12gfhm88.htm#n01cavm03hvqrbn1uzn1lnkkdlmk) [Doc].

<!-- ToDo, task when_to_renew_oidc_jwt_signing_keys.md in backlog : See also: Know when to renew your OIDC JWT Signing Keys -->

[Back to checklist](../checklist.md)