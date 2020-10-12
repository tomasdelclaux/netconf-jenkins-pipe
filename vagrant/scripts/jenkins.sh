#!/usr/bin/env bash

cd /home/vagrant

sudo yum -y install wget

sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade
sudo yum -y install jenkins java-1.8.0-openjdk-devel
sudo systemctl daemon-reload

sudo sed -i 's/JENKINS_PORT="8080"/JENKINS_PORT="8090"/g' /etc/sysconfig/jenkins
sudo systemctl start jenkins