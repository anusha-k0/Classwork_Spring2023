import requests

# POST MESSAGE
send_data = {"user": "ak701", "message": "Hi Pooja!"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = send_data)
print(r.status_code)
print(r.text)

# GET MESSAGE
r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/PoojaParameswaran")
# print(r)
# print(type(r))
# print(r.status_code)  # 404 for bad response
print(r.text)  # Response - What came back from the server
# Has a dictionary per branch
# branches = r.json()
# for branch in branches:
    # print(branch["name"])