## Django app as a rough orchestrator

### Plan: 

Using django app as an hybrid and isolated orchestrator which can collect low-tech(SMS) data via Twiio SMS API, use OpenAI api to request more info via SMS, process it, and then produce a JSON which can be handed off to the main client.

SMS on 2G is a robust way to collect resource requests on the ground, when higher tech options (chat channels and web forms) are not working. Also, not tech-savvy people might find it way easier to use SMS for requests.

Using django as a client/API hybrid makes it easier to orchestrate 2 3rd party apis and storing data during processing (as might need to ask for more info from the sender).

robust comms coordination not governance - handled in the main client.

### TO DO:

 - bool for direct_to_json - if reoutes through openAI or not and goes ddirectly to JSON output - easier to test main client as can isolate hapi.

Pos JSON example:

```json
{
    "phone_number": "+1234567890",
    "message_content": "Need water at coordinates 49.233, 28.467",
    "status": "complete",
    "additional_info": {
        "needed_items": ["water", "food"],
        "location": "coordinates 49.233, 28.467"
    }
}
```

### Future:\

Ideally would make it more modular with a dedicate client and dedicated APIs which consume respective 3rd party APIs.
Also, could research if Signal Protocol could be used.