import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='JPYPOHOOT5ZYG2MEOYJU1RYJTZR3JKHZBHFYWLVXP11L3EB2',
  client_secret='B4DECH4D14D1TSI1MSDZUJQEMQ5MRTJV3SORCDJYGXDJMNBU',
  v='20180323',
  ll='40.7243,-74.0018',
  query='restaurant',
  limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

