import awsgi

import source.spatial_web_api

app = source.spatial_web_api.app


def lambda_handler(event, context):
    return awsgi.response(app, event, context)