import time
import hashlib
import requests


BACKEND_API = os.getenv('BACKEND_API', '')
api_url = f'{BACKEND_API}/api'


def do_work(process_id):
    # Start: work that takes very long time
    result = hashlib.md5(process_id)
    time.sleep(5)
    # End

    requests.post(f'{api_url}/work-done/{process_id}', data=result)