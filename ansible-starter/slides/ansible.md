---
(author: foosinn
title: Ansible
date: 23.07.2019
---

# Was ist Ansible? 🤔

* Automatisierung
* Konfigmanagement
* Ad-Hoc Commands
* Braucht keine Software auf den Nodes

# Ansible vs ⚔️

* Puppet (braucht Agent, komplexer, Ruby)
* Others:
  * Chef?
  * Salt?
  
# Create dirs

```
mkdir -p inventory/host_vars roles/engelsystem/{defaults,handlers,tasks,templates}
```

# Install

```sh
python -m venv env
. env/bin/activate
pip install ansible
```

# ansible.cfg

```
[defaults]
inventory = inventory
gathering = smart
fact_caching = jsonfile
fact_caching_connection = facts
fact_caching_timeout = 7200
stdout_callback = yaml
bin_ansible_callbacks = True

[ssh_connection]
ssh_args = -C -o ControlMaster=auto -o ControlPersist=300s
pipelining = True
```

# inventory

```
engelsystem_version: v3.0.0
engelsystem_servername: engel.example.com
engelsystem_mysql_root_password: password
engelsystem_mysql_user_password: password
engelsystem_api_key: password
engelsystem_app_name: Engelsystem
engelsystem_footer_items:
FAQ: https://faq.example.com
Contact: mailto:help@example.com
engelsystem_theme: 7
engelsystem_default_locale: de_DE.UTF-8
certbot_mail: admin@example.com
```

# Demo Time 🖥️

* [Engelsystem](https://github.com/engelsystem/engelsystem-ansible)

# Cool Stuff 🕶️

* ansible-doc
* ansible-console
* run tests with molecule
* Write own filters with Python

# Questions? 🙋
