#!/bin/bash

# Ansible doesn't play nicely with RVM, which wants to be a function
# This wrapper script can be used to run shell commands from Ansible with the `script` module.
#
# Don't run this as root, run it as the user who has RVM installed.
#
# Params:
#    $1    - Target, for example rvm, rake, etc
#    *args - args

set -e


source $HOME/.bash_profile

export RAILS_ENV=production
export DB=postgres

export DIASPORA_RUBY_VERSION=`cat $HOME/diaspora/.ruby-version`

cd $HOME/diaspora

if [[ "$1 $2" -ne "rvm install" ]]; then
    rvm use $DIASPORA_RUBY_VERSION@diaspora
fi

$1 $2 $3 $4 $5 $6 $7 $8 $9
