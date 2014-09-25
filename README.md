# SAKURA Internet API Client Library for Python

This library gives you an easy interface to control your resources on
[SAKURA Cloud](https://secure.sakura.ad.jp/cloud/).


## Table of Contents

* [Requirements](#requirements)
* [How to use this library in your project](#how-to-use-this-library-in-your-project)
* [Copyright and license](#copyright-and-license)


## Requirements

- Python 3


## How to use this library in your project

Just copy the **saklient** directory into your project.
```python
from saklient.cloud.api import API

api = API.authorize(token, secret, zone)
# ZONE: "is1a" (Ishikari 1st zone), "is1b" (Ishikari 2nd zone), "tk1v" (Sandbox)
# "tk1v" is recommended for tests

# ...
```


## Copyright and license

Copyright (C) 2014 SAKURA Internet, Inc.

This library is freely redistributable under [MIT license](http://www.opensource.org/licenses/mit-license.php).

