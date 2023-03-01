import requests

# GET MESSAGE
get_r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/ak701")
print(get_r.text)

get_r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F1")
print(get_r2.text)

get_r3 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F3")
print(get_r3.text)

# POST MESSAGE
out_data = {"Name": "ak701", "Match": "Yes"}
post_r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(post_r.status_code)
print(post_r.text)
