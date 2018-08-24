# -*- coding: utf-8 -*-

import subprocess
import os
import time
ips = ['127.0.0.1','192.168.0.11','10.3.1.19','192.168.0.13']

for ip in ips:

    result=subprocess.Popen(["ping", "-c", "1", "-W", "2", ip]).wait()

    if result:
        print ip, "inativo"
    else:
        print ip, "ativo"
