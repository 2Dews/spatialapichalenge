from flask import (
    Flask,
    jsonify,
    request,
)

import source.spatial_library

app = Flask(__name__)

@app.route('/serverstatus')
def server_status():
    return jsonify(status=200, message='ok')


@app.route('/geometry/intersection', methods=['POST'])
def geometry_intersection():
    requstJson = request.get_json()

    doesIntersect = source.spatial_library.does_intersect(requstJson['geometry_a'], requstJson['geometry_a'])

    response = {'status': 'ok'}

    return jsonify(response)
