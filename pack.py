# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

#需要配置分割线 ===================================================================
# 项目配置
project_name = "" #工程名
scheme = "" #scheme
project_type = "-workspace" #工程类型 pod工程 -workspace 普通工程 -project
configuration = "Release" #编译模式 Debug,Release
project_path = "" # 项目根目录
pack_robot_parth = "/Users/Love/Desktop/PackRobot/" # 打包后ipa存储目录 请指向自动打包脚本所在目录
mobileprovision_uuid = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" #mobileprovision uuid
signing_certificate = "iPhone Distribution: xxxx xxxx xxxx" #证书名称

# fir
fir_api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx" # firm的api token
download_address = "https://fir.im/xxxxxxxxx" #firm 下载地址

#邮件配置
app_name = "" #App名
from_name = ""
from_addr = ""
password = ""
smtp_server = "smtp.exmail.qq.com"
to_addr = ['xx@qq.com','xx@126.com']

#需要配置分割线 ===================================================================

# 清理项目
def clean_project():
    print("** PACKROBOT START **")
    os.system('cd %s;xcodebuild clean' % project_path) # clean 项目

# archive项目
def build_project():
    os.system('cd %s;mkdir build' % project_path)
    if project_type == "-workspace" :
        project_suffix_name = "xcworkspace"
    else :
        project_suffix_name = "xcodeproj"
    os.system ('cd %s;xcodebuild archive %s %s.%s -scheme %s -configuration %s -archivePath %s/build/%s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s" || exit' % (project_path,project_type,project_name,project_suffix_name,scheme,configuration,project_path,project_name,signing_certificate,mobileprovision_uuid))

# 导出ipa包到自动打包程序所在目录
def exportArchive_ipa():
    global ipa_filename
    ipa_filename = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    ipa_filename = project_name + "_" + ipa_filename;
    os.system ('%s/xcodebuild-safe.sh -exportArchive -archivePath %s/build/%s.xcarchive -exportPath %s/%s -exportOptionsPlist %s/exportOptionsPlist.plist ' %(pack_robot_parth,project_path,project_name,pack_robot_parth,ipa_filename,pack_robot_parth))

# 删除build目录
def rm_project_build():
    os.system('rm -r %s/build' % project_path)

# 上传fim
def upload_fir():
    if os.path.exists("%s/%s" % (pack_robot_parth,ipa_filename)):
        # 直接使用fir 有问题 这里使用了绝对地址 在终端通过 which fir 获得
        ret = os.system("fir publish '%s/%s/%s.ipa' --token='%s'" % (pack_robot_parth,ipa_filename,project_name,fir_api_token))
    else:
        print("没有找到ipa文件")

# 地址格式化
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 发邮件
def send_mail():
    msg = MIMEText(app_name + "iOS测试项目已经打包完毕，请前往 " + download_address + " 下载测试！如有问题，请联系iOS相关人员或者直接将问题提至Teambition，我们会及时解决，谢谢", 'plain', 'utf-8')
    msg['From'] = _format_addr('%s''<%s>' % (from_name,from_addr))
    msg['To'] = ",".join(_format_addr('%s' % to_addr))
    msg['Subject'] = Header(app_name + "iOS客户端自动打包程序 打包于:" + time.strftime('%Y年%m月%d日%H:%M:%S',time.localtime(time.time())), 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr,to_addr, msg.as_string())
    server.quit()

# 输出包信息
def ipa_info():
    os.system('fir info %s/%s/%s.ipa' % (pack_robot_parth,ipa_filename,project_name))
    print("** PACKROBOT SUCCEEDED **")

def main():
    # 清理并创建build目录
    clean_project()
    # 编译目录
    build_project()
    # 导出ipa到机器人所在目录
    exportArchive_ipa()
    # 删除build目录
    rm_project_build()
    # 上传fir
    upload_fir()
    # 发邮件
    send_mail()
    #输出包信息
    ipa_info()

# 执行
main()
