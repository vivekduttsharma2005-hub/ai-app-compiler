import json


def repair_schema(schema_text, validation_result):

    try:
        data = json.loads(schema_text)

    except Exception:
        data = {}

    for error in validation_result["errors"]:

        if "ui_pages" in error:
            data["ui_pages"] = []

        if "api_endpoints" in error:
            data["api_endpoints"] = []

        if "database_tables" in error:
            data["database_tables"] = []

    return json.dumps(data, indent=2)