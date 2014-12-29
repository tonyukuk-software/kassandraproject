import time

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
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
        self.analyze.guess_what()
        print self.analyze.get_now_ask_price()
        infinite_profit_loop = True
        infinite_profit_loop_counter = 0
        if self.analyze.main_result:
            print 'Bitcoin will be high!'
            # self.buy_bitcoins()
            while(infinite_profit_loop):
                print self.analyze.get_now_ask_price()
                profit = (self.bitcoin_bought_price * self.bitcoin_bought_amount) + (self.bitcoin_bought_price * self.bitcoin_bought_amount) * 0.4
                earn_money_amount = (self.analyze.get_now_ask_price() * self.bitcoin_bought_amount) + (self.analyze.get_now_ask_price() * self.bitcoin_bought_amount) * 0.4
                print 'profit' + ' ' + str(profit)
                if earn_money_amount > profit:
                    print 'You earned money yo bitch!'
                    # self.sell_bitcoins()
                    infinite_profit_loop = False
                else:
                    print 'Still Waiting!'
                    infinite_profit_loop_counter += 1
                    if infinite_profit_loop_counter == 10:
                        if self.bitcoin_bought_price > self.analyze.get_now_ask_price():
                            print 'sorry Wrong Guess!'
                            self.analyze.send_new_rank()
                    time.sleep(60)
        else:
            time.sleep(120)


    def buy_bitcoins(self):
        self.bitcoin_bought_price = self.analyze.get_now_ask_price()
        money_amount = self._btcturk.balance()['money_available']
        self._btcturk.buy(price=money_amount)
        time.sleep(60)
        self.bitcoin_bought_amount = self._btcturk.balance()['bitcoin_available']
        print 'Bought Bitcoin' + ' ' + str(self.bitcoin_bought_amount)


    def sell_bitcoins(self):
        bitcoin_amount = self._btcturk.balance()['bitcoin_available']
        print 'Sold Bitcoin' + ' ' + str(bitcoin_amount)
        self._btcturk.sell(amount=bitcoin_amount)
        time.sleep(60)
        self.bitcoin_bought_amount = self._btcturk.balance()['bitcoin_available']



def main():
    robot = robot_investor()
    while(True):
        print 'Theater Start!'
        robot.theater_stage()

if __name__ == "__main__":
    main()