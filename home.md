# Home

![Snips Voice Platform](https://camo.githubusercontent.com/49ba9a98bff75e6dc20a9cc4e2f85c77ac5279e4/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6765742e646f63732e736e6970732e61692f7374617469632f696d616765732f77696b692f736e6970735f62616e6e65725f70726f642e706e67)

The **Snips Voice Platform** allows anyone to integrate AI powered voice interaction in their devices with ease. The end-to-end pipeline - Hotword detection, Automatic Speech Recognition \(ASR\) and Natural Language Understanding \(NLU\) - runs fully on device, powered by state of the art deep learning. By using Snips, you can avoid cloud provider costs, cloud latency, and protect user's privacy.

#### Snips console

Your voice assistant in English, French, German, Spanish or Korean \(more to come\) can be configured easily via a [web console](https://console.snips.ai/). You can select pre-built capabilities, called _bundles_, or create completely custom ones. For optimal performances, we provide you with a [unique set of tools](https://github.com/snipsco/snips-platform-documentation/wiki/4.-Aim-for-quality): automatic data generation, assistant metrics, etc. Once your assistant is ready, you can download it directly from the web console. The downloaded assistant archive will be used to setup the on-device platform.

#### Snips platform

On device, the Snips platform takes an audio stream as input, detects when a user pronounces a pre-defined wake word \(a.k.a. hotword\), transcribes the subsequent query, and analyses it to extract the user intention \(his/her _intent_\), along with the corresponding parameters of the query \(the _slots_\). These are then exposed to your code, so you can implement the response to the user query. A [dialog system](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions) is provided to keep a fine control on dialog sessions, allowing multi-turn and multi-room scenarios.

Each component is a process \(from the system perspective\) communicating through a standard MQTT software bus \(see [http://mqtt.org](http://mqtt.org/)\). Hermes is the protocol on top of MQTT that defines the coordination and communication between the components of the platform, as well as between the platform and your code. Each component subscribes to events on the bus, and publishes events based on their results, that are taken over by other components, and so on.

Today, the following setups are supported:

* Linux \(Debian, Raspbian\)
* Android
* iOS

More platforms will be added in the coming months. If you are interested in a platform that is not supported, contact us at [contact@snips.ai](mailto:contact@snips.ai).

#### Moving on to the next step

Sounds clear to you? You can now head to the next part of this documentation, [learning how to create your first assistant from an existing bundle](https://github.com/snipsco/snips-platform-documentation/wiki/2.-Create-an-assistant-using-an-existing-bundle)  


