import json
import geojson
import shapely

def geometry_string_to_geometry(geometry_string):
    """
    Creates a shapely geometry object from a geojson or wkt string.
    """
    try:
        jsonObj = json.loads(geometry_string)
        if geojson.loads(geometry_string).is_valid:
            return shapely.geometry.shape(jsonObj)
    except:
        print("Input is not valid json.")

    try: 
        wktGeometry = shapely.wkt.loads(geometry_string)
        return wktGeometry
    except:
        raise Exception('Could not create geometry object from string: {0}'.format(geometry_string))


def does_intersect(geometry_string_a, geometry_string_b):
    """
    Returns true when polygon_a spatially intersects polygon_b.
    """   
    geometry_a = geometry_string_to_geometry(geometry_string_a)
    geometry_b = geometry_string_to_geometry(geometry_string_b)

    #TODO Checks that the polygons have same spatial reference.

    return geometry_a.intersects(geometry_b)
    
