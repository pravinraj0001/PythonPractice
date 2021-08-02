# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:52:45 2021

@author: Pravin
"""

# Declarative stye of programming like mathematical notations
# Here we are using select kind of statements replication in python by importing
# data from the input file

fields = (line.split() for line in open("portfolio.txt"))
portfolio = [{'name' : f[0],
              'shares': int(f[1]),
              'price' : float(f[2])}
                for f in fields]

# filtering condtions in the queries like where
msft = [s for s in portfolio if s['name'] == 'MSFT']
large_holdings = [s for s in portfolio if s['shares']*s['price'] >= 10000]

print("select * from portfolio as p : "+ str(portfolio))
print("where p.name = 'MSFT' : " + str(msft))
print("and large_holdings : " + str(large_holdings))

