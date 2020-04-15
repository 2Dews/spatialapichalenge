import pytest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from spatial_api import app

@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_server_status(client):
    response = client.get('serverstatus')
    assert b'ok' in response.data


def test_geometry_intersect(client):

    testData = {
        'geometry_a': {"type": "Polygon", "coordinates": [[[-11648991.3615983, 4921487.3851758], [-11648463.8373444, 4921488.17577299], [-11648467.7337492, 4922020.46492316], [-11648994.3243665, 4922018.95145425], [-11648991.3615983, 4921487.3851758]]]}, 
        'geometry_b': {"type": "Polygon", "coordinates": [[[-11648991.3615983, 4921487.3851758], [-11648463.8373444, 4921488.17577299], [-11648467.7337492, 4922020.46492316], [-11648994.3243665, 4922018.95145425], [-11648991.3615983, 4921487.3851758]]]}
    }

    response = client.post('/geometry/intersection', json=testData, follow_redirects=True)
    assert b'ok' in response.data