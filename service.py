import repository


def get_log_by_trace_id(trace_id: str):
    logs = repository.get_log_by_trace_id(trace_id=trace_id)
    filtered_logs = []
    for log in logs:
        filtered_log = {
            "message": log.get("message"),
            "timestamp": log.get("timestamp"),
        }
        filtered_logs.append(filtered_log)
    return filtered_logs
