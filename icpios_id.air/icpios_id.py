# -*- encoding=utf8 -*-
__author__ = "aijinka"

from airtest.core.api import *
from poco.drivers.ios import iosPoco
auto_setup(__file__)
connect_device("ios:///127.0.0.1:8100")
#keyevent("HOME")
#stop_app("tw.com.icash.i.icashpay20240625")
#start_app("tw.com.icash.i.icashpay20240625")
poco = iosPoco()
poco(value="登入帳號").click()
text("tester350")
poco(value="登入密碼").click()
text("Aa123456")
poco(value="登 入").click()
sleep(1.0)
poco(name="儲值").click()
sleep(1.0)
poco(name="現金儲值").click()
poco(name="icp ic left nav white arrow").click()
sleep(1.0)
poco(name="自帶杯儲值").click()
poco(name="close v3").click()
sleep(1.0)
poco(name="中獎發票儲值").click()
poco(name="close v3").click()
sleep(1.0)
poco(name="close v3").click()
poco(name="我的").click()
sleep(1.0)
poco(name="個人資訊").click()
sleep(1.0)
touch(Template(r"tpl1719303156080.png", record_pos=(-0.397, -0.495), resolution=(1124, 2436)))
touch(Template(r"tpl1719303159251.png", record_pos=(0.01, 0.376), resolution=(1124, 2436)))
touch(Template(r"tpl1719303165409.png", record_pos=(-0.24, -0.502), resolution=(1124, 2436)))
touch(Template(r"tpl1719303168208.png", record_pos=(-0.329, 0.526), resolution=(1124, 2436)))
touch(Template(r"tpl1719303172910.png", record_pos=(-0.093, -0.512), resolution=(1124, 2436)))
touch(Template(r"tpl1719303177206.png", record_pos=(0.331, 0.515), resolution=(1124, 2436)))
touch(Template(r"tpl1719303179978.png", record_pos=(0.085, -0.509), resolution=(1124, 2436)))
touch(Template(r"tpl1719303182615.png", record_pos=(-0.329, 0.655), resolution=(1124, 2436)))
touch(Template(r"tpl1719303186576.png", record_pos=(0.246, -0.502), resolution=(1124, 2436)))
touch(Template(r"tpl1719303188897.png", record_pos=(0.335, 0.655), resolution=(1124, 2436)))
touch(Template(r"tpl1719303191826.png", record_pos=(0.403, -0.509), resolution=(1124, 2436)))
touch(Template(r"tpl1719303195150.png", record_pos=(-0.001, 0.808), resolution=(1124, 2436)))
poco(name="icp ic left nav white arrow").click()
poco(name="交易限額").click()
poco(name="icp ic left nav white arrow").click()
poco(name="授權扣款管理").click()
poco(name="icp ic left nav white arrow").click()
poco(name="使用教學").click()
poco(name="icp ic left nav white arrow").click()
swipe(Template(r"tpl1719306777226.png", record_pos=(-0.446, 0.394), resolution=(1124, 2436)), vector=[-0.0107, -0.3871])
poco(name="常見問題").click()
poco(name="icp ic left nav white arrow").click()
poco(name="服務條款").click()
poco(name="icp ic left nav white arrow").click()
poco(name="聯絡我們").click()
poco(name="icp ic left nav white arrow").click()
poco(name="image main home").click()
poco(name="我的").click()
sleep(1.0)
poco(name="會員卡").click()
sleep(1.0)
poco(name="環球購物中心(僅環球點數)").click()
sleep(1.0)
poco(name="icp ic left nav white arrow").click()
poco(name="icp ic left nav white arrow").click()
poco(name="image main home").click()