# -*- encoding: utf-8 -*-
"""
@File    : 04.py
@Time    : 2019/8/29 14:14
@Author  : HeKai
@Email   : hek@corp.21cn.com
@Software: PyCharm
"""

import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()