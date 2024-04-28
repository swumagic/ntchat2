<h1 align="center">NtChat2</h1>
<p align="center">
    <a href="https://github.com/smallevilbeast/ntchat/releases"><img src="https://img.shields.io/badge/release-0.1.1-blue.svg?" alt="release"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?" alt="License"></a>
</p>




## 介绍

- 基于pc微信的api接口, 类似itchat项目
- 支持收发文本、群@、名片、图片、文件、视频、链接卡片等
- 支持好友和群管理
  
## 支持的微信版本下载
- [WeChatSetup3.6.0.18.exe](https://webcdn.m.qq.com/spcmgr/download/WeChat3.6.0.18.exe)

## 安装

```bash
pip install ntchat2
```
国内源安装
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntchat2
```

## 简单入门实例

有了ntchat，如果你想要给文件传输助手发一条信息，只需要这样

```python
# -*- coding: utf-8 -*-
import sys
import ntchat2

wechat = ntchat2.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(faked_wechat_version="3.9.10.19", smart=False)

# 等待登录
wechat.wait_login()

# 向文件助手发送一条消息
wechat.send_text(to_wxid="filehelper", content="hello, filehelper")

try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat2.exit_()
    sys.exit()
```

## 获取联系人和群列表
```python
# -*- coding: utf-8 -*-
import sys
import ntchat2

wechat = ntchat2.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(faked_wechat_version="3.9.10.19", smart=False)

# 等待登录
wechat.wait_login()

# 获取联系人列表并输出
contacts = wechat.get_contacts()

print("联系人列表: ")
print(contacts)

rooms = wechat.get_rooms()
print("群列表: ")
print(rooms)


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat2.exit_()
    sys.exit()
```

## 监听消息并自动回复

```python
# -*- coding: utf-8 -*-
import sys
import ntchat2

wechat = ntchat2.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(faked_wechat_version="3.9.10.19", smart=False)


# 注册消息回调
@wechat.msg_register(ntchat2.MT_RECV_TEXT_MSG)
def on_recv_text_msg(wechat_instance: ntchat2.WeChat, message):
    data = message["data"]
    from_wxid = data["from_wxid"]
    self_wxid = wechat_instance.get_login_info()["wxid"]

    # 判断消息不是自己发的，并回复对方
    if from_wxid != self_wxid:
        wechat_instance.send_text(to_wxid=from_wxid, content=f"你发送的消息是: {data['msg']}")


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat2.exit_()
    sys.exit()
```
