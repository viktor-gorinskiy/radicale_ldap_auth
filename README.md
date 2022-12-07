# Radicale IMAP authentication plugin

LDAP authentication plugin for [Radicale](http://radicale.org/).

## Installation

    python3 -m pip install radicale_ldap_auth

## Configuration

    [auth]
    type = radicale_ldap_auth
    ldap_url = ldap://digi-dc01.corp.myservices.digital
    ldap_port = 389
    ldap_user_postfix = myservices.digital

## License

[GPL-3.0](LICENSE)
