#!/bin/bash
cd /tmp
wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.8.0-Linux-x86_64.sh
chmod a+x Anaconda-1.8.0-Linux-x86_64.sh
./Anaconda-1.8.0-Linux-x86_64.sh -b -p /tmp/anaconda
export PATH=/tmp/anaconda/bin/:$PATH
rm Anaconda-1.8.0-Linux-x86_64.sh
