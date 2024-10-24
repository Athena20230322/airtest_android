# -*- encoding=utf8 -*-
__author__ = "aijinka"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.ios import iosPoco
poco = iosPoco()
poco(rect="{'y': 212, 'x': 40, 'width': 56, 'height': 57}").click()
poco("首頁").click()
poco("高鐵國旅").click()
poco("首頁").click()
poco("首頁").click()
poco("首頁").click()
poco("Window").child("Other")[1].child("無法取得街口授權").child("Other").child("Other").child("Other")[1].child("ScrollView")[1].child("Other").child("Other").child("Other")[0].click()
poco("dismiss v2").click()
poco("dismiss v2").click()
poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("WebView").child("WebView").child("WebView").child("Other").child("Other").offspring("街口好友推薦碼").child("Other")[11].click()

