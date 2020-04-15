import awsgi
from flask import (
    Flask,
    jsonify,
    request,
)

from spatial_api import spatial_library

app = Flask(__name__)

@app.route('/serverstatus')
def server_status():
    return jsonify(status=200, message='ok')


@app.route('/geometry/intersection', methods=['POST'])
def geometry_intersection():
    requstJson = request.get_json()

    doesIntersect = spatial_library.does_intersect(requstJson['geometry_a'], requstJson['geometry_a'])

    response = {'status': 'ok'}

    return jsonify(response)

def lambda_handler(event, context):
    return awsgi.response(app, event, context)