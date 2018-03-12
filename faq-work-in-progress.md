# FAQ \(work in progress\)

#### What do I need to run the Snips Voice Platform?

These are the current minimal requirements to install and run the Snips Voice Platform:

* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) and power supply \(see [starter kit](https://www.adafruit.com/product/3334)\)
* an SD card \(at least 4Gb, 8Gb recommended\) with [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/) installed. [How to install?](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md)
* a USB microphone \(see [recommended](https://www.adafruit.com/product/3367)\)
* optional: a speaker \(see recommended [USB](https://www.adafruit.com/products/3369) or [3.5mm-jack](https://www.sparkfun.com/products/14023)\) or headphone if you want to use the dialog features, where you need to hear questions from the assistant
* you may also want to have a USB keyboard, USB mouse, and a monitor with an HDMI cable, to easily setup your Raspberry.

More platforms are coming, send a mail to [contact@snips.ai](mailto:contact@snips.ai) if you are impatient!

#### Known issues

If your on-device assistant is not working and you somewhere in the logs you see this:

```text
ERROR:snips_queries: missing field name at line 291 column 1
```

please try to re-train your assistant online and download it again.

#### What is Privacy by Design?

Privacy by Design is an approach to systems engineering which takes privacy into account throughout the whole engineering process. This principle will be mandatory for every company offering a product or service to a European citizen after May 2018.

#### How does it differ from other voice providers, such as Amazon Alexa or Google API.ai?

Cloud providers' Automatic Speech Recognition \(ASR\) and Natural Language Understanding \(NLU\) run in the cloud: if you power your assistant with Amazon Alexa or Google API.ai, your voice will be sent to the cloud. This means it cannot be Private by Design, it cannot run offline, and it will cost you every time someone uses your product. Snips, on the other hand, runs completely on your device, with nothing being sent to the cloud. This means it guarantees your Privacy, works offline and doesn't have variable costs! Last but not least, Snips' on-device performances are [significantly better](https://medium.com/@alicecoucke/benchmarking-natural-language-understanding-systems-google-facebook-microsoft-and-snips-2b8ddcf9fb19) than every major cloud provider.

#### Is it possible to contribute to the platform?

Today, the best way to help us is to provide feedback. Join our community on [Slack](https://snipslabs.herokuapp.com/), or contact us by email on [support@snips.ai](mailto:support@snips.ai). Stay tuned though, because we will soon open source the platform!

#### Is Snips free?

Snips is completely free for makers and for building prototypes. For commercial use \(products you sell\), we charge fixed fees per device, for unlimited queries. You can learn more on our [enterprise page](https://snips.ai/enterprise).

#### Is Snips open-source?

Snips will be open source soon! In the meantime, we already opened a lot of things, which you can find on our Github account [here](https://github.com/snipsco). Follow our [Medium](http://medium.com/snips-ai) and our newsletter to stay updated!

#### Which languages are supported?

Snips' NLU understands English, French, Spanish, German and Korean. As for the ASR, it currently understands English and French, but more languages will be added soon! If you need ASR in another language than English, we provide an integration with [Google's Cloud Speech service](https://cloud.google.com/speech).

#### Can I customize the hotword for my assistant?

At the moment, custom hotword is a feature provided as part of our enterprise package. We realize that it’s an important requirement for all our users and we are working on a public feature that should be available by the end of 2017.

#### Can I use Snips to build conversational chatbots?

You can use our NLU independently from the other components, and run it on your own servers. However, the main purpose of Snips Voice Platform is to power physical devices, such as speakers, TVs, cars, etc..



