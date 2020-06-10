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

Natch enables, but is not limited to, pattern matching in function headers with single or multi arities, by supporting linear or nested lookups including logical expressions; can be expanded by writing custom rule classes.


**Conditional function headers:**

````python
@natch.lt(0)
def f(x):
  return f(x * -1)


@natch.gte(0)
def f(x):
  return x + 1

>>> f(-1)
>>> 2

````


See more [examples](https://natch.readthedocs.io/en/latest/guide/examples.html).


### [Installing](#installing)
<a name="installing"></a>

Natch can be installed and updated using [pip](https://pip.pypa.io/en/stable/quickstart/).

```bash
$ pip install -U natch
```


### [Troubleshooting](#troubleshooting)
<a name="troubleshooting"></a>


- #### [RecursionError](#troubleshooting--recursion-error)
<a name="troubleshooting--recursion-error"></a>

> Python has a platform-dependent recursion limit. If your software requires too many nested function calls, it is recommended to avoid using recursive functions.
> 
> If you still need to follow recursive approach, you may need to [set recursion limit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit) as necessary.
