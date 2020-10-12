#!/usr/bin/env bash

cd /home/vagrant

sudo -s
yum -y install dnf
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
sudo EXTERNAL_URL="http://localhost" dnf install -y gitlab-ee