create_auth_restore_schema = {
    "type": "object",
    "properties": {
        "email_address": {"type": "string", "minLength": 5, "maxLength": 120},
      },
    "required": ["email_address"]
}

auth_restore_schema = {
    "type": "object",
    "properties": {
        "ticket": {"type": "string", "minLength": 1, "maxLength": 180},
        "password": {"type": "string", "minLength": 6, "maxLength": 24}
      },
    "required": ["ticket", "password"]
}