firm_provision_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "maxLength": 80},
        "email_address": {"type": "string", "maxLength": 80},
        "activity_address": {"type": "string", "maxLength": 80},
        "legal_address": {"type": "string", "maxLength": 80},
        "phone_number": {"type": "number"},

        "hvhh": {"type": "string", "maxLength": 120},
        "chapter_registration_number": {"type": "number"},
        "tax_area_code": {"type": "number"},
        "insurer_account_number": {"type": "number"},
        "shiper_registration_book_number": {"type": "string", "maxLength": 120},
      },
    "required": []
}