import strawberry

def to_dict(query):
    return {field: value for field, value in query.__dict__.items() if value is not strawberry.UNSET}