# Users devices and policies

Given 3 config files: `devices.json`, `users.json`, `policies.json` write Python code that can perform the following functions:

1. Answer whether user X has access to the device Y.
2. List all users who have access to the device Y.
3. List all devices that user X can access.
4. *(Optional)* List all device types the user X has access to.
5. *(Optional)* For the device type Z, list all users who have access to at least one device of this type.

*Details:* 

- `devices.json` contains the array of devices where each `device` object has unique `id` and `type`

    Example:
    ```json
    {
        "devices":
        [
            {
                "id": "kettle_0",
                "type": "kettle"
            },
            {
                "id": "garageDoor",
                "type": "door"
            },
            {
                "id": "bedroomDoor",
                "type": "door"
            }
        ]
    }
    ```
    
- `policies.json` contains the array of policies where each `policy` object has unique `id` and the array of devices the policy grants access to

    Example:
    ```json
    {
        "policies":
        [
            {
                "id": "KettlePolicy",
                "devices": ["kettle_0", "kettle_1"]
            },
            {
                "id": "GaragePolicy",
                "devices": ["garageDoor", "garageBlinds"]
            }
        ]
    }
    ```
    
- `users.json` contains the array of users where each `user` object has unique `name` and the array of policies they are in
  
    Example:
    ```json
    {
        "users": 
        [
            { 
                "name" : "John",
                "policies": ["KettlePolicy", "BlindsPolicy", "MasterBedroomPolicy"]
            },
            {
                "name" : "Doe",
                "policies": ["GaragePolicy", "BlindsPolicy", "DoorsPolicy"]
            }
        ]
    }
    ```