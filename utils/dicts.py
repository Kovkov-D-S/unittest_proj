def get_val(collection, key, default='git'):
    """
        Возвращает значение из словаря по переданному ключу, если ключ существует.
        Если ключ не существует, возвращает значение по умолчанию.
        :param collection: исходный список.
        :param key: индекс извлекаемого элемента.
        :param default: значение по-умолчанию.
        :return: значение из словаря по переданному ключу.
        """
    if key in collection.keys():
        return collection[key]
    return default
