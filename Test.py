import pandas as pd

HDI_value = pd.read_csv("./human-development-index.csv")
first_foodprice = pd.read_csv("./FAOFP1990_2022.csv")
second_foodprice = pd.read_csv("./global_food_prices.csv", low_memory=False)
#third_foodprice = pd.read_csv("./wfp_market_food_prices.csv", low_memory=False, encoding='utf-8')
#population_data = pd.read_csv("./API_data.csv", low_memory=False, error_bad_lines=False)
