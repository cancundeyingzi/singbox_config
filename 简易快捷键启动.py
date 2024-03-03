import os
import time

import keyboard
系统代理开关=0
网卡代理开关=0

def 系统代理():
    global 系统代理开关,网卡代理开关
    if 系统代理开关==0:
        os.system('taskkill /f /im %s' % 'sing-box.exe')
        网卡代理开关 = 0
        time.sleep(1)
        result = os.popen('D:\\v2rayN-With-Core\\bin\sing_box\\sing-box.exe run -c D:\\v2rayN-With-Core\\bin\sing_box\肥羊3.json')
        系统代理开关=1
        return
    if 系统代理开关 == 1:
        os.system('taskkill /f /im %s' % 'sing-box.exe')
        系统代理开关=0

def 网卡代理():
    global 网卡代理开关,系统代理开关
    if 网卡代理开关==0:
        os.system('taskkill /f /im %s' % 'sing-box.exe')
        系统代理开关 = 0
        time.sleep(1)
        result = os.popen('D:\\v2rayN-With-Core\\bin\sing_box\\sing-box.exe run -c D:\\v2rayN-With-Core\\bin\sing_box\肥羊3副本.json')
        网卡代理开关=1
        return
    if 网卡代理开关 == 1:
        os.system('taskkill /f /im %s' % 'sing-box.exe')
        网卡代理开关=0

def abc(x):
    print(x, x.scan_code)
    if x.event_type == 'down':

        d = {62:"系统代理()",61:"网卡代理()"}
        eval(d.get(x.scan_code,'print("其他按键")'))  # exec没有返回值eval必须有返回值,

if __name__ == '__main__':

    keyboard.hook(abc)
    keyboard.wait()
