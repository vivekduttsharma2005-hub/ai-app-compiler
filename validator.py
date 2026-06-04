import json

REQUIRED_KEYS = [
    "ui_pages",
    "api_endpoints",
    "database_tables"
]


def validate_schema(schema_text):

    errors = []

    try:
        data = json.loads(schema_text)

    except Exception:
        return {
            "valid": False,
            "errors": ["Invalid JSON"]
        }

    for key in REQUIRED_KEYS:

        if key not in data:
            errors.append(f"Missing key: {key}")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }