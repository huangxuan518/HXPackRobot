# HXPackRobot
一键打包机器人

# 如何使用

1.下载压缩包，解压缩到桌面(注意:必须放到桌面)
![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/1.png)

2.将文件名改为PackRobot,否则无法使用

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/2.png)

3.将我们需要签名的mobileprovision文件替换文件夹中的,可以命名一样替换，或者随便命名，如果是随便命名则需要在resign.sh中做更改，Entitlements.plist文件也要做更改

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/3.png)

4.ipa.py里面的配置更改成自己的

5.运行PackRobot.app则可以一键打包改签名并上传fir,给相关人员发送邮件


