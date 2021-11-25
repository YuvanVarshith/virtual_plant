
import requests
import datetime

# get the events for a user and iterate through the json to get the last days commits only


# endpoint to get the profiles activity
endpoint = 'https://api.github.com/users/cosmoglint/events'
response = requests.get(endpoint)
data = response.json()


today = datetime.datetime.now()

filtered_data = list(filter(lambda x: (today - datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%SZ") < datetime.timedelta(days=1)), data))

print(filtered_data)

for i in data:
    created_at = i['created_at']
    # extract the time of each event from json
    event_date = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    print(event_date)
    # filtered_data = list(data.filter(lamda x: (today - datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%SZ") < datetime.timedelta(days=1))
    # print(i["id"])
