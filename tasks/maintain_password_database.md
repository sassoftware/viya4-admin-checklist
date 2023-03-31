![Global Enablement & Learning](/img/gel_banner_logo_tech-partners.jpg)

# Maintain a Secure Password Database

<!--
SortString: 0040
Description: Maintain a secure and encrypted password-protected password database using an appropriate software tool or service
Tags: Initial,Legacy,Done
Topic: Kubernetes & IT Admin
Essential: -
Authors: David Stern,Michael Erickson
-->
When: Post-install, after platform changes, and when any shared or service account’s password changes

## Maintain a secure and encrypted password-protected password database using an appropriate software tool or service

KeePass is a popular, good, free, and open-source choice.

For larger enterprise-scaled deployments, consider popular paid-for password database tools such as One Identity, CyberArk Enterprise Password Vault, and Centrify. For smaller organizations, consider something like 1Password, LastPass, Dashlane, Keeper, Sticky Password, Bitwarden, NordPass, or ZohoVault.

Maintain the credentials in this database for service and administrative accounts, external-database-outbound logins, and so on.

Decide whether you should store the credential database in the cloud, or on premise. Keep the password database on a machine that is physically better protected than a desktop or laptop PC so that it cannot easily be stolen. (In other words, store the database on a host in the datacenter or corporate cloud.)

Use multi-factor authentication for access to the hosts in the data center on which the password database is stored, and for authentication to the password database itself.

[Back to checklist](../checklist.md)