# HXPackRobot 如果对你有一点点帮助,请给一颗★,你的支持是对我的最大鼓励！

作为一名开发人员，我们不仅需要面对无穷无尽的bug，还得无穷无尽的打测试包，有的时候甚至一天打N个包，面对如此频繁的苦力工作，我们自然会想是否可以让机器人来帮我们实现这一重复的过程，其实这个完全可以实现，而且网上的实现方法各式各样，但无非都是运用系统打包指令打包，然后通过Fir.im的fir-cli上传指令上传，如果你是打包到其他平台，其过程也大同小异。网上实现比较多的是Python和shell实现。但是很多使用起来都有一些问题。下面就把自己经过多天实践的Python和shell实现的一键打包程序分享给大家，只需简单配置，便可以轻松打包，打包的时候，来上一杯茶，和别人聊聊天，何不惬意！

# 最新更新：
邮件中增加二维码，扫一扫即可下载 感谢

# 程序支持上传平台：
fir.im / pgyer.com(蒲公英)


# 程序运行条件：
Python 和 fir-cli(上传fir.im时需要)

# 注意事项

1. 运行之前请将证书自动 □ kuangAutomatically manage signing 配置勾勾去掉(选择工程，在配置文件的General-Signing里面)
2. 使用 Xcode 9.0 以上编译器 exportOptionsPlist.plist 中需要新增 provisioningProfiles 字段(具体配置会在后面说明)

# 如何使用

1.下载压缩包，解压缩到桌面(注意:必须放到桌面)

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/1.png)

2.将文件名改为PackRobot,否则无法使用

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/2.png)

3.打开文件夹

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/3.png)

4.打开pack.py文件，根据自己的实际情况更改红框部分
![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/6.png)

7.打开exportOptionsPlist.plist文件更改,teamId见下文如何获取用户ID

## exportOptionsPlist中键值填写说明:
* 必须填写的公共设置:
    * method
        * 可选参数:app-store, package, ad-hoc, enterprise, development, developer-id
    * teamID
    * provisioningProfiles( Xcode 9.0 需要, 类型: Dictionary )
        * 包含一对子键  bundle id : 证书名
    
* 用于非App Store导出的:
    * compileBitcode
    * embedOnDemandResourcesAssetPacksInBundle
    * iCloudContainerEnvironment
    * manifest
    * onDemandResourcesAssetPacksBaseURL
    * thinning

* 用于App Store导出:
    * uploadBitcode
    * uploadSymbols

## 通用配置:
* 用于App Store导出:
    * method＝app-store，uploadBitcode＝YES，uploadSymbols＝YES
    
* Other:
    * method＝ad-hoc，compileBitcode＝NO

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/5.png)

8.运行PackRobot.app会打开终端运行指令，archive成功会在工程目录下看到bulid目录

9.ipa包生成成功会根据工程名+时间生成一个ipa包文件夹，并删除build目录

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/4.png)

10.进入可以看到我们的ipa包

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/7.png)

11.上传fir

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/14.png)

12.上传成功

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/15.png)

11.发送邮件

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/16.png)

11.收到邮件

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/17.png)

11.下载安装包

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/18.png)

# 证书名称和用户ID如何获取

1.打开钥匙串

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/11.png)

2.双击证书

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/12.png)

3.红框标示的用户ID如果和我们苹果中心按照下图进入后看到的红框id一样则为当前需要的证书

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/8.png)

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/9.png)

# .mobileprovision的UUID如何获取

1.Xcode - Window - Organizer 进入 Archives目录，然后选择之前手动打好的包

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/19.png)

2.选择Export导出

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/20.png)

3.选择第三个Inhouse包

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/21.png)

4.一直下一步，到最后可以看到图示

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/22.png)

5.点击箭头进入，可以看到.mobileprovision，名字前面即为UUID

![image](https://github.com/huangxuan518/HXPackRobot/blob/master/%E8%AF%B4%E6%98%8E%E5%9B%BE/23.png)

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
