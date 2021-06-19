# Rars API
This repo houses the REST API for communication with the Rars storage and retrieval system, as well as websocket support in order to communicate with the SCARA robot or event-driven scheduling system. This API will be the only external interface, and will communicate with the task scheduler and SCARA/Gantry system; relaying status updates to clients. <br>

Currently this API does not interface with the SCARA robot directly as the communication system in the robot has not yet been defined; websocket support was added to facilitate future integrations.

## Endpoints

- **store_slide** (POST)
```
{
    "timestamp": 1221445323,            # unix number
    "payload": "KL20-12031_B_2.35.1"    # String
    "storage_box": "box_1",             # String optional (?)
}
```

- **store_slides** (POST)
```
{
    "timestamp": 1221445323,                                    # unix number
    "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]    # [String]
    "storage_box": "box_1",                                     # String optional (?)
}
```

- **get_slide** (POST)
```
{
    "timestamp": 1221445323,            # unix number
    "payload": "KL20-12031_B_2.35.1"    # String
}
```

Mulitple slides can be retrieved by a number of different fields in the database, some of these are yet to be defined.

-  **get_slides** (POST)
```
by ids
{
    "timestamp": 1221445323,
    'type': 'ids'
    "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]
}

by casetype
{
    "timestamp": 12412354325,
    "type": "casetype",
    "payload": "case-type-string"
}
```
