# HXPackRobot
一键打包机器人

# 程序运行条件：
Python 和 fir-cli

# 如何使用

1.下载压缩包，解压缩到桌面(注意:必须放到桌面)

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/1.png)

2.将文件名改为PackRobot,否则无法使用

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/2.png)

3.打开文件夹

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/3.png)

4.进入苹果开发者中心下载我们需要的签名证书，替换掉文件夹中的FuKuaiDi_Inhouse.mobileprovision证书

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/10.png)

5.打开ipa.py文件，根据自己的实际情况更改红框部分
![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/6.png)

6.打开resign.sh文件，更改红框部分

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/4.png)

7.打开Entitlements.plist文件，更改红框部分，红框部分即为用户证书ID+identifier

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/5.png)

8.运行PackRobot.app则可以一键打包改签名并上传fir,给相关人员发送邮件

# 证书名称和用户ID如何获取

1.打开钥匙串

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/11.png)

2.双击证书

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/12.png)

3.红框标示的用户ID如果和我们苹果中心按照下图进入后看到的红框id一样则为当前需要的证书

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/8.png)

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/9.png)

# 扩展

Python下载：https://www.python.org/downloads/

fir-cli 安装使用:https://github.com/FIRHQ/fir-cli/blob/master/README.md 
