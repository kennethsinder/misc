import json
import os

_values = {}
_loaded = False


def _load():
    # Copy .env.example to .env and replace with real values
    global _values, _loaded
    config_filepath = os.path.join(os.path.dirname(__file__), 'env.json')
    with open(config_filepath) as config_file:
        _values = json.load(config_file)
        _loaded = True


def get_value(key, default=None):
    if not _loaded:
        _load()
    return _values.get(key, default)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
