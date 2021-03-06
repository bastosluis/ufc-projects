VALID_OP = ['r', 'w', 'c']

READ_LOCK = 0
WRITE_LOCK = 1
UPDATE_LOCK = 2
READ_INTENTIONAL = 3
WRITE_INTENTIONAL = 4
UPDATE_INTENTIONAL = 5
CERTIFY_LOCK = 6


STATUS_UNDEFINED = 0
STATUS_GRANTED = 1
STATUS_CONVERTING = 2
STATUS_WAITING = 3
STATUS_ABORTED = 4


VERTEX_NOT_SEEN = 0
VERTEX_CURRENT = 1
VERTEX_DONE = 2

def lock_to_string(lock_type):
    if READ_LOCK:
        return 'RL'
    elif WRITE_LOCK:
        return 'WL'
    elif CERTIFY_LOCK:
        return 'CL'