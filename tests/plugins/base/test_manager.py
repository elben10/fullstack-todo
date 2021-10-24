import pytest

from fullstack_todo.plugins.base.instance import PluginInstance
from fullstack_todo.plugins.base.manager import (
    NotValidPlugin,
    PluginDoesNotExists,
    PluginExists,
    PluginManager,
)


def test_register_plugin() -> None:
    manager = PluginManager()
    plugin = PluginInstance(title="test", slug="test")
    assert plugin == manager.register(plugin)
    assert len(manager) == 1


def test_register_non_valid_instance() -> None:
    manager = PluginManager()
    plugin = 1
    with pytest.raises(NotValidPlugin):
        manager.register(plugin)  # type: ignore


def test_double_register_plugin() -> None:
    manager = PluginManager()
    plugin1 = PluginInstance(title="test", slug="slug")
    plugin2 = PluginInstance(title="test", slug="slug")

    manager.register(plugin1)

    with pytest.raises(PluginExists):
        manager.register(plugin2)


def test_unregister_plugin() -> None:
    manager = PluginManager()
    plugin = PluginInstance(title="test", slug="slug")
    manager.register(plugin)

    assert plugin == manager.unregister(plugin)
    assert len(manager) == 0


def test_unregister_non_valud_instance() -> None:
    manager = PluginManager()
    plugin = 1
    with pytest.raises(NotValidPlugin):
        manager.unregister(plugin)  # type: ignore


def test_unregister_plugin_not_present() -> None:
    manager = PluginManager()
    plugin = PluginInstance(title="test", slug="slug")
    with pytest.raises(PluginDoesNotExists):
        manager.unregister(plugin)


def test_iterating_over_plugings() -> None:
    manager = PluginManager()
    plugin1 = PluginInstance(title="test", slug="test")
    plugin2 = PluginInstance(title="test2", slug="test2")

    manager.register(plugin1)
    manager.register(plugin2)

    iterator = iter(manager)
    assert next(iterator) == plugin1
    assert next(iterator) == plugin2


def test_get_all_plugins() -> None:
    manager = PluginManager()
    plugin1 = PluginInstance(title="test", slug="test")
    plugin2 = PluginInstance(title="test2", slug="test2")

    manager.register(plugin1)
    manager.register(plugin2)

    assert manager.all() == [plugin1, plugin2]


def test_plugin_exists() -> None:
    manager = PluginManager()
    plugin1 = PluginInstance(title="test", slug="test")
    manager.register(plugin1)

    assert manager.exists(plugin1)


def test_get_plugin_by_slug() -> None:
    manager = PluginManager()
    plugin1 = PluginInstance(title="Title", slug="title")
    manager.register(plugin1)

    assert plugin1 == manager.get(slug=plugin1.slug)


def test_get_plugin_raises_exception_if_not_present() -> None:
    manager = PluginManager()

    with pytest.raises(PluginDoesNotExists):
        manager.get("title")
