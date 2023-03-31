![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Use customer-provided certificates

<!--
SortString: 0050
Description: Generate new or renew expiring TLS certificates used for encryption of data in transit.
Tags: Initial,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: Ajmal Farzam
-->

When: Initial

By default, the SAS Viya platform is deployed with full-stack TLS. A certificate generator creates a trusted issuing CA certificate which is used to sign server identity certificates to encrypt back-end communications.  A list of trusted certificate authorities is delivered with SAS Viya in a truststore.

Your organization might have its own, proprietary CA certificates that are used to protect resources within your organization's network infrastructure (for example, your ingress controller or LDAP server). The proprietary CA certificates are not in the public truststore that is distributed with SAS Viya, and must be [added to the deployment](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calencryptmotion/n1xdqv1sezyrahn17erzcunxwix9.htm#n00kfxh05vul45n1ki9k5x6jj4bc) [Doc]. Both SAS Viya generated and proprietary CA certificates have expiration dates (default of two years for SAS Viya generated CA certificates). Follow the [documented instructions](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calencryptmotion/n1xdqv1sezyrahn17erzcunxwix9.htm#n0hxizba350deqn1l7prdukhsrwf) [Doc] for changing or renewing certificates as they approach expiry.

CA certificates should also be [imported into the trust bundles on and Windows client machines](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calencryptmotion/n1xdqv1sezyrahn17erzcunxwix9.htm#p09ebu28fz7zpjn17r6jf6iwpyyw) [Doc] used to access your SAS Viya platform.

The CA certificate can be extracted from the `sas-viya-ca-certificate-secret` secret in the Viya namespace to inspect its attributes (including expiry date) using standard [openssl commands](https://www.suse.com/support/kb/doc/?id=000018417).

See also:
* [SAS Viya Platform Encryption: Data in Motion](https://go.documentation.sas.com/doc/en/sasadmincdc/default/calencryptmotion/titlepage.htm) [Doc]
* [SAS Viya 4 TLS Options](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-2020-1-and-later-TLS-Options/ta-p/705982) [Blog]
* [SAS Viya 4 TLS Troubleshooting Tips](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-2020-1-and-later-TLS-Troubleshooting-Tips/ta-p/706087) [Blog]
* [SAS Viya 2021.1.3 TLS Changes](https://communities.sas.com/t5/SAS-Communities-Library/SAS-Viya-2021-1-3-TLS-Changes/ta-p/754712) [Blog]

[Back to checklist](../checklist.md)