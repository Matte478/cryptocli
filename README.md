# cryptocli

 A simple commandline app for encrypt / decrypt files in Python 3.

## Installation
In the root directory of the CLI source code run installation bash script.

```bash
sudo sh install.sh
```

## Prerequisites
 * python _>= 3.8_
 * pip

## Usage

```bash
usage: cryptocli [-h] [-v] {symmetric-mode,hybrid-mode,generate-key} ...

positional arguments:
  {symmetric-mode,hybrid-mode,generate-key}
    symmetric-mode      symmetric mode for encryption / decryption
    hybrid-mode         hybrid mode for encryption / decryption
    generate-key        generate key pair (public and private) for hybrid mode

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Display this application version
```

## License
MIT © [dave.](https://davedot.dev)