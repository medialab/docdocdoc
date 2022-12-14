# =============================================================================
# Docdocdoc Build Unit Tests
# =============================================================================
from docdocdoc import build_docs, build_toc, build_fn


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
    return f"hello from {city}, {name}"


def hallo(name):
    """
    Function returning "hallo" followed by name.

    Args:
        name (string): string with the name you want to say hello to.
    Returns:
        string: "hello from" city, followed by name.
    """
    return f"hallo {name}"


def hola():
    """
    Function returning "hola".

    Note that it doesn't take any argument.

    Yields:
        string: "hola".
    """
    yield "hola"


class Person:
    """
    A class to represent a person.

    Args:
        name (str): first name of the person. Defaults to ("Jean", "Baptiste").
        surname (str): family name of the person.
        age (int): age of the person. Prefer using `months` as unit.
        opinion_on_cats_and_dogs (dict): whether the person likes cats and dogs. Defaults to {"cats": False, "dogs": True}.

    """

    def __init__(self, surname, age, name=("Jean", "Baptiste"), opinion_on_cats_and_dogs={"cats": False, "dogs": True}):

        self.name = name
        self.surname = surname
        self.age = age
        self.opinion_on_cats_and_dogs = opinion_on_cats_and_dogs


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

EXPECTED_FN = """\
#### Person

A class to represent a person.

*Arguments*

* **name** *str* `("Jean", "Baptiste")` - first name of the person.
* **surname** *str* - family name of the person.
* **age** *int* - age of the person. Prefer using `months` as unit.
* **opinion_on_cats_and_dogs** *dict* `{"cats": False, "dogs": True}` - whether the person likes cats and dogs.\
"""

EXPECTED_TOC = """\
* [first part](#first-part)
  * [hello](#hello)
  * [hallo](#hallo)
* [second part](#second-part)
  * [hola](#hola)\
"""

EXPECTED_DOC = """\

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


class TestBuildFn(object):
    def test_basics(self):

        assert build_fn(Person) == EXPECTED_FN


class TestBuildToc(object):
    def test_basics(self):

        assert build_toc(DOCS_TEST) == EXPECTED_TOC


class TestBuildDocs(object):
    def test_basics(self):
        assert build_docs(DOCS_TEST) == EXPECTED_DOC
