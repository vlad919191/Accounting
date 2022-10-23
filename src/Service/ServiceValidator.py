service_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "string", "maxLength": 120},
        "title": {"type": "string", "maxLength": 120},
        "check": {"type": "string", "maxLength": 120},
        "wholesale_price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "retail_price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "unit_id": {"type": "number"}
      },
    "required": ["code", "title"]
}
