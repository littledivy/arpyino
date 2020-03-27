# Arpyino

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI version fury.io](https://badge.fury.io/py/arpyino.svg)](https://pypi.python.org/pypi/arpyino/)
[![PyPI license](https://img.shields.io/pypi/l/arpyino.svg)](https://pypi.python.org/pypi/arpyino/)
[![Only some bytes!](https://badge-size.herokuapp.com/divy-work/arpyino/master/arpyino/main.py)](https://github.com/divy-work/arpyino/blob/master/arpyino/main.py)

`pip install arpyino`
Arpyino is a really tiny but saves your time. It basically reads the serial port of your Arduino board.

# Usage

## Basic Usage
```python
import arpyino
ard = arpyino.Arduino('/dev/ttyACM0', 9600)
while (1 == 1):
  print(ard.readAll())
```

## Configuring components
This is can be useful when you have more than one moudules connected to your Arduino board.
```python
import arpyino
ard = arpyino.Arduino('/dev/ttyACM0', 9600)
# the `:servo:` here is the prefix that you will send along with the data from your Arduino
ard.configure('ultrasonic', ':ultrasonic:')
while(1 == 1):
  print(ard.read('ultrasonic'))
```
### Installation

It's quite obvious:
`pip install arpyino`

### License

