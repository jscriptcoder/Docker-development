from uuid import uuid4
from flask import Blueprint, request, jsonify, current_app


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/run-process', methods=['POST'])
def run_process():
  process_id = uuid4().hex

  # Send to RQ

  return process_id