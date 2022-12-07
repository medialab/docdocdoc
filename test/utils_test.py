# =============================================================================
# Docdocdoc Utils Unit Tests
# =============================================================================
from docdocdoc import collapse, clean_line_break, clean_multiple


STRING_TO_COLLAPSE = """graph (nx.AnyGraph or ig.AnyGraph): networkx or igraph graph instance
to explore."""

STRING_LINE_BREAK = """This is a line.



An other paragraph.




A new paragraph."""

STRING_NO_LINE_BREAK = """This is a line.

An other paragraph.

A new paragraph."""

STRING_MULTIPLE = "This  is a sentence !!"

STRING_MULTIPLE_NO_CHANGE = """\

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

EXPECTED_STRING_TO_COLLAPSE = """graph (nx.AnyGraph or ig.AnyGraph): networkx or igraph graph instance to explore."""

EXPECTED_STRING_LINE_BREAK = """This is a line.

An other paragraph.

A new paragraph."""

EXPECTED_MULTIPLE = "This is a sentence !"


class TestUtils(object):
    def test_collpase(self):
        assert collapse(STRING_TO_COLLAPSE) == EXPECTED_STRING_TO_COLLAPSE

    def test_clean_line_break(self):
        assert clean_line_break(STRING_LINE_BREAK) == EXPECTED_STRING_LINE_BREAK

        assert clean_line_break(STRING_NO_LINE_BREAK) == EXPECTED_STRING_LINE_BREAK

        assert clean_line_break(STRING_TO_COLLAPSE) == STRING_TO_COLLAPSE

    def test_clean_multiple(self):
        assert clean_multiple(STRING_MULTIPLE) == EXPECTED_MULTIPLE

        assert clean_multiple(STRING_MULTIPLE_NO_CHANGE) == STRING_MULTIPLE_NO_CHANGE
