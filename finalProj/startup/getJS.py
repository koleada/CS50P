import requests
from jsbeautifier import beautify

# make the get request
r = requests.get(
    "https://static.tradingview.com/static/bundles/27883.3d2e60e6d67d4467f4f5.js"
)

# get the actual JS
js = r.text

# make the JS look normal (typical line breaks not just a huge block of code)
print(beautify(js))
