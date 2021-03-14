from flask import Blueprint, request, jsonify, current_app


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/run-process', methods=['POST'])
def run_process():
  pass