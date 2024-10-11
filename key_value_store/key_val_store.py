#!/usr/bin.env python3

# Key value store implementation
# This key value store supports 3 basic functions: Begin, Commit & Rollback (definitions are described below)
# 

# Begin() - Starts a new transaction allowing user to perform multiple operations as a batch.
# Changes made in this transaction are temporary until user either commits or roll them back

# Commit() - Finalizes the transaction, applying all the changes made since the begin() call permanently to the key-value store

# Rollback() - Cancels the current transaction, undoing all the changes made since the begin() call & reverting the key-value store
# to the state it was in before the transaction began

# Certain clarifications:
# - if Rollback was called before Begin() was called, => im suggesting nothing occurs since no begin() created a chance for temp changes
# - if commit() was called before begin() was called, => im suggesting that no new changes 
# - if its already in transaction & begin() is called, continue to stay in transction

# Description of my implementation:
# transaction system will support nested transactions (i.e. T1 calls put (x, 1), T2 calls put (y, 2), rollback() is called, T2 is discarded but not T1)
# supports, getting, putting and deleting values from the key value store
# if no temp transaction was initiated, alteration actions done will be to the permanent key value store

class key_value_store:
    
    def __init__(self):
        self.perm = {}
        self.temp = []

    def has_temp_transaction(self):
        return len(self.temp) > 0
    
    def get(self, key):
        if self.has_temp_transaction():
            return self.temp[-1][key]
        else:
            return self.perm[key]

    def put(self, key, value):
        if self.has_temp_transaction():
            self.temp[-1][key] = value
        else:
            self.perm[key] = value

    def delete(self, key):
        if self.has_temp_transaction():
            if self.temp[-1].get(key):
                del self.temp[-1][key]
        else:
            if self.perm.get(key):
                del self.perm[key]

    def begin(self):
        if self.has_temp_transaction():
            self.temp.append(self.temp[-1].copy())
        else:
            self.temp.append(self.perm.copy())
    
    def update_storage(self, old_s, new_s):
        for k, v in old_s.items():
            new_s[k] = v
        for k in new_s:
            if k not in old_s:
                del new_s[k]

    def commit(self):
        if self.has_temp_transaction():
            if len(self.temp) == 1:
                self.update_storage(self.temp[-1], self.perm)
            else:
                self.update_storage(self.temp[-1], self.temp[-2])
    
    def rollback(self):
        if self.has_temp_transaction():
            self.perm.pop()

def main():
    # code to test key value store
    pass

if __name__ == "__main__":
    main()