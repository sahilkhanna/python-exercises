"""
Author: Sahil Khanna
Email: mail@SahilKhanna.org
User can Enter following Options to get the result.
    [OPTION] FUNCTION
    [1] Answer whether user X has access to the device Y.
    [2] List all users who have access to the device Y.
    [3] List all devices that user X can access.
    [4] List all device types the user X has access to.
    [5] For the device type Z, list all users who have access to at least one device of this type.

User may also specify the path of different json files as arguments. For details 
execute ->
    python user_device_policy.py -h 

"""
import json, argparse, os

def user_access_device(user:str, device:str, user_dict: dict, device_dict:dict, policy_dict: dict) -> bool:
    policies = dict()
    if not user:
        print("No User Argument Passed")
        return None
    if not device:
        print("No Device Argument Passed")
        return None
    for _user in user_dict['users']:
        if _user['name'] == user:
            policies = _user['policies']
            break
    if policies:
        for user_policy in policies:
            for _policy in policy_dict['policies']:
                if _policy['id'] == user_policy:
                    if device in _policy['devices']:
                        print(f"{user} HAS ACCESS to {device}")
                        return True
    print(f"{user} DOES NOT HAVE ACCESS to {device}")
    return False

def list_all_user_with_access_to_device(device:str, user_dict: dict, device_dict:dict, policy_dict: dict) -> list:
    attached_policies = list()
    user_list = list()
    for _policy in policy_dict['policies']:
        if device in _policy['devices']:
            attached_policies.append(_policy['id'])
    if not attached_policies:
        print(f"{device} is not attached to any policy")
        return None
    for _user in user_dict['users']:
        for __policy in attached_policies:
            if __policy in _user['policies']:
                user_list.append(_user['name'])
                break
    return user_list

def list_all_devices_that_user_can_access(user:str, user_dict: dict, device_dict:dict, policy_dict: dict) -> list:
    device_list = list()
    policy_list = list()
    for _user in user_dict['users']:
        if _user['name'] == user:
            policy_list = _user['policies']
            break
    for policy in policy_list:
        for _policy in policy_dict['policies']:
            if _policy['id'] == policy:
                device_list.extend(device for device in _policy['devices'] if device not in device_list)
                break
    return device_list

def list_all_device_types_that_user_has_access(user:str, user_dict: dict, device_dict:dict, policy_dict: dict) -> list:
    device_type_list = []
    device_list = list_all_devices_that_user_can_access(user, user_dict, device_dict, policy_dict)
    for device in device_list: 
        for _device in device_dict['devices']:
            if device == _device['id']:
                device_type_list.append(_device['type'])
                break
    return device_type_list

def list_all_users_that_has_access_to_device_type(device_type:str, user_dict: dict, device_dict:dict, policy_dict: dict) -> list:
    user_list = []
    device_list = []
    for _device in device_dict['devices']:
        if device_type == _device["type"]:
            device_list.append(_device["id"])
    for device in device_list:
        _user_list = list_all_user_with_access_to_device(device, user_dict, device_dict, policy_dict)
        if _user_list:
            user_list.extend(user for user in _user_list if user not in user_list)
    return user_list

if __name__ == "__main__":
    CURRENT_DIR = os.getcwd()
    parser = argparse.ArgumentParser(description='User Device Policy checker.')
    parser.add_argument("--device", "-d", type=argparse.FileType('r'), required=False, default="devices.json",
                        help='Path to Device Json File, default=devices.json')
    parser.add_argument("--policy", "-p", type=argparse.FileType('r'), required=False, default="policies.json",
                        help='Path to Policy Json File, default=policies.json')
    parser.add_argument("--user", "-u", type=argparse.FileType('r'), required=False, default="users.json",
                        help='Path to User Json File, default=users.json')
    args = parser.parse_args()
    device_dict = json.load(args.device)
    policy_dict = json.load(args.policy)
    user_dict = json.load(args.user)
    
    print("[OPTION] FUNCTION")
    print("[1] Answer whether user X has access to the device Y.")
    print("[2] List all users who have access to the device Y.")
    print("[3] List all devices that user X can access.")
    print("[4] List all device types the user X has access to.")
    print("[5] For the device type Z, list all users who have access to at least one device of this type.")
    option = input("Enter Option > ")
    if option =='1':
        user = input("Enter User Name > ")
        device = input("Enter Device Name > ")
        ret = user_access_device(user, device, user_dict, device_dict, policy_dict)
        if ret:
            print(f"User:{user} has access to Device:{device}")
        else:
            print(f"User:{user} does NOT have access to Device:{device}")
    elif option =='2':
        device = input("Enter Device Name > ")
        user_list = list_all_user_with_access_to_device(device,user_dict,device_dict,policy_dict)
        if user_list:
            print(f"{user_list} has access to Device: {device}")
        else:
            print(f"No User has access to Device: {device}")
    elif option =='3':
        user = input("Enter User Name > ")
        device_list = list_all_devices_that_user_can_access(user,user_dict,device_dict,policy_dict)
        if device_list:
            print(f"{user} has access to Devices: {device_list}")
        else:
            print(f"{user} has access to ZERO Devices")
    elif option =='4':
        user = input("Enter User Name > ")
        device_type_list = list_all_device_types_that_user_has_access(user,user_dict,device_dict,policy_dict)
        if device_type_list:
            print(f"{user} has access to Device types:{device_type_list}")
        else:
            print(f"{user} has access to ZERO Device types")
    elif option =='5':
        device_type = input("Enter Device Type > ")
        user_list = list_all_users_that_has_access_to_device_type(device_type,user_dict,device_dict,policy_dict)
        if user_list:
            print(f"{user_list} has access to Device type: {device_type}")
        else:
            print(f"ZERO USER has access to Device type: {device_type}")
    # functions[int(option)]()