from flask import Blueprint, request, jsonify, make_response, Response
from bson.json_util import dumps

upload_route = Blueprint('upload_route', __name__)


@upload_route.route("/upload", methods=['POST'])
def upload():
    if 'file' not in request.files:
        return make_response(jsonify(status=False,
                                     message="please provide a file with name 'file'",
                                     data=None
                                     ), 400)
    from src.module.random import id_generator
    file = request.files['file']
    name = file.filename
    extension = name.split(".")[-1]
    random = id_generator(4) + '-' + id_generator(8)
    path = random + "." + extension
    try:
        from src.module.upload import upload
        # uploaded = file.save(path)
        uploaded = upload(file, path)
        print("UPLOADDED: ",uploaded)
        # try:
        #     from src.database.connection import collection
        #     collection.insert_one({
        #         "_user": str(request.headers['X-USER']['_id']),
        #         "file": str(uploaded)
        #     })
        # except Exception as e:
        #     print(e)
        #     return make_response(jsonify(status=False,
        #                                  message="error",
        #                                  data=None
        #                                  ), 500)
    except Exception as e:
        print(e)
        return make_response(jsonify(status=False,
                                     message='error',
                                     data=None
                                     ), 500)

    return make_response(jsonify(status=True,
                                 message="file uploaded",
                                 data="https://s3.us-east-2.amazonaws.com/cutz2u/upload/"+uploaded
                                 ), 200)


@upload_route.route("/show", methods=['GET'])
def show():
    try:
        from src.database.connection import collection
        files = collection.find({})
        return make_response(Response(
            dumps(list(files)),
            mimetype='application/json'
        ), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify(status=False,
                                     message="error",
                                     data=None
                                     ), 500)
