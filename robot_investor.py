import time

__author__ = 'cemkiy'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kassandraproject.settings")
from bitcoin_analyze.analyze import *

class robot_investor:
    def __init__(self):
        self.analyze = analyze()
        self.bitcoin_bought_price = 0.0
        self.bitcoin_bought_amount = 0.0

    def theater_stage(self):
        infinite_profit_loop = True
        if self.main_result:
            while(infinite_profit_loop):
                profit = (self.bitcoin_bought_price * self.bitcoin_bought_amount) + (self.bitcoin_bought_price * self.bitcoin_bought_amount) * 0.4
                if self.get_now_ask_price() > profit:
                    self.sell_bitcoins()
                    infinite_profit_loop = False
                else:
                    time.sleep(60)


    def buy_bitcoins(self):
        money_amount = self._btcturk.balance()['money_available']
        self._btcturk.buy(price=money_amount)


    def sell_bitcoins(self):
        bitcoin_amount = self._btcturk.balance()['bitcoin_available']
        self._btcturk.sell(amount=bitcoin_amount)






def main():
    pass

if __name__ == "__main__":
    main()