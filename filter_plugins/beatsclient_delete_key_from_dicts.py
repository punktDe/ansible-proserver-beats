def delete_key_from_dicts(items: dict, key: str):
    for item in items:
        del item[key]
    return items


class FilterModule(object):
    def filters(self):
        return {
            'beatsclient_delete_key_from_dicts': delete_key_from_dicts,
        }
