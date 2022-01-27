#!/usr/bin/env python3

import algosdk
import json
import base64
import datetime

my = algosdk.v2client.indexer.IndexerClient(indexer_token="",indexer_address="https://algoindexer.algoexplorerapi.io")
acct = 'TISUX6HMR6GLI4B7CBZLUJCV4M7IGKPVMP6P2SSUG5XXL33RSJH7KHLEXI'
acct = input("Enter your account id:")
try:
    response = my.search_transactions_by_address(address=acct, min_amount=1, limit=1000, asset_id=27165954)

    if 'transactions' in response:
        for transaction in response['transactions']:
            if 'note' in transaction and acct == transaction['asset-transfer-transaction']['receiver']:
                amount = transaction['asset-transfer-transaction']['amount']
                note = transaction['note']
                streams = json.loads(base64.b64decode(note))['streams']
                planets_per_stream = amount / streams
                device = json.loads(base64.b64decode(note))['deviceId']
                tDate =  datetime.datetime.fromtimestamp(transaction['round-time']).isoformat()
                print("Date:{}\tDevice:{}\tStreams:{}\tPlanets:{}\tStreams/Planet:{}".format(tDate, device, streams, amount/1000000, planets_per_stream/1000000))
    else:
        print("Something went wrong")

except algosdk.error.IndexerHTTPError:
    print("T")
except:
    print("A")