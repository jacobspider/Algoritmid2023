def rehash(old_table):
    new_capacity = len(old_table) * 2
    new_table = [None] * new_capacity

    for item in old_table:
        if item is not None:
            
            index = hash(item[0]) % new_capacity
            new_table[index] = item
    
    return new_table


old_table = [("key1", "value1"), ("key2", "value2"), None, None]
new_table = rehash(old_table)
