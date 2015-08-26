# SAKURA Internet API Client Library for Python

This library gives you an easy interface to control your resources on
[SAKURA Cloud](https://secure.sakura.ad.jp/cloud/).


## Table of Contents

* [Requirements](#requirements)
* [How to use this library in your project](#how-to-use-this-library-in-your-project)
* [Examples](#examples)
* [Copyright and license](#copyright-and-license)


## Requirements

- Python 2.7 or 3.4


## How to use this library in your project

```bash
# Install the package
pip install saklient

# Edit your code
cd YOUR/PROJECT/ROOT
vim YOUR-CODE.py
```

```python
from saklient.cloud.api import API

api = API.authorize(token, secret, zone)
# ZONE: "is1a" (Ishikari 1st zone), "is1b" (Ishikari 2nd zone), "tk1v" (Sandbox)
# "tk1v" is recommended for tests

# ...
```


## Examples

Code examples are available [here](http://sakura-internet.github.io/saklient.doc/).


## Copyright and license

Copyright (C) 2014-2015 SAKURA Internet, Inc.

This library is freely redistributable under [MIT license](http://www.opensource.org/licenses/mit-license.php).

- Special thanks to ABEJA.INC for supporting Python 2

