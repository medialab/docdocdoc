# =============================================================================
# Docdocdoc Build Unit Tests
# =============================================================================
from docdocdoc import build_docs, build_toc


def hello(name, city):
    """
    Function returning a string "hello from" city, followed by name.

    Article:
        Some ref here (2022).
    References:
        paper: https://www.pnas.org/content/pnas/106/16/6483.full.pdf
        wikipedia: https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network
    Args:
        name (str): string with the name you want to say hello to.
        city (str): string with the city you want to say hello from.
    Returns:
        str: "hello from" city, followed by name.
    """
    return "hello from {city}, {name}"


def hallo(name):
    """
    Function returning "hallo" followed by name.

    Args:
        name (string): string with the name you want to say hello to.
    Returns:
        string: "hello from" city, followed by name.
    """
    return "hallo {name}"


def hola():
    """
    Function returning "hola".

    Note that it doesn't take any argument.

    Yields:
        string: "hola".
    """
    yield "hola"


DOCS_TEST = [
    {
        "title": "first part",
        "fns": [
            hello,
            hallo,
        ]
    },
    {
        "title": "second part",
        "fns": [
            hola,
        ]
    }
]


EXPECTED_TOC = """* [first part](#first-part)
  * [hello](#hello)
  * [hallo](#hallo)
* [second part](#second-part)
  * [hola](#hola)"""

EXPECTED_DOC = """
---

### first part

#### hello

Function returning a string \"hello from\" city, followed by name.

*Article*
> Some ref here (2022).

*References*

- https://www.pnas.org/content/pnas/106/16/6483.full.pdf
- https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network

*Arguments*

* **name** *str* - string with the name you want to say hello to.
* **city** *str* - string with the city you want to say hello from.

*Returns*

*str* - \"hello from\" city, followed by name.

#### hallo

Function returning \"hallo\" followed by name.

*Arguments*

* **name** *string* - string with the name you want to say hello to.

*Returns*

*string* - \"hello from\" city, followed by name.

---

### second part

#### hola

Function returning \"hola\".
Note that it doesn't take any argument.

*Arguments*



*Yields*

*string* - \"hola\".
"""


class TestBuildToc(object):
    def test_basics(self):

        assert build_toc(DOCS_TEST) == EXPECTED_TOC


class TestBuildDocs(object):
    def test_basics(self):
        assert build_docs(DOCS_TEST) == EXPECTED_DOC
