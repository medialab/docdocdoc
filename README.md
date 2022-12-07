[![Build Status](https://github.com/medialab/docdocdoc/workflows/Tests/badge.svg)](https://github.com/medialab/docdocdoc/actions)

# Docdocdoc

A python library to template documentation from docstrings.

## Installation

You can install `docdocdoc` with pip with the following command:

```
pip install docdocdoc
```

## Usage

* [build](#build)
  * [build_fn](#build_fn)
  * [build_toc](#build_toc)
  * [build_docs](#build_docs)
  * [generate_readme](#generate_readme)
* [parts](#parts)
  * [assembling_description](#assembling_description)
  * [get_article](#get_article)
  * [get_function](#get_function)
  * [get_references](#get_references)
  * [template_params](#template_params)
  * [template_references](#template_references)
  * [template_return](#template_return)

---

### build

#### build_fn

Function returning the function or class documentation written in Markdown.

*Arguments*

* **fn** *str* - str of the function or class name".

*Returns*

*str* - function or class documentation written in Markdown.

#### build_toc

Function returning the table of content written in Markdown.

*Arguments*

* **data** *list* - list of dicts with the keys "title" and "fns". "title" contains the name of the section and "fns" contains the name of the functions in the section.

*Returns*

*str* - table of content written in Markdown.

#### build_docs

Function returning the documentation written in Markdown.

*Arguments*

* **data** *list* - list of dicts with the keys "title" and "fns". "title" contains the name of the section and "fns" contains the name of the functions in the section.

*Returns*

*StringIO* - documentation written in Markdown.

#### generate_readme

Function printing readme.

*Arguments*

* **data** *list* - list of dicts with the keys "title" and "fns". "title" contains the name of the section and "fns" contains the name of the fonctions in the section.

---

### parts

#### assembling_description

Function returning the short description of the docstring,
aggregated with the long description.

*Arguments*

* **docstring** *DocstringStyle.GOOGLE* - a google docstring.

*Returns*

*string* - description of the docstring.

#### get_article

Function returning the article if the docstring has one, None otherwise.

*Arguments*

* **docstring** *DocstringStyle.GOOGLE* - a google docstring.

*Returns*

*string* - string containing the description of the article.

#### get_function

Function returning a dict with the different part for a function (or class)
documentation (i.e. name, description, article.).

*Arguments*

* **fn** *function* - a function you defined.

*Returns*

*dict* - dict with the different part of the documentation.

#### get_references

Function returning the references if the docstring has some, None otherwise.

*Arguments*

* **docstring** *DocstringStyle.GOOGLE* - a google docstring.

*Returns*

*list* - list containing the strings with the references.

#### template_params

Function returning templated arguments.

*Arguments*

* **fn_doc** *dict* - a dict with the function documentation parts (returned by get_function).

*Returns*

*string* - templated arguments.

#### template_references

Function returning templated references.

*Arguments*

* **fn_doc** *dict* - a dict with the function documentation parts (returned by get_function).

*Returns*

*string* - templated references.

#### template_return

Function returning templated arguments.

*Arguments*

* **fn_doc** *dict* - a dict with the function documentation parts (returned by get_function).

*Returns*

*string* - templated returns.
