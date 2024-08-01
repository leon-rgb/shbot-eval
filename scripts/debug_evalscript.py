import shbot_eval

list = [
    "Turning on the Zwischenstecker now. { \"action\": \"turn-on\", \"deviceID\": \"hdm:HomeMaticIP:3014F711A000049878593469\", \"device\": \"POWER_METER_SWITCH\", \"room\": \"Schlafzimmer\", \"name\": \"Zwischenstecker\" }",
    "Currently, the TV and the Living Room Lamp are consuming power. { \"action\": 'none', 'deviceID': 'hdm:HomeMaticIP:3014F711A000049878593477', 'device': 'POWER_METER_SWITCH', 'room': 'Living Room', 'name': 'TV' }",
    "The TV is currently switched ON. { 'action': 'none', 'deviceID': 'hdm:HomeMaticIP:3014F711A000049878593477', 'device': 'POWER_METER_SWITCH', 'room': 'Living Room', 'name': 'TV' }"
]
print(list)