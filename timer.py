#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rumps
import time

@rumps.clicked(u'1分')
def decision_time(_):
    global minutes
    minutes = 60
    global start
    start = time.time()

@rumps.clicked(u'3分')
def decision_time(_):
    global minutes
    minutes = 60*3
    global start
    start = time.time()

@rumps.clicked(u'5分')
def decision_time(_):
    global minutes
    minutes = 60*5
    global start
    start = time.time()


@rumps.clicked(u'10分')
def decision_time(_):
    global minutes
    minutes = 60*10
    global start
    start = time.time()

@rumps.clicked(u'15分')
def decision_time(_):
    global minutes
    minutes = 60*15
    global start
    start = time.time()

@rumps.clicked(u'20分')
def decision_time(_):
    global minutes
    minutes = 60*20
    global start
    start = time.time()


@rumps.clicked(u'30分')
def decision_time(_):
    global minutes
    minutes = 60*30
    global start
    start = time.time()

@rumps.clicked(u'60分')
def decision_time(_):
    global minutes
    minutes = 60*60
    global start
    start = time.time()

#1秒ごとに更新
@rumps.timer(1)
def measure_time(_):
    timer_now = time.time()
    remaining_time = int(minutes - (timer_now - start))
    timer_minutes = str((remaining_time) // 60)
    timer_second = str((remaining_time) % 60)
    if int(timer_second) < 10:
        timer_second = '0' + timer_second

    if (remaining_time) > 0:
        app.title = '残り時間:'+ timer_minutes +':'+ timer_second
    elif (remaining_time) <=0:
        app.title = 'TIMEUP'
        rumps.alert(message='時間になりました!')
        rumps.quit_application()


if __name__ == "__main__":
    app = rumps.App("Timer", title = 'タイマー')
    app.run()
