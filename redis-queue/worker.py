import time
import hashlib
import requests


BACKEND_API = os.getenv('BACKEND_API', '')
api_url = '{}/api'.format(BACKEND_API)


def do_work(process_id):
    result = hashlib.md5(process_id)
    
    time.sleep(5)

    requests.post(
        f'{api_url}/work-done/{process_id}',
        headers={'Content-type': 'application/json'}
    )