import dash
from dash import html
from Data_Vis import app   # Import Dash app


def test_001_header_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal("h1", "Soul Foods Sales Visualiser", timeout=4)

    # 5. assert it is there
    assert dash_duo.find_element("h1").text == "Soul Foods Sales Visualiser", \
        "Header <h1> should display 'Soul Foods Sales Visualiser'"

    # 6. check no browser console errors
    assert dash_duo.get_logs() == [], "browser console should contain no error"


def test_002_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#sales-line-chart", timeout=4)

    assert dash_duo.find_element("#sales-line-chart") is not None, \
        "Graph with id='sales-line-chart' should be present"

    assert dash_duo.get_logs() == [], "browser console should contain no error"


def test_003_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#region-filter", timeout=4)
    assert dash_duo.find_element("#region-filter") is not None, \
        "RadioItems with id='region-filter' should be present"

    assert dash_duo.get_logs() == [], "browser console should contain no error"
