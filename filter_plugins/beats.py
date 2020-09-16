#!/usr/bin/env python3

import unittest
from typing import List, Dict


class Beats:
    @staticmethod
    def delete_key_from_dicts(items: List[Dict], key: str) -> List[Dict]:
        for item in items:
            del item[key]
            yield item


class BeatsTest(unittest.TestCase):
    def test_flatten_htpasswd(self):
        self.assertEqual(
            list(Beats.delete_key_from_dicts([{'foo': 123, 'bar': 456}, {'baz': 123, 'foo': 456}], 'foo')),
            [{'bar': 456}, {'baz': 123}],
        )


class FilterModule(object):
    def filters(self):
        return {
            'beatsclient_delete_key_from_dicts': Beats.delete_key_from_dicts,
        }


if __name__ == '__main__':
    unittest.main()
