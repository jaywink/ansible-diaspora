# Ansible role for diaspora*

This Ansible role aims to automate the setup and maintenance of a diaspora* pod as much as possible. All configuration that is normally supported by diaspora* configuration files can be given through variables in this role.

The role is meant to not just create, but update and maintain the pod, so re-running the role will pull in latest code, run migrations, etc. Note however that server upgrades are not in the scope of this role.

This role by default deploys a pod in production mode. For development, please follow the normal install instructions, as developers need to be familiar with that stuff anyway.

What is diaspora*? [Find out here](http://diasporafoundation.org).

![](http://i.imgur.com/eWlYMFPl.jpg)

## Requirements

### Ansible

Tested on 1.9.x.

### Hardware

This role includes a slightly more light weight configuration than the default instructions. However, a minimum of 1GB of RAM is still recommended to run diaspora* for a small amount of users.

### OS

Currently only Ubuntu targets have verified. Ubuntu versions below have been verified to work:

* 14.04 (Trusty)
* 15.04 (Vivid)

15.10 is not supported, see [this issue](https://github.com/jaywink/ansible-diaspora/issues/1).

Pull requests welcome to include other platforms!

### Database

PostgreSQL only for now. Pull requests welcome for MySQL/MariaDB!

### Web server

Apache2 only for now. Pull requests welcome for other options!

## Diaspora* versions supported

Currently this role supports the current stable (0.5.x) releases and the development branch.

When diaspora* pushes out a new release or major changes to the develop branch, it is possible this role will start to fail. Please [follow the author](https://iliketoast.net/u/jaywink) on diaspora* for news and updates regarding this role.

## Configuration

Default configuration can be found in `defaults/main.yaml`. Please make a copy of it for your pod and tune the settings to your needs. You can also just override the ones you want.

The configuration is split into 4 main parts:

* Role configuration. This part contains things like repository information and the user on the target machine to install diaspora* on.
* Diaspora* configuration. Anything inside `diaspora_yml` is part of the diaspora* normal configuration and will get dumped as is into `config/diaspora.yml`. This means you can set *any* available configuration values into this YAML object, and they will be available for diaspora*. Only a part of the possible items are included in the defaults. Check [diaspora* configuration example](https://github.com/diaspora/diaspora/blob/develop/config/diaspora.yml.example) for the full list.
* Database configuration. These will be injected into `config/database.yml`.
* SSL certificates. These will be copied to relevant locations.

### SSL

Default configuration will make the pod run on HTTP, which of course is bad. To make it run on HTTPS, get some certificates, place them in your vars file, and then switch `diaspora_yml.configuration.environment.require_ssl` to `true`. Rerun role, that is it. No excuses to run on HTTP.

### Domain name

Before creating your pod, obviously you need to think of a domain name. This cannot be changed in diaspora*, though the role doesn't enforce this. Changing it will break everything in your pod though!

Make sure to place the domain name in these variables:

* `domainname`
* `diaspora_yml.configuration.environment.url`

## Running your pod

Once deployed, the pod will be available and running. That's it! A few things to note though.

* After creating your first account, please see the diaspora* wiki on [how to make yourself an admin](https://wiki.diasporafoundation.org/FAQ_for_pod_maintainers#What_are_roles_and_how_do_I_use_them.3F_.2F_Make_yourself_an_admin_or_assign_moderators). The setting `diaspora_yml.configuration.admins.account` should be set to your username to ensure you see the admin panel. Rerun role now.
* Consider setting `diaspora_yml.configuration.settings.enable_registrations` to `false` if you don't want to have other people signing up.
* If you need to for some reason do some manual stop/start actions to the pod, it is governed by Upstart or SystemD, depending on your OS version. Log into your server and do the normal `sudo service diaspora stop/start/restart` etc as per other Ubuntu services. Replace service name with whatever you set in `servicename` variable, if you changed that.

## Caveats

While automating maintenance, this role doesn't do your backups. [Do your backups!](https://wiki.diasporafoundation.org/FAQ_for_pod_maintainers#How_do_I_back_up_my_pod.3F)

## Contact

* diaspora*: https://iliketoast.net/u/jaywink / jaywink@iliketoast.net
* xmpp: jaywink@dukgo.com
* email: mail@jasonrobinson.me

## License

[MIT](https://tldrlegal.com/license/mit-license).

The role author takes no responsibility for what this role does when you run it. If your server melts down, or the stock markets collapse, or the world burns in fire - I am not responsible. Normally, you should just get a nice little diaspora* pod though.
