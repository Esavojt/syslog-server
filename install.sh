#!/bin/bash

install syslog-server.py /usr/local/bin/
install syslog-server.service /etc/systemd/system

systemctl start syslog-server
systemctl enable syslog-server