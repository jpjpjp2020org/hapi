## Django app as a rough orchestrator

### Plan: 

Using django app as an hybrid and isolated orchestrator which can collect low-tech(SMS) data via Twiio SMS API, use OpenAI api to request more info via SMS, process it, and then produce a JSON which can be handed off to the main client.

SMS on 2G is a robust way to collect resource requests on the ground, when higher tech options (chat channels and web forms) are not working. Also, not tech-savvy people might find it way easier to use SMS for requests.

Using django as a client/API hybrid makes it easier to orchestrate 2 3rd party apis and storing data during processing (as might need to ask for more info from the sender).

robust comms coordination not governance - handled in the main client.

### Data consumption:

- For GET requests can use these endpoints with the latest ngrok free url:

    - https://0110-2001-1530-1003-8e5-34f7-882d-2993-9fca.ngrok-free.app/api/sms-data/ 
    - https://0110-2001-1530-1003-8e5-34f7-882d-2993-9fca.ngrok-free.app/api/sms-val-dump/

- sms-data returns JSON for db data which OpenAI API helper deemed complete after evaluation.
- sms-val-dump returns JSON for db data which OpenAI API helper deemed incomplete after evaluation.
- Can use these in separate updatable lists on the main dashboard - incomplete one allows to check that no message is missing.

JSON example for sms-data (complete):

```json
[
    {
        "id": 2,
        "phone_number": "phone number here",
        "message_content": "Need two diesel generators in Pärnu Pikk tänav 1 on next Wednesday 4th",
        "resource_needed": "diesel generators",
        "quantity": "two",
        "location": "Pärnu Pikk tänav 1",
        "timeline": "next Wednesday 4th",
        "evaluation": "complete",
        "created_at": "2024-08-30T19:45:19.131998Z",
        "updated_at": "2024-08-30T19:45:19.132051Z"
    },
    {
        "id": 3,
        "phone_number": "phone number here",
        "message_content": "200L drinking water in Peraküla beach parking lot as soon as possible ",
        "resource_needed": "drinking water",
        "quantity": "200L",
        "location": "Peraküla beach parking lot",
        "timeline": "as soon as possible",
        "evaluation": "complete",
        "created_at": "2024-08-30T19:47:55.007213Z",
        "updated_at": "2024-08-30T19:47:55.007269Z"
    }
]
```

JSON example for sms-val-dump (incomplete):

```json
[
    {
        "id": 1,
        "phone_number": "phone number here",
        "message_content": "Vaja oleks vett ASAP test ",
        "created_at": "2024-08-30T19:46:57.410387Z"
    }
]
```

### Future:\

Ideally would make it more modular with a dedicate client and dedicated APIs which consume respective 3rd party APIs.
Also, could research if Signal Protocol could be used.