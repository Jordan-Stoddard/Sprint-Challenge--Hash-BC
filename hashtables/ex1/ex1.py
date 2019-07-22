#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    indexSet = set()

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(weights)):
        if hash_table_retrieve(ht, limit - weights[i]) is not None:
                indexSet.add(i)
    
    if len(indexSet) == 0:
        return None
    else:
        return sorted(indexSet, reverse=True)


def print_answer(answer):
    if answer is not None:
        print(f'{answer[0]} {answer[1]}')
    else:
        print("None")