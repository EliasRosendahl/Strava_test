from stravalib.client import Client
import polyline


def main():
    access_token = input("access token: ")
    client = Client(access_token)

    activities = client.get_activities(limit=100)


    points = []    
    for activity in activities:
        activity = activity.to_dict()
        print("--------------")
        poly = activity['map']['summary_polyline']
        points.extend(polyline.decode(poly))


    all_routes = polyline.encode(points)
    print(all_routes)

if __name__ == "__main__":
    main()
