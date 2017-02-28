# coding=utf-8
import datetime

from qqbot import QQBot


def msg_log(chatroom_name, user_name, time, content):
    log = '[%s] %s (%s): %s\n' % (chatroom_name, user_name, time, content)
    logfile = 'msg_log/%s' % datetime.date.today().strftime("%Y-%m-%d.txt")
    with open(logfile, 'a') as file_fb:
        file_fb.write(log)


class MyQQBot(QQBot):
    def onPollComplete(self, msgType, from_uin, buddy_uin, message, create_time):
        if msgType == 'group':
            group = self.getGroupByUin(from_uin)
            gName = group['name']
            bName = group['member'].get(buddy_uin, '未知用户')
            try:
                msg_log(gName, bName, create_time, message)
            except Exception as e:
                pass

myqqbot = MyQQBot()
myqqbot.Login()
myqqbot.Run()