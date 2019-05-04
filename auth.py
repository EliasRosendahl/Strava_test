from stravalib.client import Client

def main():
    access_token = input("token: ")
    client = Client(access_token)
    activities = client.get_activities(limit=100)
    print(activities)

if __name__ == "__main__":
    main()
