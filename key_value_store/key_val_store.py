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
        # self.in_transaction = False # initially planned to use this, but since nested kv store, it shall not be the boolean to decide whether a value is added to temp store, rather it should be the length of the temp stack

    def has_temp_transaction(self):
        return len(self.temp) > 0
    
    # methods for changing key val store
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

    # methods for changing the staging mechanism
    def begin(self):
        # adds on an additional transaction to the system
        # it will add on from either the previous saved temp OR
        # if there's no temp, it will add on from perm
        
        if self.has_temp_transaction():
            self.temp.append(self.temp[-1].copy())
        else:
            self.temp.append(self.perm.copy())
    
    def update_storage(self, old_s, new_s):
        # want to update changes in old to new
        # if key in old, but not in new, add to new
        # if key in old and new, make value of new to old
        # if key not in old, but in new, delete from new
        
        # run through twice
        for k, v in old_s.items():
            new_s[k] = v # add or update values & keys in key-val store
        
        for k in new_s:
            if k not in old_s:
                del new_s[k]

    def commit(self): # only applicable when there are transactions
        # pushes the changes inside the temp to the perm DS (ends curr transaction)
        # if there is temp transactions
        if self.has_temp_transaction():
            if len(self.temp) == 1:
                self.update_storage(self.temp[-1], self.perm) # update changes from temp to perm
            else:
                self.update_storage(self.temp[-1], self.temp[-2]) # update changes from latest to 2nd latest
        # if no temp transaction, nth happens
    
    def rollback(self): # only applicable when there are transactions
        # removes the temp changes (ends curr transaction)
        # if there is, if will pop the change, else nth happens
        if self.has_temp_transaction():
            self.perm.pop() # pops the latest temp changes

def main():
    # code to test key value store
    pass

if __name__ == "__main__":
    main()