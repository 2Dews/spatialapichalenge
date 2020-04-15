import awsgi

import spatial_api.spatial_web_api

app = spatial_api.spatial_web_api.app

def lambda_handler(event, context):
    return awsgi.response(app, event, context)