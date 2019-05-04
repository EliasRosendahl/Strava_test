from stravalib.client import Client

def main():
    user_id = input("user id: ")
    client = Client(access_token)

    #Build url or authorizing app
    url = client.authorization_url(client_id=user_id, redirect_uri='http://127.0.0.1:5000/authorization')
    print(url)

    #Extract access code from url response
    access_code = input("access code: ")
    client_secret = input("client secret: ")

    #Get permanent access token
    access_token = client.exchange_code_for_token(user_id, client_secret, access_code)
    print(new_access_token)

    
if __name__ == "__main__":
    main()
