
import requests
import json

url = 'https://api.pancakeswap.info/api/v2/tokens/0x40f906e19b14100d5247686e08053c4873c66192'
data = requests.get(url)
print(data)


# url = 'https://api.pancakeswap.info/api/v2/tokens/0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82'
# data = requests.get(url).json()

# price = float(data['data']['price'][:6]) # to get the first 6 digits of the price

# print(price)





# def calcSell(tokenAddress):
#     apiURL = "https://api.pancakeswap.info/api/v2/tokens/"
#     response = requests.get(url = apiURL + tokenAddress)
#     price = extractPriceFromRaw(response)
#     return price

# def extractPriceFromRaw(response):
#     jsonRaw = response.json()
#     price = jsonRaw['data']['price']
#     return price

# CAKE = '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82'
# print(calcSell(CAKE))