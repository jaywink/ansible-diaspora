#!/usr/bin/env python3
"""
Check of memory usage has capped and restart if so.

Run this as root.
"""
import os
import datetime
import psutil


MEM_MAX_MB = {{ diaspora_restart_on_memory }}


for proc in psutil.process_iter():
    try:
        if proc.username == "{{ os_user }}" and " ".join(proc.cmdline).find("sidekiq") > -1:
            current_mem = proc.get_memory_info().rss/1024/1024
            if current_mem > MEM_MAX_MB:
                # Restart!
                with open("/home/{{ os_user }}/restart_on_memory_capped.log", "a") as logfile:
                    logfile.write("{datetime} | Memory at {mem} MB, restarting...\n".format(
                        datetime=datetime.datetime.now().isoformat(), mem=current_mem
                    ))
                # Use `initctl` instead of `service`. The latter gives `unrecognized service` when done in root crontab..
                os.system("/sbin/initctl restart {{ servicename }}")
                with open("/home/{{ os_user }}/restart_on_memory_capped.log", "a") as logfile:
                    logfile.write("{datetime} | Restart done\n".format(
                        datetime=datetime.datetime.now().isoformat()
                    ))
    except psutil.NoSuchProcess:
        # Process went away while we're looping
        pass
