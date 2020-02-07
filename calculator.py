def stock_calculator(stock_prices: list) -> float:
    """ 
    Calculates what could be the best profit for a trade operation 
    based on a list with stock prices of a given period.
    """
    profit = 0
    for index, quote in enumerate(stock_prices):
        higher_price = max(stock_prices[index::])
        comparison = higher_price - quote
        if higher_price > quote:
            if comparison > profit:
                profit = comparison
    return profit

"""
import time
import pandas as pd

df = pd.read_csv('itsa4_historica.csv')
t0 = time.time()
best_profit = stock_calculator(df['FECHAMENTO'])
t1 = time.time()
print(f'Best selling profit: R${best_profit:.2f}')
print(f'Execution time: {t1 - t0}')
"""