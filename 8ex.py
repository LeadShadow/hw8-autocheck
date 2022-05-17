from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)


def get_frequent_visit_from_ip(ips):
    counts_ip = Counter(ips)
    return counts_ip.most_common(1)[0]


ips = [
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.258",
    "85.157.172.252",
    "85.157.172.251",
    "85.157.172.251",

]

print(get_count_visits_from_ip(ips))