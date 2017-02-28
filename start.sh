#!/bin/bash
killall -9 python
source env/bin/activate

echo "退出按ctrl＋c结束程序"
echo "聊天数据记录在msg_log文件夹里面"

env/bin/python main.py 


