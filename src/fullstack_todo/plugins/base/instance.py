from pydantic import BaseModel


class PluginInstance(BaseModel):
    title: str
    slug: str
