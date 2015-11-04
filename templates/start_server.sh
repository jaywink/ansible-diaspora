#!/usr/bin/env bash
# Run as root - launched from upstart init or systemd service

sleep 10

sudo -u {{ os_user }} -H bash -c "source /home/{{ os_user }}/.bash_profile && cd /home/{{ os_user }}/diaspora && rvm use `cat /home/{{ os_user }}/diaspora/.ruby-version`@diaspora && DB=postgres RAILS_ENV=production ./script/server"


