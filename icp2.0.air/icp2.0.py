# -*- encoding=utf8 -*-
__author__ = "aijinka"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.ios import iosPoco
poco = iosPoco()
poco("ic_tab_personal").click()
poco("交易紀錄").click()
poco("支付工具").click()
poco("icp ic left nav white arrow").click()
poco("交易限額").click()
poco("icp ic left nav white arrow").click()
poco("ic_tab_home").click()
