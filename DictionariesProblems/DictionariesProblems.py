# Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
di = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(di["key1"])
di["key4"] = "value4"
print(di)
print(len(di))

# Reassignment by Key and Del:
di2 = {"k1": "alpha", "k2": "beta"}
print(di2)
di2["k2"] = "gamma"
print(di2)
try:
    del di2['k2']
except:
    di2.pop('k2', None)
print(di2)