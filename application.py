from flask import Flask, request, jsonify, make_response
import os
from dotenv import load_dotenv
from json import loads
from src.route.upload import upload_route
from flask_cors import CORS

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

app = Flask(__name__)
CORS(app)

#
# @app.before_request
# def check_headers():
#     print(request.headers)
#     if 'X-USER' not in request.headers:
#         response = make_response(jsonify(status=False,
#                                          message="unauthorized",
#                                          data=None), 401)
#         return response
#     else:
#         try:
#             user = loads(request.headers['X-USER'])
#             if '_id' not in user:
#                 return make_response(jsonify(status=False,
#                                              message="forbidden",
#                                              data=None), 403)
#         except Exception as e:
#             print(e)
#             return make_response(jsonify(status=False,
#                                          message="forbidden",
#                                          data=None), 403)


app.register_blueprint(upload_route)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST"),
        port=os.environ.get("PORT"),
        debug=True if (os.environ.get("DEBUG") == 'on') else False
    )
