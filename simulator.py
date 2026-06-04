import json


def simulate_execution(schema_text):

    try:
        data = json.loads(schema_text)

    except Exception:

        return {
            "success": False,
            "message": "Execution failed"
        }

    return {
        "success": True,
        "message": (
            f"Generated "
            f"{len(data.get('ui_pages', []))} pages, "
            f"{len(data.get('api_endpoints', []))} APIs, "
            f"{len(data.get('database_tables', []))} tables"
        )
    }