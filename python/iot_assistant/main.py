import paho.mqtt.client as mqtt
import json

# MQTT client to connect to the bus
mqtt_client = mqtt.Client()


# Subscribe to the important messages
def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe('hermes/intent/lightsTurnOnSet')
    mqtt_client.subscribe('hermes/intent/lightsTurnOff')
    mqtt_client.subscribe('hermes/intent/lightsTurnUp')
    mqtt_client.subscribe('hermes/intent/lightsTurnDown')


# Process a message as it arrives
def on_message(client, userdata, msg):
    if msg.topic == 'hermes/intent/lightsTurnOnSet':
        action = "on"
    elif msg.topic == 'hermes/intent/lightsTurnOff':
        action = "off"
    elif msg.topic == 'hermes/intent/lightsTurnUp':
        action = "up"
    elif msg.topic == 'hermes/intent/lightsTurnDown':
        action = "down"
    slots = parse_slots(msg)
    session_id = parse_session_id(msg)
    if 'house_room' not in slots:
        say(session_id, "I don't know where I should turn {} the lights".format(action))
    else:
        room = slots['house_room']
        say(session_id, 'Turning {} the lights in the {}'.format(action, room))


def parse_slots(msg):
    '''
    We extract the slots as a dict
    '''
    data = json.loads(msg.payload)
    return dict((slot['slotName'], slot['rawValue']) for slot in data['slots'])


def parse_session_id(msg): 
    '''
    Extract the session id from the message
    '''
    data = json.loads(msg.payload)
    return data['sessionId']

def say(session_id, text):
    '''
    Print the output to the console and to the TTS engine
    '''
    print(text)
    mqtt_client.publish('hermes/dialogueManager/endSession', json.dumps({'text': text, "sessionId" : session_id}))

if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect('localhost', 1883)
    mqtt_client.loop_forever()
