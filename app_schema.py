from pydantic import BaseModel
from typing import List


class IntentSchema(BaseModel):
    app_name: str
    features: List[str]


class SystemDesignSchema(BaseModel):
    entities: List[str]
    roles: List[str]


class AppConfigSchema(BaseModel):
    ui_pages: List[str]
    api_endpoints: List[str]
    database_tables: List[str]