invoice_name_list_schema = {
    "type": "object",
    "properties": {
        "invoice_type_id": {"type": "number"},
        "storage_id": {"type": "number"},
        "unit_id": {"type": "number"},
        "count": {"type": "number"},
        "price": {"type": "number", "minimum": 0, "maximum": 99999999},
        "aah": {"type": "boolean"},
        "expense_account": {"type": "string", "maxLength": 180},
        "income_account": {"type": "string", "maxLength": 180},
        "batch": {"type": "string", "maxLength": 80},
      },
    "required": []
}
