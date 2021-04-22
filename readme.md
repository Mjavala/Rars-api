# Rars API
This repo houses the REST API for communication with the Rars storage and retrieval system. Requests from a client will be processed here before handing off instructions to the SCARA robot. Currently this API does not interface with the SCARA robot directly as the communication system in the robot has not yet been defined; development is ongoing.

## Endpoints

- store_slide (POST)
```
{
    "timestamp": 1221445323,
    "payload": "KL20-12031_B_2.35.1"
}
```

- store_slides (POST)
```
{
    "timestamp": 1221445323,
    "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]
}

- retrieve_slide (POST)
```
{
    "timestamp": 1221445323,
    "payload": "KL20-12031_B_2.35.1"
}
```

Slides can be retrieved by a number of different fields in the database.

- retrieve_films (POST)
```
by id's
{
    "timestamp": 1221445323,
    'type': 'id'
    "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]
}

by casetype
{
    "timestamp": 12412354325,
    "type": "casetype",
    "payload": "case-type-string"
}
```

Each endpoint will return a boolean True (success) / False (failure).
```
{
    "response": true
}
```

