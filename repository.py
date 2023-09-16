import requests
import json
import constants


def get_log_by_trace_id(trace_id: str):
    payload = json.dumps(
        {
            "queryType": "log",
            "filter": f'message contains "[{trace_id}]"',
        }
    )
    headers = {
        "Authorization": f"Bearer {constants.SCALYR_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.request(
        "POST", constants.SCALYR_URL, headers=headers, data=payload
    )

    return response.json().get("matches")
