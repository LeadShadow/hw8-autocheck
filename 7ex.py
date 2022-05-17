import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if type(cats[0]) == Cat:
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]
    else:
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]


cats = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

print(convert_list(cats))
