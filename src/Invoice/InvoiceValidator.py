invoice_schema = {
    "type": "object",
    "properties": {
        "date": {"type": "string", "maxLength": 80},
        "document_number": {"type": "string", "maxLength": 80},
        "buyer_account": {"type": "string", "maxLength": 80},
        "bar_code": {"type": "string",  "maxLength": 180},
        "contract": {"type": "string", "maxLength": 80},
        "contact_date": {"type": "string", "maxLength": 80},
        "prepaid_account": {"type": "string", "maxLength": 80},

        "aah_account": {"type": "string", "maxLength": 80},
        "out_type": {"type": "string", "maxLength": 80},

        "series_and_number": {"type": "string", "maxLength": 120},
        "out_date": {"type": "string", "maxLength": 80},
        "description": {"type": "string", "maxLength": 120},

        "type": {"type": "string", "maxLength": 80},

        "storage_id": {"type": "number"},

        "title": {"type": "string", "maxLength": 80},
        "unit_id": {"type": "number"},
        "count": {"type": "number"},
        "price": {"type": "number"},

        "provider_id": {"type": "number"},
        "buyer_id": {"type": "number"},
      },
    "required": ["title"]
}
