from stravalib.client import Client

def main():
    user_id = input("user id: ")
    access_token = input("access token: ")
    client = Client(access_token)

    #Build url or authorizing app
    url = client.authorization_url(client_id=user_id, redirect_uri='http://127.0.0.1:5000/authorization', approval_prompt='auto', scope='activity:read_all')
    print(url)

    #Extract access code from url response
    access_code = input("access code: ")
    client_secret = input("client secret: ")

    #Get permanent access token
    permanent_access_token = client.exchange_code_for_token(user_id, client_secret, access_code)
    print(permanent_access_token)

    
if __name__ == "__main__":
    main()
