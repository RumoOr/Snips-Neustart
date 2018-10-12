# Snips-Neustart
A german restart app for Snips.ai

### Getting Started

These instructions will give you an advice how to setup the app on your snips running device. 

### Prerequisites

You need [Snips](https://snips.gitbook.io/documentation/snips-basics) already configured and running on your device. 

You also need [SAM](https://snips.gitbook.io/getting-started/installation) as a command line interface to set up and connected your device and your account.

### Installing

1. In the German [app store](https://console.snips.ai/) add the
[app](https://console.snips.ai/app-editor/bundle_AdmAbpqQ2nE7) `Neustart` to your *German* assistant.

2. If you already have the same assistant on your platform, update it with:
      ```bash
      sam update-assistant
      ```
      
   Otherwise install the assistant on your platform with the following command:
      ```bash
      sam install assistant
      ```
	  
3. You can debug potential errors with:
      ```bash
      sam service log
      ```
   Or
      ```bash
      snips-skill-server
      ```	
	
## Usage

With this app you can order Snips to reboot your system.

### Example sentences

* *Neustart*
* *Bitte neustarten*
* *Starte jetzt neu*
* *Mach jetzt einen Neustart*
* [...]

## Contribution

Please report errors and bugs by
opening a [new issue](https://github.com/RumoOr/Snips-Neustart/issues/new).
You can also write other ideas for this skill. Thank you for your contribution.

## Thanks To

[MrJohnZoidberg](https://github.com/MrJohnZoidberg) for his bunch of snips app examples 