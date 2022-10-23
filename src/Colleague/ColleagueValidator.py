colleague_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 1, "maxLength": 80},
        "code": {"type": "string", "maxLength": 80},
        "activity_address": {"type": "string", "minLength": 1, "maxLength": 80},
        "legal_address": {"type": "string", "minLength": 1, "maxLength": 80},
        "phone_number": {"type": "number"},
        "hvhh": {"type": "number"},
        "account_number": {"type": "string", "maxLength": 80},
      },
    "required": ["title"]
}
