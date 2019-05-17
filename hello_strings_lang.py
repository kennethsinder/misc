#!/usr/bin/env python

# Followed tutorial from https://thatjdanisso.cool/programming-languages/
# but applied it to Python instead of JS!

import unittest


def lookup(env, name):
    return env[name]


def extend_env(env, name, value):
    new_env = dict(env)
    new_env[name] = value
    return new_env


def evaluate(node, env=None):
    if env is None:
        env = {}

    def eq(s): return node['type'] == s

    if eq('Variable'):
        return lookup(env, node['name'])
    elif eq('String'):
        return node['content']
    elif eq('Excite'):
        return '{}!'.format(evaluate(node['expression'], env))
    elif eq('Append'):
        return '{}{}'.format(
            evaluate(node['first'], env),
            evaluate(node['second'], env),
        )
    elif eq('Let'):
        name = node['name']
        value = evaluate(node['value'], env)
        new_env = extend_env(env, name, value)
        return evaluate(node['expression'], new_env)
    else:
        raise 'unknown'


class HelloStringsLangTests(unittest.TestCase):
    def test_excite(self):
        self.assertEqual(
            'x!',
            evaluate({
                'type': 'Excite',
                'expression': {
                    'type': 'String',
                    'content': 'x',
                },
            }),
        )

    def test_excite_nested(self):
        self.assertEqual(
            'x!!',
            evaluate({
                'type': 'Excite',
                'expression': {
                    'type': 'Excite',
                    'expression': {
                        'type': 'String',
                        'content': 'x',
                    },
                },
            }),
        )

    def test_variable_basic(self):
        self.assertEqual('Hello, world!', evaluate(
            {'type': 'Variable', 'name': 'x'},
            {'x': 'Hello, world!'}
        ))

    def test_variable_complex(self):
        self.assertEqual(
            'Hello, world!',
            evaluate({
                'type': 'Let',
                'name': 'x',
                'value': {
                    'type': 'String',
                    'content': 'Hello, world',
                },
                'expression': {
                    'type': 'Excite',
                    'expression': {
                        'type': 'Variable',
                        'name': 'x',
                    }
                }
            }, {})
        )

    def test_extend_env(self):
        env = {'a': '2'}
        new_env = extend_env(env, 'b', '3')
        self.assertDictEqual(new_env, {'a': '2', 'b': '3'})
        self.assertDictEqual(env, {'a': '2'})


if __name__ == '__main__':
    unittest.main()
