class QueueState:
    CHOOSING_SERVICE = "choosing_service"
    WAITING_NAME = "waiting_name"
    CONFIRMING = "confirming"


def get_queue_position(entries, entry_id):
    waiting_entries = [
        entry for entry in entries
        if entry["status"] == "waiting"
    ]

    for position, entry in enumerate(waiting_entries, start=1):
        if entry["id"] == entry_id:
            return position

    return None
