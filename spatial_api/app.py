import awsgi

from flask import (
    Flask,
    jsonify,
    request,
)
from shapely import (
    geometry,
    wkt
)
import json
import geojson
import shapely

def geometry_string_to_geometry(geometry_string):
    """
    Creates a shapely geometry object from a geojson or wkt string.
    """
    try:
        if geojson.loads(json.dumps(geometry_string)).is_valid:
            return geometry.shape(geometry_string)
    except:
        print("Input is not valid json.")

    try: 
        wktGeometry = wkt.loads(geometry_string)
        return wktGeometry
    except:
        raise Exception('Could not create geometry object from string: {0}'.format(geometry_string))


def does_intersect(geometry_string_a, geometry_string_b):
    """
    Returns true when polygon_a spatially intersects polygon_b.
    """   
    geometry_a = geometry_string_to_geometry(geometry_string_a)
    geometry_b = geometry_string_to_geometry(geometry_string_b)

    #TODO try and check that the geometries have same spatial reference.

    return geometry_a.intersects(geometry_b)

app = Flask(__name__)

@app.route('/serverstatus')
def server_status():
    return jsonify(status=200, message='ok')


@app.route('/geometry/intersection', methods=['POST'])
def geometry_intersection():
    """
    Checks two geometries for intersection. 
    Geometries can be geojson or wkt strings. 
    """
    requstJson = request.get_json()

    doesIntersect = does_intersect(requstJson['geometry_a'], requstJson['geometry_a'])

    response = {'status': 'ok',
                'intersects': doesIntersect
    }

    return jsonify(response)

def lambda_handler(event, context):
    return awsgi.response(app, event, context)