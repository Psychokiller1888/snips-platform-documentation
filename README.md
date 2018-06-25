# THIS IS A DEPRECATED DOCUMENTATION OF THE SNIPS PLATFORM KEPT ONLY FOR REFERENCE AND HISTORY. THE NEW DOCUMENTATION CAN BE FOUND ON GITBOOK: [SNIPS DOUCMENTATION](https://www.gitbook.com/@snips/spaces)




# Snips Voice Platform Documentation

![Snips Voice Platform](https://s3.amazonaws.com/get.docs.snips.ai/static/images/wiki/snips_banner_prod.png)

## About the Platform

The Snips Voice Platform allows anyone to integrate AI powered voice interaction in their devices with ease. The end-to-end pipeline - Hotword detection, Automatic Speech Recognition \(ASR\) and Natural Language Understanding \(NLU\) - runs fully on device, powered by state of the art deep learning. By using Snips, you can avoid cloud provider costs, cloud latency, and protect user's privacy.

Your voice assistant in English and French \(more to come\) can be configured easily via a web console. You can select pre-built assistants, or create completely custom ones. Today, the assistant can be deployed to a Raspberry Pi 3 and Android running on ARM hardware. More platforms are available for enterprise clients, contact us at contact@snips.ai.

## Getting Started

You will find everything you need in the [wiki](https://github.com/snipsco/snips-platform-documentation/wiki). You can get started with the [overview](https://github.com/snipsco/snips-platform-documentation/wiki), or alternatively, navigate the doc from here:

1. [Overview](https://github.com/snipsco/snips-platform-documentation/wiki)
   * [Snips console](https://github.com/snihttps://github.com/snipsco/snips-platform-documentation/wiki#snips-platform)
   * [Snips platform](https://github.com/snipsco/snips-platform-documentation/wiki#building-your-assistant-via-the-console)
2. [Setup the Snips Voice Platform](https://github.com/snipsco/snips-platform-documentation/wiki/1.-Setup-the-Snips-Voice-Platform)
   * [1. Snips Platform for Raspberry Pi 3 with Raspbian Stretch](https://github.com/snipsco/snips-platform-documentation/wiki/1.-Setup-the-Snips-Voice-Platform#1-snips-platform-for-raspberry-pi-3-with-raspbian-stretch)
   * [2. Snips Platform Installation on Debian/amd64](https://github.com/snipsco/snips-platform-documentation/wiki/1.-Setup-the-Snips-Voice-Platform#2-snips-platform-installation-on-debianamd64)
   * [3. Adding Voice Capability to an Android Application](https://github.com/snipsco/snips-platform-documentation/wiki/1.-Setup-the-Snips-Voice-Platform#3-adding-voice-capability-to-an-android-application)
3. [Create an assistant using an existing bundle](https://github.com/snipsco/snips-platform-documentation/wiki/2.-Create-an-assistant-using-an-existing-bundle)
4. [Create your own bundle](https://github.com/snipsco/snips-platform-documentation/wiki/3.-Create-your-own-bundle)
5. [Aim for quality](https://github.com/snipsco/snips-platform-documentation/wiki/4.-Aim-for-quality)
   * [Quality indicators](https://github.com/snipsco/snips-platform-documentation/wiki/4.-Aim-for-quality#quality-indicators)
   * [Built-in slot types](https://github.com/snipsco/snips-platform-documentation/wiki/4.-Aim-for-quality#built-in-slot-types)
   * [Entity extension](https://github.com/snipsco/snips-platform-documentation/wiki/4.-Aim-for-quality#entity-extension)
6. [Build rich interactions](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions)
   * [Sessions](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions#sessions)
   * [Multi-turn dialog](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions#multi-turn-dialog)
   * [Multi-room dialog](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions#multi-room-dialog)
   * [Triggering interactions with your user](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions#triggering-interactions-with-your-user)
   * [Messages reference](https://github.com/snipsco/snips-platform-documentation/wiki/5.-Build-rich-interactions#messages-reference)
7. [Miscellaneous](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous)
   * [Platform Configuration](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous#platform-configuration)
   * [Hermes Protocol](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous#hermes-protocol)
   * [Logs](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous#logs)
   * [Using Docker](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous#using-docker)
   * [Using External MQTT Broker](https://github.com/snipsco/snips-platform-documentation/wiki/6.--Miscellaneous#using-external-mqtt-broker)
8. [Key Concepts](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts)
   * [Hotword Detection](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#1-hotword-detection)
   * [Automatic Speech Recognition](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#2-automatic-speech-recognition)
     * [Snips ASR  \(English, with French and more coming soon\)](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#snips-asr)
     * [Using Google’s Cloud service for other languages](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#using-googles-cloud-service-for-other-languages)
   * [Natural Language Understanding](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#3-natural-language-understanding)
     * [Bundle](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#bundle)
     * [Intent](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#intent)
     * [Slot](https://github.com/snipsco/snips-platform-documentation/wiki/7.-Key-Concepts#slot)

[Contact us](https://github.com/snipsco/snips-platform-documentation/wiki/Contact-us)

[FAQ](https://github.com/snipsco/snips-platform-documentation/wiki/FAQ)

## About this repository code

You'll also find here sample code for handlers both in python and node. We strongly advise to get started with the [wiki](https://github.com/snipsco/snips-platform-documentation/wiki), that will route you to these samples at the right time.

