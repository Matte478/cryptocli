# cryptocli

 A simple commandline app for encrypt / decrypt files in Python 3.

## Installation
In the root directory of the CLI source code run installation bash script.

```bash
sh install.sh
```

## Usage

```bash
usage: cryptocli [-h] [-v] (-e | -d) -i  -o  -k

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   Display this application version
  -e, --encrypt   Encrypt mode
  -d, --decrypt   Decrypt mode
  -i, --input     Input file
  -o, --output    Output file
  -k, --key       Key file
```