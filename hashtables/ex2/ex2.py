#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []

    for i in range(len(tickets)):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    index = hash_table_retrieve(ht, "NONE")
    route.append(index)
    for i in range(length - 1):
        next_index = hash_table_retrieve(ht, index)
        route.append(next_index)
        index = next_index

    return route