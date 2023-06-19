
import requests




def admin_login(host:list,username:str,password:str) -> dict:
    """
    Authenticates to the given host in a [host,port] list with the provided username and password as string.

    >>> admin_login([ip,port],admin,password)
    {'APSCOOKIE_443': '"<CONTENT>"', 'ccsrftoken_443': '"<CONTENT>"'}
    """
    url = "https://" + host[0] + ":" + host[1] + "/logincheck"

    data = "username=" + username + "&secretkey=" + password + "&ajax=1"

    response = requests.post(
        verify = False,
        url = url,
        data = data
    )

    cookie = (response.cookies.get_dict())

    ### Response code is always 200, regardless of credentials. Hence check of cookie length. Must be 2 or more depending on OS version.
    if len(cookie) > 1:
        return(cookie)
    else:
        print("Something went wrong with the login. Be sure that the username and password are correct!")
        # print ("\nRaw response from POST token request:\n" + response)
        quit()




def admin_logout(host:list,cookie:dict) -> str:
    """
    De-authenticates to the given host in a [host,port] list with the provided cookie also in a dictionary format.

    >>> admin_logout([ip,port],cookie)
    Reponse: 200
    """
    url = "https://" + host[0] + ":" + host[1] + "/logout"

    response = requests.get(
        verify = False,
        url = url,
        cookies = cookie
    )

    ### Response code is always 200. Regardless of cookies.
    print ("\nResponse: " + str(response.status_code))
