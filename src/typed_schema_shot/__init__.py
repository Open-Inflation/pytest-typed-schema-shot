"""
pytest-typed-schema-shot
========================

Плагин для pytest, который автоматически генерирует JSON Schema
на основе примеров данных и проверяет соответствие данных сохраненным схемам.
"""

from .core import SchemaShot

__version__ = "0.1.9"
__all__ = ["SchemaShot"]

# Публичное API
assert_match = SchemaShot.assert_match
