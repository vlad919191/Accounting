storage_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 120},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "code": {"type": "string", "maxLength": 120},
        "storekeeper": {"type": "string", "minLength": 3, "maxLength": 120},
        "address": {"type": "string", "minLength": 3, "maxLength": 120}
      },
    "required": ["title", "code"]
}
