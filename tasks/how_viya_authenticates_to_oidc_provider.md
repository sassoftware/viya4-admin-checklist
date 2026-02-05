![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Know how SAS Viya Authenticates to your OIDC Identity Provider

<!--
SortString: 0095
Description: Know how SAS Viya Authenticates to your OIDC Identity Provider
Tags: Initial,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern,Stuart Rogers
-->
When: After platform changes

Open ID Connect (OIDC) is a federated authentication protocol, which allows applications such as SAS Viya to support single sign-on for users who have already authenticated against the third-party e.g. Microsoft Entra ID.

If you are using OpenID Connect with SAS Viya, SAS Logon Manager must authenticate to the provider as part of the authentication processing.  SAS Viya supports authentication of SAS Logon Manager with either a clientSecret or private key JSON web tokens (JWTs).

With either mechanism the items used should be regularly refreshed and, in many cases, will expire.  As such, you must be aware of the mechanism that has been used in the OIDC configuration.  You can check the SAS Viya configuration under sas.logon.oauth.providers looking at the [jwtclientAuthentication](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calconfigref/n0ojd7b4h9o3rln1e6gqmpn39k9n.htm) [Doc] or [relyingPartySecret](https://go.documentation.sas.com/doc/en/sasadmincdc/v_072/calconfigref/p08z3xygmetaocn1t9jbk2gg0ilh.htm) [Doc] attributes.

See Also: [SAS Viya 2025.11 Custom Application Authenticate with Client Assertion](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-2025-11-Custom-Application-Authenticate-with-Client/ta-p/981722) [Blog]

[Back to checklist](../checklist.md)