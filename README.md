# Snips-WolframAlpha
A *german* knowledge app for Snips.ai that uses `WolframAlpha` and `Google Translate`.

### Getting Started

These instructions will give you an advice how to setup the app on your snips running device. 

### Prerequisites

You need [Snips](https://snips.gitbook.io/documentation/snips-basics) already configured and running on your device. 

You also need [SAM](https://snips.gitbook.io/getting-started/installation) as a command line interface to set up and connected your device and your account.

### Installing

1. In the German [app store](https://console.snips.ai/) add the
[app](https://console.snips.ai/app-editor/bundle_AdmAbpqQ2nE7) `WolframAlpha` to your *german* assistant.

2. Before you install the app make sure that you copy your `Google Cloud Account (GCA) file` into `/sys/...`.
      ```bash
      cp your_gca_file.json /sys/your_gca_file.json
      ```

   Make sure that all required file permissions are set:
      ```bash
      sam install assistant
      ```
	  
3. If you already have the same assistant on your platform, update it with:
      ```bash
      sam update-assistant
      ```
      
   Otherwise install the assistant on your platform with the following command:
      ```bash
      sam install assistant
      ```
	  
4. During installation you will get asked for your `WolframAlpha API key` and the path of your `GCA file`

5. You can debug potential errors with `sam service log` and `snips-skill-server`
	
## Usage

With this app you can ask Snips several questions.

### Example sentences

* *Wo steht der Eiffelturm*
* *Wo wurde Albert Einstein geboren*
* *Woran starb Marie Curie*
* *Wofür steht CDU*
* *Wofür steht die Abkürzung HTML*
* *Wie groß ist der Mount Everest*
* *Wie tief ist der Bodensee*
* *Wieweit weit ist es von Paris nach Berlin*
* *Wieviel Sterne hat die Amerikanische Flagge*
* *Wieviel ergibt 24 mal 50*
* *Wann wurde Leonardo Da Vinci geboren*
* *Wann wurde Norwegen unabhängig*
* *Was bedeutet Apartheid*
* *Was ist die Wurzel aus 100*
* *Was ist ein Säugetier*
* *Welches Formelzeichen hat Silber*
* *Welches ist das höchste Gebäude der Welt*
* *Welchen Aggregatzustand hat Wasser*
* *Welchen Wert hat Gold*
* *Welcher Tag ist heut*
* *Welcher Stern ist der Erde am nähesten*
* *Welche Dichte hat Eisen*
* *Welche Farbe hat die italienische Flagge*
* *Wer war der erste Mensch auf dem Mond*
* *Wer erfand den Wechselstrom*
* [...]

## Contribution

Please report errors and bugs by
opening a [new issue](https://github.com/RumoOr/Snips-Neustart/issues/new).
You can also write other ideas for this skill. Thank you for your contribution.

## Thanks To

[MrJohnZoidberg](https://github.com/MrJohnZoidberg) for his bunch of snips app examples 