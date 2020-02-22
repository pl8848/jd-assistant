#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    asst = Assistant()        # ³õÊ¼»¯
    asst.login_by_QRcode()    # É¨ÂëµÇÂ½
    asst.clear_cart()
    asst.exec_reserve_seckill_by_time(sku_id=100011462830, buy_time="2020-02-22 10:59:59.99999", retry=10, interval=0.2)