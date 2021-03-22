from uuid import uuid4
from flask import Blueprint, request, current_app
from .db_models import ProcessModel
from .db import db


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/run-process', methods=['POST'])
def run_process():
    process_id = uuid4().hex

    process = ProcessModel(id=process_id)
    db.session.add(process)
    db.session.commit()

    current_app.task_queue.enqueue('worker.do_work', process_id)

    return process_id


@api.route('/work-done/<process_id>', methods=['POST'])
def work_done(process_id):
    process = ProcessModel.query.get(process_id)

    process.update(result=request.data)
    db.session.commit()

    # Do we want to communicate? WebSockets?
    return 'OK'
