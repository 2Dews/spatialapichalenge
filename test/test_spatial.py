import pytest
import json
import shapely.geometry
import shapely.wkt

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import source.spatial_library

testdata = [
    ('POLYGON((-11648991.3615983 4921487.3851758,-11648463.8373444 4921488.17577299,-11648467.7337492 4922020.46492316,-11648994.3243665 4922018.95145425,-11648991.3615983 4921487.3851758))', 
    'POLYGON((-11649516.863177 4920955.76313538,-11648988.4018356 4920955.83532279,-11648459.937266 4920955.91145567,-11648463.8373444 4921488.17577299,-11648991.3615983 4921487.3851758,-11648994.3243665 4922018.95145425,-11649520.9117556 4922017.40948747,-11649518.8890804 4921486.56988166,-11649516.863177 4920955.76313538))', 
    True),
    ('POLYGON((-11648991.3615983 4921487.3851758,-11648463.8373444 4921488.17577299,-11648467.7337492 4922020.46492316,-11648994.3243665 4922018.95145425,-11648991.3615983 4921487.3851758))', 
    'POLYGON((-11648991.3615983 4921487.3851758,-11648463.8373444 4921488.17577299,-11648467.7337492 4922020.46492316,-11648994.3243665 4922018.95145425,-11648991.3615983 4921487.3851758))', 
    True),
    ('POLYGON((-11648991.3615983 4921487.3851758,-11648463.8373444 4921488.17577299,-11648467.7337492 4922020.46492316,-11648994.3243665 4922018.95145425,-11648991.3615983 4921487.3851758))', 
    'POLYGON((-11650045.1912689 4920430.02704007,-11650045.4576565 4920955.69094797,-11650574.0549189 4920955.61466896,-11650573.8843774 4920430.86811007,-11650045.1912689 4920430.02704007))', 
    False)
]

@pytest.mark.parametrize("polyA,polyB,expected", testdata)
def test_valid_geojson_polygons_intersect(polyA, polyB, expected):

    polyAJson = json.dumps(shapely.geometry.mapping(shapely.wkt.loads(polyA)))
    polyBJson = json.dumps(shapely.geometry.mapping(shapely.wkt.loads(polyB)))

    intersects = source.spatial_library.does_intersect(polyAJson, polyBJson)
    assert intersects == expected


@pytest.mark.parametrize("polyA,polyB,expected", testdata)
def test_valid_wkt_polygons_intersect(polyA, polyB, expected):
    intersects = source.spatial_library.does_intersect(polyA, polyB)
    assert intersects == expected


def test_invalid_string_polygon_intersection():
    with pytest.raises(Exception, match=r'.*Could not create geometry object from string.*'):
        source.spatial_library.does_intersect('*', r'{}')
