import requests
from jsbeautifier import beautify

# make the get request
r = requests.get("https://developers.google.com/machine-learning/crash-course").text

# make the JS look normal (typical line breaks not just a huge block of code)
print(beautify(r))
