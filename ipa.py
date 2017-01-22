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
app_name = “app" #App名
project_name = "project" #工程名
scheme = "scheme" #scheme
project_path = "~/Desktop/iOS-Project" # 项目根目录
targerIPA_parth = "~/Desktop/PackRobot/" # 打包后ipa存储目录 请指向PackRobot所在目录

# fir
fir_api_token = "1d93d24eee630b269e46a7c98df5655c" # firm的api token
download_address = "https://fir.im/project" #firm 下载地址

#邮件配置
from_name = “发件人姓名”
from_addr = "xxx@qq.com"
password = “******”
smtp_server = "smtp.exmail.qq.com" #不同邮箱服务器可百度
to_addr = [‘xxxx@qq.com’,’xxxx@qq.com']

#需要配置分割线 ===================================================================

# 清理项目 创建build目录
def clean_project_mkdir_build():
    os.system('cd %s;xcodebuild clean' % project_path) # clean 项目
    os.system('cd %s;mkdir build' % project_path)

def build_project():
    print("build release start")
    os.system ('xcodebuild -list')
    os.system ('cd %s;xcodebuild -workspace %s.xcworkspace  -scheme %s -configuration release -derivedDataPath build ONLY_ACTIVE_ARCH=NO || exit' % (project_path,project_name,scheme))

# 打包ipa 并且保存在当前目录
def build_ipa():
    global ipa_filename
    ipa_filename = time.strftime('%Y-%m-%d-%H-%M-%S.ipa',time.localtime(time.time()))
    ipa_filename = project_name + "_" + ipa_filename;
    os.system ('xcrun -sdk iphoneos PackageApplication -v %s/build/Build/Products/Release-iphoneos/%s.app -o %s/%s'%(project_path,project_name,targerIPA_parth,ipa_filename))

# 重新签名ipa包
def resign_code():
    os.system('cd %s;./resign.sh %s' % (targerIPA_parth,ipa_filename))

# 删除build目录
def rm_project_build():
    os.system('rm -r %s/build' % project_path)

#上传
def upload_fir():
    if os.path.exists("%s/%s" % (targerIPA_parth,ipa_filename)):
        print('watting...')
        # 直接使用fir 有问题 这里使用了绝对地址 在终端通过 which fir 获得
        ret = os.system("fir publish '%s/%s' --token='%s'" % (targerIPA_parth,ipa_filename,fir_api_token))
    else:
        print("没有找到ipa文件")

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

#输出包信息
def ipa_info():
    os.system('fir info %s/%s' % (targerIPA_parth,ipa_filename))


def main():
    # 清理并创建build目录
    clean_project_mkdir_build()
    # 编译coocaPods项目文件并 执行编译目录
    build_project()
    # 打包ipa 并制定到桌面
    build_ipa()
    # 重新签名ipa包
    resign_code()
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
