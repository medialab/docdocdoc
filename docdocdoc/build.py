
# =============================================================================
# Build documentation Function
# =============================================================================
#
# Functions to build the library documentation
#
from io import StringIO
from functools import partial

from docdocdoc.parts import (
    get_function,
    template_params,
    template_references,
    template_return
)


def build_toc(data):
    """
    Function returning the table of content written in Markdown.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the fonctions in the section.
    Returns:
        str: table of content written in Markdown.
    """

    lines = []

    for item in data:
        lines.append(
            "* [%s](#%s)" % (item["title"], item["title"].lower().replace(" ", "-"))
        )

        for fn in item["fns"]:
            name = fn.__name__

            lines.append("  * [%s](#%s)" % (name, name.lower()))

    return "\n".join(lines)


def build_docs(data):
    """
    Function returning the documentation written in Markdown.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the fonctions in the section.
    Returns:
        StringIO: documentation written in Markdown.
    """

    f = StringIO()

    p = partial(print, file=f)

    for item in data:
        p()
        p("---")
        p()
        p("### %s" % item["title"])

        for fn in item["fns"]:
            fn_doc = get_function(fn)

            p()
            p("#### %s" % fn_doc["name"])
            p()
            p(fn_doc["description"])

            if fn_doc["article"] is not None:
                p()
                p("*Article*")
                p("> " + fn_doc["article"])

            if fn_doc["references"]:
                p()
                p("*References*")
                p()
                p(template_references(fn_doc))

            for example in fn_doc["examples"]:
                p()
                p("```python")
                p(example.description)
                p("```")

            p()
            p("*Arguments*")
            p()
            p(template_params(fn_doc))

            if fn_doc["returns"]:
                p()
                p("*Yields*" if fn_doc["returns"].is_generator else "*Returns*")
                p()
                p(template_return(fn_doc))

    result = f.getvalue()
    f.close()

    return result


def generate_readme(data):
    """
    Function printing readme.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the fonctions in the section.
    """

    with open("./README.template.md") as f:
        TEMPLATE = f.read()

    readme = TEMPLATE.format(toc=build_toc(data), docs=build_docs(data)).rstrip()

    print(readme)
