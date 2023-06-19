
import requests




def get_address(host:list,cookie:dict,vdom="root",address=""):
    """
    Returns a JSON of either all addresses or a single address if one is given.
    By default requests addresses against the root VDOM.

    >>> get_address([ip,port],cookie)
    
    >>> get_address([ip,port],cookie,address="RFC1918_Class_C")

    >>> get_address([ip,port],cookie,"Customer_1","RFC1918_Class_C")
    
    """
    url = "https://" + host[0] + ":" + host[1] + "/api/v2/cmdb/firewall/address"

    if address != "":
        url = url + "/" + address
      
    url = url + "/?vdom=" + vdom

    response = requests.get(
        verify = False,
        url = url,
        cookies = cookie
    )
    return response.json()