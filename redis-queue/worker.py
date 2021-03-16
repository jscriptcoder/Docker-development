import os
import time
import hashlib
import requests


BACKEND_API = os.getenv('BACKEND_API', '')
api_url = f'{BACKEND_API}/api'


def do_work(process_id):
    # Start: work that takes very long time
    encoded_process_id = process_id.encode('utf-8')
    hash_object = hashlib.md5(encoded_process_id)
    result = hash_object.hexdigest()
    time.sleep(5)
    # End

    requests.post(f'{api_url}/work-done/{process_id}', data=result)