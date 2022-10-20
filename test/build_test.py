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


EXPECTED_TOC = "\
* [first part](#first-part)\n\
  * [hello](#hello)\n\
  * [hallo](#hallo)\n\
* [second part](#second-part)\n\
  * [hola](#hola)"

EXPECTED_DOC = "\n---\n\n\
### first part\n\n\
#### hello\n\n\
Function returning a string \"hello from\" city, followed by name.\n\n\
*Article*\n\
> Some ref here (2022).\n\n\
*References*\n\n\
- https://www.pnas.org/content/pnas/106/16/6483.full.pdf\n\
- https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network\n\n\
*Arguments*\n\n\
* **name** *str* - string with the name you want to say hello to.\n\
* **city** *str* - string with the city you want to say hello from.\n\n\
*Returns*\n\n\
*str* - \"hello from\" city, followed by name.\n\n\
#### hallo\n\n\
Function returning \"hallo\" followed by name.\n\n\
*Arguments*\n\n\
* **name** *string* - string with the name you want to say hello to.\n\n\
*Returns*\n\n\
*string* - \"hello from\" city, followed by name.\n\n\
---\n\n\
### second part\n\n\
#### hola\n\n\
Function returning \"hola\".\n\
Note that it doesn't take any argument.\n\n\
*Arguments*\n\n\n\n\
*Yields*\n\n\
*string* - \"hola\".\n"


class TestBuildToc(object):
    def test_basics(self):

        assert build_toc(DOCS_TEST) == EXPECTED_TOC


class TestBuildDocs(object):
    def test_basics(self):
        assert build_docs(DOCS_TEST) == EXPECTED_DOC
