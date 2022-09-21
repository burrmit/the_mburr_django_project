# test_views.py
"""
This is the test_views.py that will run all test for the views program.
"""

def test_index_ok(client):
    """
    Test that a 200 response code is received when requesting '/'
    """
    response = client.get('/')
    assert response.status_code == 200
