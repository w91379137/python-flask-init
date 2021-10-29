
from flask_mqtt import Mqtt # type: ignore

# https://ithelp.ithome.com.tw/articles/10198250

class MQTTManager:

    mqtt: None 

    def __init__(self, server, mqtt_config):

        server.config['MQTT_BROKER_URL'] = mqtt_config['MQTT_BROKER_URL']
        server.config['MQTT_BROKER_PORT'] = mqtt_config['MQTT_BROKER_PORT']
        # server.config['MQTT_REFRESH_TIME'] = 1.0  

        mqtt = Mqtt(server)
        self.mqtt = mqtt

        @mqtt.on_connect()
        def on_connect(client, userdata, flags, rc):
            print('mqtt on_connect')

        @mqtt.on_message()
        def on_message(client, userdata, message):
            topic = message.topic,
            payload = message.payload.decode()
            print(f'mqtt on_message: {topic}: {payload}')


    def subscribe(self, topic):
        print(f'mqtt subscribe: {topic}')
        self.mqtt.subscribe(topic)

    def publish(self, topic, msg):
        print(f'mqtt publish: {topic}: {msg}')
        self.mqtt.publish(topic, msg)