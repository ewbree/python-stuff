
###
### Logs into FortiGate as normal web user and returns cookies to use for other calls.
###

### import external modules:
import json
import urllib3
urllib3.disable_warnings()


### local Python scripts here:
import login_data
from functions import authentication, firewall


host_address = login_data.host_address
host_port = login_data.host_port
host = [host_address,host_port]

username = login_data.username
password = login_data.password


cookie = authentication.admin_login(host,username,password)

print(json.dumps(firewall.get_address(host,cookie),indent=4))
print(json.dumps(firewall.get_address(host,cookie,address="China"),indent=4))

authentication.admin_logout(host,cookie)
