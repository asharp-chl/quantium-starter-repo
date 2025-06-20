import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app():

    app_module = import_app('dash_app_upgraded')
    return app_module.app

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    # Check for the main header h1 text
    header = dash_duo.find_element("header h1")
    assert header is not None
    assert 'Pink Morsel Sales Dashboard' in header.text

def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)
    # Check the presence of the dcc.Graph with id 'sales-line-chart'
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    # Check for the RadioItems container (id = region-selector)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None
