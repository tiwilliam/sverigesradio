# Python bindings for Sveriges Radio API

Tested with Python version 2.5, 2.6, 2.7, 3.2 and 3.3.

## Installation

You can easily install sverigesradio from PyPi.

```bash
pip install sverigesradio
```

## Issues and Contribution

Bug reports are done by [creating an issue on Github](https://github.com/tiwilliam/sverigesradio/issues). If you want to contribute you can always [create a pull request](https://github.com/tiwilliam/sverigesradio/pulls) for discussion and code submission.

## Getting Started

SverigesRadio provides a simple interface for retrieving channels, programs, songs and more from Sveriges Radio's public API.

```python
>>> from sverigesradio import SverigesRadio

>>> SverigesRadio.channels()
[Channel(P1), Channel(P2), Channel(P3), Channel(P4 Blekinge), Channel(P4 Dalarna), Channel(P4 Gotland), Channel(P4 Gävleborg), Channel(P4 Göteborg), Channel(P4 Halland), Channel(P4 Jämtland), Channel(P4 Jönköping), Channel(P4 Kalmar), Channel(P4 Kristianstad), Channel(P4 Kronoberg), Channel(P4 Malmöhus), Channel(P4 Norrbotten), Channel(P4 Sjuhärad), Channel(P4 Skaraborg), Channel(P4 Stockholm), Channel(P4 Sörmland), Channel(P4 Uppland), Channel(P4 Värmland), Channel(P4 Väst), Channel(P4 Västerbotten), Channel(P4 Västernorrland), Channel(P4 Västmanland), Channel(P4 Örebro), Channel(P4 Östergötland), Channel(SR Sápmi), Channel(SR Sisuradio), Channel(P6), Channel(Din gata), Channel(Metropol), Channel(P2), Channel(P3 Star), Channel(Radioapans knattekanal), Channel(P4 Radiosporten), Channel(P2 Klassiskt), Channel(Minnen), Channel(P2 Världen), Channel(SR Extra01), Channel(SR Extra02), Channel(SR Extra03), Channel(SR Extra04), Channel(SR Extra05), Channel(SR Extra06), Channel(SR Extra07), Channel(SR Extra08), Channel(SR Extra09), Channel(SR Extra10), Channel(P2 Klassisk Jul), Channel(P4 Bjällerklang)]

>>> p3 = SverigesRadio.channel(164)
>>> p3.song.now
Song(Mat Zo & Porter Robinson - Easy)

>>> p3.program.now
Episode(Musikguiden i P3)

>>> p3.program.next
Episode(Ekonyheter)
```
