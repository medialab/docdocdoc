# =============================================================================
# Docdocdoc Parts Unit Tests
# =============================================================================
from pytest import raises
from textwrap import dedent

from docdocdoc import get_function, template_params, template_references, template_return


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


class TestTemplates(object):
    def test_basics(self):

        with raises(TypeError):
            get_function("bonjour")

        fn = get_function(hello)

        assert template_references(fn) == dedent(
            """\
                - https://www.pnas.org/content/pnas/106/16/6483.full.pdf
                - https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network
            """
        ).rstrip()

        assert template_params(fn) == dedent(
            """\
                * **name** *str* - string with the name you want to say hello to.
                * **city** *str* - string with the city you want to say hello from.
            """
        ).rstrip()

        assert template_return(fn) == "*str* - \"hello from\" city, followed by name."

    def test_class(self):

        my_class = get_function(Person)

        assert template_params(my_class) == dedent(
            """\
                * **name** *str* `("Jean", "Baptiste")` - first name of the person.
                * **surname** *str* - family name of the person.
                * **age** *int* - age of the person. Prefer using `months` as unit.
                * **opinion_on_cats_and_dogs** *dict* `{"cats": False, "dogs": True}` - whether the person likes cats and dogs.
            """
        ).rstrip()
