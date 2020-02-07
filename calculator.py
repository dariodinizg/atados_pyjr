def stock_calculator(stock_prices: list) -> float:
    """ 
    Calculates what could be the best profit for a trade operation 
    based on a list with stock prices of a given period.

    Ex:
    import time
    import pandas as pd

    df = pd.read_csv('itsa4_historica.csv')
    best_profit = stock_calculator(df['FECHAMENTO'])
    print(f'Best selling profit: R${best_profit:.2f}')

    Output:
    Best selling profit: R$1.81
  
    Performance time: 0.021959781646728516

    """
    profit = 0
    for index, quote in enumerate(stock_prices):
        higher_price = max(stock_prices[index::])
        comparison = higher_price - quote
        if higher_price > quote:
            if comparison > profit:
                profit = comparison
    return profit
