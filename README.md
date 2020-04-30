# Arpyino

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI version fury.io](https://badge.fury.io/py/arpyino.svg)](https://pypi.python.org/pypi/arpyino/)
[![PyPI license](https://img.shields.io/pypi/l/arpyino.svg)](https://pypi.python.org/pypi/arpyino/)
[![Only some bytes!](https://badge-size.herokuapp.com/divy-work/arpyino/master/arpyino/main.py)](https://github.com/divy-work/arpyino/blob/master/arpyino/main.py)

`pip install arpyino`

Arpyino is really tiny but saves your time. It basically reads the serial port of your Arduino board.

# Usage

## Basic Usage
```python
import arpyino
ard = arpyino.Arduino('/dev/ttyACM0', 9600)
while (1 == 1):
  print(ard.readAll())
```

## Configuring components
This is can be useful when you have more than one modules connected to your Arduino board.
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

MIT License
Copyright (c) 2018 Divy Srivastava
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


