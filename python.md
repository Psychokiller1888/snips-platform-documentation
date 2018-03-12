# Handler code examples for your Snips assistant

When you have built an assistant on [https://snips.ai](https://snips.ai) by following [the tutorial](https://github.com/snipsco/snips-platform-documentation/wiki), you can write your own handler to act on the behalf of the user.

This repository contains a few examples in Python

## Install requirements

The main requirement of the handler is to watch the MQTT bus with the Hermes messages from the Snips AI.

All you need is a MQTT client:

```text
sudo apt-get install python python-pip
pip install paho-mqtt
```

You also need to have [setup your platform with the Snips assistant](https://github.com/snipsco/snips-platform-documentation/wiki/1.-Setup-the-Snips-Voice-Platform-on-your-Raspberry-Pi) and copied an assistant model \(you can use the [demo IoT assistant](https://github.com/snipsco/snips-platform-documentation/raw/master/resources/iot_assistant.zip)\) to `/opt/snips/config` on your device

## Display messages

The components of the AI are communicating and coordinating through a MQTT bus, a good way to understand what your on-device Snips assistant is doing is to look at the messages on the bus

```text
python display_messages/display_messages.py
-  hermes/hotword/detected:
-  hermes/hotword/wait:
-  hermes/asr/toggleOn:
-  hermes/audioServer/playFile: {"filePath":"/usr/share/snips/dialogue/sound/start_of_input.wav"}
-  hermes/asr/textCaptured: {"text":"turn the lights blue","likelihood":0.0034613716,"seconds":3462000.0}
-  hermes/asr/toggleOff:
-  hermes/audioServer/playFile: {"filePath":"/usr/share/snips/dialogue/sound/end_of_input.wav"}
-  hermes/nlu/query: {"text":"turn the lights blue","likelihood":0.0034613716,"seconds":3462000.0}
-  hermes/nlu/intentParsed: {"input":"turn the lights blue","intent":{"intentName":"ActivateLightColor","probability":0.9836065},"slots":[{"value":{"kind":"Custom","value":"blue"},"rawValue":"blue","range":{"start":16,"end":20},"entity":"objectColor","slotName":"objectColor"}]}
-  hermes/intent/ActivateLightColor: {"input":"turn the lights blue","intent":{"intentName":"ActivateLightColor","probability":0.9836065},"slots":[{"value":{"kind":"Custom","value":"blue"},"rawValue":"blue","range":{"start":16,"end":20},"entity":"objectColor","slotName":"objectColor"}]}
```

## IoT Assistant

This piece of code handle intents from the snips smart lights bundle from the console, it uses the TTS to tell when an intent was detected \(but doesn't actually turn on the lights\)

