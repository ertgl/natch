### [Natch](#)

Pattern matching library.

[![PyPI Version](https://img.shields.io/pypi/v/natch?style=flat-square)](https://pypi.org/project/natch/)
[![Docs](https://img.shields.io/badge/API-docs-blue.svg?style=flat-square)](https://natch.readthedocs.io)
[![Status](https://img.shields.io/circleci/build/github/ertgl/natch?style=flat-square&logo=circleci)](https://circleci.com/gh/ertgl/natch)
[![GitHub](https://img.shields.io/badge/vcs-GitHub-blue.svg?style=flat-square&logo=github)](https://github.com/ertgl/natch)
[![MIT License](https://img.shields.io/pypi/l/natch?style=flat-square&color=blue)](LICENSE.txt)

---


### [Overview](#overview)
<a name="overview"></a>


**Conditional function headers:**

````text
Mathematical definition:

x < 0 => f(x) = f(x * -1)
x >= 0 => f(x) = x + 1
````

````python
# Natch:

@natch.lt(0)
def f(x):
  return f(x * -1)


@natch.gte(0)
def f(x):
  return x + 1
````


See more [examples](https://natch.readthedocs.io/en/latest/guide/examples.html).


### [Installing](#installing)
<a name="installing"></a>

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/).

```bash
$ pip install -U natch
```
