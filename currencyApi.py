import currencyapicom

client = currencyapicom.Client('7GQ2Xn7ukeH5O4juC3NSGuyKT8pa5kIbAiFvlp3a')
result = client.latest('USD',currencies=['EUR','GBP','CHF','JPY','RUB','TRY'])
currencies={
    'EUR':result['data']['EUR']['value'],
    'GBP':result['data']['GBP']['value'],
    'CHF':result['data']['CHF']['value'],
    'JPY':result['data']['JPY']['value'],
    'RUB':result['data']['RUB']['value'],
    'TRY':result['data']['TRY']['value']
}