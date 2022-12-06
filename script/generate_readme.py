from docdocdoc.build import build_fn, build_toc, build_docs, generate_readme
from docdocdoc.parts import (
    assembling_description,
    get_article,
    get_function,
    get_references,
    template_params,
    template_references,
    template_return,
)

DOCS = [
    {
        "title": "build",
        "fns": [
            build_fn,
            build_toc,
            build_docs,
            generate_readme,
        ]
    },
    {
        "title": "parts",
        "fns": [
            assembling_description,
            get_article,
            get_function,
            get_references,
            template_params,
            template_references,
            template_return,
        ]
    }
]

generate_readme(DOCS)