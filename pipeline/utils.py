import hashlib

def generate_hash(row):

    return hashlib.md5(
        str(row.values).encode()
    ).hexdigest()