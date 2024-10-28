from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/crypto')
def crypto():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    Bits = {
        'ids': 'bitcoin,ethereum,tether,binancecoin,ripple,usd-coin,cardano,solana,dogecoin,tron,'
                'litecoin,polkadot,avalanche-2,chainlink,matic-network,shiba-inu,wrapped-bitcoin,dai,'
                'bitcoin-cash,stellar,uniswap,monero,toncoin,cosmos,okb,leo-token,ethereum-classic,'
                'internet-computer,algorand,filecoin,vechain,aave,eos,tezos,theta-token,zcash,neo,'
                'huobi-token,pancakeswap-token,fantom,maker,iota,the-graph,bittorrent,havven,'
                'compound-governance-token,dash,decentraland,chiliz,enjincoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=Bits)

    with open('Crypto Info.json', 'w') as file:
        json.dump(response.json(), file, indent=4)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
