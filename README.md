# HXPackRobot 如果对你有一点点帮助,请给一颗★,你的支持是对我的最大鼓励！

作为一名开发人员，我们不仅需要面对无穷无尽的bug，还得无穷无尽的打测试包，有的时候甚至一天打N个包，面对如此频繁的苦力工作，我们自然会想是否可以让机器人来帮我们实现这一重复的过程，其实这个完全可以实现，而且网上的实现方法各式各样，但无非都是运用系统打包指令打包，然后通过Fir.im的fir-cli上传指令上传，如果你是打包到其他平台，其过程也大同小异。网上实现比较多的是Python和shell实现。下面就把Python实现的一键打包程序分享给大家，只需简单配置，便可以轻松打包，打包的时候，来上一杯茶，和别人聊聊天，何不惬意！

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

# 注意事项

打包之前请保证文件夹中没有ipa文件

# 扩展

Python下载：https://www.python.org/downloads/

fir-cli 安装使用:https://github.com/FIRHQ/fir-cli/blob/master/README.md 

# 参考文章:

http://blog.csdn.net/qq_19979539/article/details/50998275

http://zackzheng.info/2015/12/27/2015-12-27-an-automated-script-for-building-archiving-submission-sending-emails/

http://blog.csdn.net/potato512/article/details/52172107

http://doc.okbase.net/boch2436/archive/120790.html

https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/xcodebuild.1.html

http://www.jianshu.com/p/ea5fa39b8950

http://stonedu.site/2016/08/17/iOS-%E6%9C%AC%E5%9C%B0%E6%89%93%E5%8C%85%E5%B7%A5%E5%85%B7/

http://www.jianshu.com/p/15edfe11f8ac

http://www.cnblogs.com/slc-lover/p/5921129.html

http://m.blog.csdn.net/article/details?id=52694817
