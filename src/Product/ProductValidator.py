product_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 120},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "product_type_id": {"type": "number"},
        "storage_id": {"type": "number"},
        "code": {"type": "string", "minLength": 1, "maxLength": 120},
        "wholesale_price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "self_price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "retail_price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "unit_id": {"type": "number"},
        "count": {"type": "number", "minimum": 0, "maximum": 99999999}
      },
    "required": ["name", "product_type_id", "storage_id", "wholesale_price", "retail_price", "unit_id", "count"]
}

product_sale_schema = {
    "type": "object",
    "properties": {
        "colleague_id": {"type": "number"},
        "income_type_id": {"type": "number"},
        "count": {"type": "number", "minimum": 0, "maximum": 99999999},
        "price": {"type": "number"}
      },
    "required": ["colleague_id", "count", "price", "income_type_id"]
}
