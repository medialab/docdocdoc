# =============================================================================
# Docdocdoc Parts Unit Tests
# =============================================================================
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
    return "hello from {city}, {name}"


class TestTemplates(object):
    def test_basics(self):

        fn = get_function(hello)

        assert template_references(fn) == "- https://www.pnas.org/content/pnas/106/16/6483.full.pdf\n- https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network"

        assert template_params(fn) == "* **name** *str* - string with the name you want to say hello to.\n* **city** *str* - string with the city you want to say hello from."

        assert template_return(fn) == "*str* - \"hello from\" city, followed by name."
