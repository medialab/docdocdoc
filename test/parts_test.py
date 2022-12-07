# =============================================================================
# Docdocdoc Parts Unit Tests
# =============================================================================
from pytest import raises
from textwrap import dedent

from docdocdoc import (
    get_function,
    template_params,
    template_references,
    template_return
)


def hello(name, city):
    """
    Function returning a string "hello from" city, followed by name.

    Article:
        Some ref here       (2022).
    References:
        paper: https://www.pnas.org/content/pnas/106/16/6483.full.pdf
        wikipedia: https://en.wikipedia.org/wiki/Disparity_filter_algorithm_of_weighted_network
    Args:
        name (str): string with the name you want to say hello to.
        city (str): string with the city you want to say hello from.
    Returns:
        str: "hello from" city,,, followed by name.
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


class Sigma(object):
    """
    A Jupyter widget using sigma.js and graphology to render interactive
    networks directly within the result of a notebook cell.
    Args:
        graph (nx.AnyGraph or ig.AnyGraph): networkx or igraph graph instance
            to explore.
        name (str, optional): name of the graph. Defaults to None.
        height (int, optional): height of the widget container in pixels.
            Defaults to 500.
        start_layout (bool or float, optional): whether to automatically start
            the layout algorithm when mounting the widget. If a number is given
            instead, the layout algorithm will start and automatically stop
            after this many seconds. Defaults to False.
        node_metrics (Iterable or Mapping, optional): node metrics to be
            computed by graphology by the widget's JavaScript code. Currently
            only supports "louvain" for community detection.
            Defaults to None.
        layout_settings (dict, optional): settings for the ForceAtlas2 layout
            (listed here: https://graphology.github.io/standard-library/layout-forceatlas2#settings)
            Defaults to None.
        clickable_edges (bool, optional): whether to allow user to click on edges
            to display their information. This can have a performance cost on
            larger graphs. Defaults to False.
        process_gexf_viz (bool, optional): whether to process gexf files viz
            data for node & edges. Defaults to True.
        max_categorical_colors (int, optional): max number of colors to be
            generated for a categorical palette. Categories, ordered by
            frequency, over this maximum will use the default color.
            Defaults to 10.
        hide_info_panel (bool, optional): whether to hide the information panel
            to the right of the widget. Defaults to False.
        hide_search (bool, optional): whether to hide the search bar to the
            right of the widget. Defaults to False.
        hide_edges_on_move (bool, optional): whether to hide the edges when the
            graph is being moved. This can be useful to improve performance
            when the graph is too large. Defaults to False.
        sync_key (str, optional): Key used by the widget to synchronize events
            between multiple instances of views of a same graph. Prefer using
            `SigmaGrid` when able, it will handle this advanced aspect of the
            widget for you.
        sync_targets (Iterable, optional): Names of targets to synchronize
            through the `sync_key` kwarg. Targets include "layout", "camera",
            "selection" and "hover". Defaults to ("layout", "camera", "selection", "hover").
        camera_state (dict, optional): Initial state for the widget's camera (which can be
            retrieved using the `#.get_camera_state` method).
            Defaults to {"x": 0.5, "y": 0.5, "ratio": 1, "angle": 0}.
        selected_node (str or int, optional): Key of the initially selected node in
            the widget (can be retrieved using the `#.get_selected_node` method).
            Defaults to None.
        selected_edge (tuple, optional): (source, target) tuple of the initially
            selected edge in the widget (can be retrieved using the
            `#.get_selected_edge` method).
            Defaults to None.
        selected_node_category_values (Iterable, optional): list of selected node category
            values (can be retrieved using the `#.get_selected_node_category_values` method).
            Defaults to None.
        selected_edge_category_values (Iterable, optional): list of selected edge category
            values (can be retrieved using the `#.get_selected_edge_category_values` method).
            Defaults to None.
        label_font (str, optional): font to be used with labels. Defaults to "sans-serif".
        label_density (int, optional): number of labels to display per grid cell for
            default camera zoom. Defaults to 1.
        label_grid_cell_size (int, optional): size in pixels of a square cell in the label
            selection grid. Defaults to 250.
        label_rendered_size_threshold (int, optional): minimum actual rendered size
            (after camera zoom operations) a node must have on screen for its label to
            be allowed to be displayed. If None, the threshold will be inferred based
            on the maximum node size of your graph.
            Defaults to None.
        show_all_labels (bool, optional): macro setting making sure most, if not all, labels
            get displayed on screen. Might have an impact on performance with larger graphs.
            Defaults to False.
        layout (Mapping, optional): node positions, expressed as a mapping of nodes to a {x, y}
            dict. Defaults to None.
        node_color (VariableData, optional): data to be used as categorical or continuous node
            color. Defaults to None.
        raw_node_color (RawVariableData, optional): raw data (colors) to be used for nodes.
            Defaults to "color".
        node_color_gradient (Iterable or str, optional): gradient of colors to map to, for instance:
            (["yellow", "red"]), or name of a d3 continuous color scale (found here:
            https://github.com/d3/d3-scale-chromatic#readme), for instance: "Viridis".
            If given, node color will be interpreted as continuous rather than categorical.
            Defaults to None.
        node_color_scale (Iterable or str, optional): ...
        node_color_palette (Mapping or str, optional): ...
        default_node_color (str, optional): ...
    """


EXPECTED_SIGMA = """\
* **graph** *nx.AnyGraph or ig.AnyGraph* - networkx or igraph graph instance to explore.
* **name** *str, optional* `None` - name of the graph.
* **height** *int, optional* `500` - height of the widget container in pixels.
* **start_layout** *bool or float, optional* `False` - whether to automatically start the layout algorithm when mounting the widget. If a number is given instead, the layout algorithm will start and automatically stop after this many seconds.
* **node_metrics** *Iterable or Mapping, optional* `None` - node metrics to be computed by graphology by the widget's JavaScript code. Currently only supports "louvain" for community detection.
* **layout_settings** *dict, optional* `None` - settings for the ForceAtlas2 layout (listed here: https://graphology.github.io/standard-library/layout-forceatlas2#settings.
* **clickable_edges** *bool, optional* `False` - whether to allow user to click on edges to display their information. This can have a performance cost on larger graphs.
* **process_gexf_viz** *bool, optional* `True` - whether to process gexf files viz data for node & edges.
* **max_categorical_colors** *int, optional* `10` - max number of colors to be generated for a categorical palette. Categories, ordered by frequency, over this maximum will use the default color.
* **hide_info_panel** *bool, optional* `False` - whether to hide the information panel to the right of the widget.
* **hide_search** *bool, optional* `False` - whether to hide the search bar to the right of the widget.
* **hide_edges_on_move** *bool, optional* `False` - whether to hide the edges when the graph is being moved. This can be useful to improve performance when the graph is too large.
* **sync_key** *str, optional* - Key used by the widget to synchronize events between multiple instances of views of a same graph. Prefer using `SigmaGrid` when able, it will handle this advanced aspect of the widget for you.
* **sync_targets** *Iterable, optional* `("layout", "camera", "selection", "hover")` - Names of targets to synchronize through the `sync_key` kwarg. Targets include "layout", "camera", "selection" and "hover".
* **camera_state** *dict, optional* `{"x": 0.5, "y": 0.5, "ratio": 1, "angle": 0}` - Initial state for the widget's camera (which can be retrieved using the `#.get_camera_state` method).
* **selected_node** *str or int, optional* `None` - Key of the initially selected node in the widget (can be retrieved using the `#.get_selected_node` method).
* **selected_edge** *tuple, optional* `None` - (source, target) tuple of the initially selected edge in the widget (can be retrieved using the `#.get_selected_edge` method).
* **selected_node_category_values** *Iterable, optional* `None` - list of selected node category values (can be retrieved using the `#.get_selected_node_category_values` method).
* **selected_edge_category_values** *Iterable, optional* `None` - list of selected edge category values (can be retrieved using the `#.get_selected_edge_category_values` method).
* **label_font** *str, optional* `"sans-serif"` - font to be used with labels.
* **label_density** *int, optional* `1` - number of labels to display per grid cell for default camera zoom.
* **label_grid_cell_size** *int, optional* `250` - size in pixels of a square cell in the label selection grid.
* **label_rendered_size_threshold** *int, optional* `None` - minimum actual rendered size (after camera zoom operations) a node must have on screen for its label to be allowed to be displayed. If None, the threshold will be inferred based on the maximum node size of your graph.
* **show_all_labels** *bool, optional* `False` - macro setting making sure most, if not all, labels get displayed on screen. Might have an impact on performance with larger graphs.
* **layout** *Mapping, optional* `None` - node positions, expressed as a mapping of nodes to a {x, y} dict.
* **node_color** *VariableData, optional* `None` - data to be used as categorical or continuous node color.
* **raw_node_color** *RawVariableData, optional* `"color"` - raw data (colors) to be used for nodes.
* **node_color_gradient** *Iterable or str, optional* `None` - gradient of colors to map to, for instance: (["yellow", "red"]), or name of a d3 continuous color scale (found here: https://github.com/d3/d3-scale-chromatic#readme), for instance: "Viridis". If given, node color will be interpreted as continuous rather than categorical.
* **node_color_scale** *Iterable or str, optional* - .
* **node_color_palette** *Mapping or str, optional* - .
* **default_node_color** *str, optional* - .\
"""


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

        my_class = get_function(Sigma)

        assert template_params(my_class) == EXPECTED_SIGMA
