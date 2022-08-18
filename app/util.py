from datetime import datetime

def to_datetime(string: str, format: str = None):

    if not string:
        return None
    
    result = datetime.strptime(string, format)

    return result