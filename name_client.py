import requests

# Info to send
out_data = {"name": "Anusha Krishnamoorthy", "net_id": "ak701",
            "e-mail": "ak701@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
