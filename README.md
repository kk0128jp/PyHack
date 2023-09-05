# PyHack

## Description

HackTools in Python

Tool List

- Dos
  - SynFlood
- BindShell
- ReverseShell
- Spoofing
  - Email
  
## Requirement

- Python 3.11.0

## Install

``` bash
pip install scapy pyyaml keyboard pyinstaller
```

## Usage

``` bash
usage: 使い方

説明

positional arguments:
  {synflood,bs-connect,rs-connect,spoof-mail}
    synflood            see `synflood -h`
    bs-connect          see `bs-connect -h`
    rs-connect          see `rs-connect -h`
    spoof-mail          see `spoof-mail -h`

options:
  -h, --help            show this help message and exit
```

### setting

``` bash
git clone https://github.com/kk0128jp/PyHack.git
cd ./PyHack
cp example_setting.yaml setting.yaml
vi setting.yaml
```

### Dos

waiting update

### BindShell

waiting update

### ReverseShell

1. Edit rs_target.py SERVER_HOST and SERVER_PORT
2. Convert python file to exe file

``` bash
vi rs_target.py
pyinstaller "python file" --onefile --noconsole
```

### KeyRogger

waiting update

### Spoofing

waiting update

## Note

## Auther

- kk0128jp

## License
