from typing import Iterator, List

from fullstack_todo.plugins.base.instance import PluginInstance


class PluginExists(Exception):
    pass


class PluginDoesNotExists(Exception):
    pass


class NotValidPlugin(Exception):
    pass


class PluginManager:
    def __init__(self) -> None:
        self.plugins: List[PluginInstance] = []

    def __len__(self) -> int:
        return len(self.plugins)

    def __iter__(self) -> Iterator[PluginInstance]:
        return iter(self.plugins)

    def all(self) -> List[PluginInstance]:
        return self.plugins

    def exists(self, plugin: PluginInstance) -> bool:
        for _plugin in self.plugins:
            if plugin.slug == _plugin.slug:
                return True
        return False

    def get(self, slug: str) -> PluginInstance:
        for plugin in self.plugins:
            if plugin.slug == slug:
                return plugin
        raise PluginDoesNotExists

    def register(self, plugin: PluginInstance) -> PluginInstance:
        if not issubclass(type(plugin), PluginInstance):
            raise NotValidPlugin
        if self.exists(plugin=plugin):
            raise PluginExists
        self.plugins.append(plugin)
        return plugin

    def unregister(self, plugin: PluginInstance) -> PluginInstance:
        if not issubclass(type(plugin), PluginInstance):
            raise NotValidPlugin
        for _plugin in self.plugins:
            if plugin.slug == _plugin.slug:
                self.plugins.remove(_plugin)
                return _plugin
        raise PluginDoesNotExists
