import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")  # sending a request
print(r)
print(type(r))
print(r.status_code)  # 404 for bad response
print(r.text)  # Response - What came back from the server
# Has a dictionary per branch
branches = r.json()
for branch in branches:
    print(branch["name"])

