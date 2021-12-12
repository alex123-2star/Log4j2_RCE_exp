# Log4j2_RCE_exp
this is a private project
0x01 漏洞描述
Apache Log4j 是 Apache 的一个开源项目，Apache Log4j2是一个基于Java的日志记录工具。该工具重写了Log4j框架，并且引入了大量丰富的特性。我们可以控制日志信息输送的目的地为控制台、文件、GUI组件等，通过定义每一条日志信息的级别，能够更加细致地控制日志的生成过程。该日志框架被大量用于业务系统开发，用来记录日志信息。

这里需要在服务器上执行一个python 脚本，可以自动安装你输入的命令生成对应的EXP，exp地址会贴在最下面。


![image](https://github.com/alex123-2star/Log4j2_RCE_exp/blob/1c2347d15a451a7cb9e4742921bae481a65778d5/imags/%E5%9B%BE%E7%89%87%204.png)


Exp生成并且编译成功

开启服务
使用python执行

python3 log4j_exp.py

![image](https://github.com/alex123-2star/Log4j2_RCE_exp/blob/1c2347d15a451a7cb9e4742921bae481a65778d5/imags/%E5%9B%BE%E7%89%87%209.png)

marshalsec-0.0.3-SNAPSHOT-all.jar 
这个包有点大，我相信你们手上应该有现成的，你们也可以自己编译

如果你嫌麻烦 那去releases中获取吧
