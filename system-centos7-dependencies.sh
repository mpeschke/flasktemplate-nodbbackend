#!/bin/bash

# You need EPEL repo to install some of the dependencies
# For RHEL 7: sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install -y epel-release

# mysqlclient and possibly other pip packages need gcc.
yum groupinstall -y "Development tools"

# Installing python 2.X and 3.X from RHEL repo yum.
yum install -y wget python-pip python python-devel python34 python34-devel MySQL-python mysql-devel docker