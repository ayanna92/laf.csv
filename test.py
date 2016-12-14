dictionary= {
"apple": [3,4,5,6,7,8,6,3],
"banana": 6,
"jhajh": 8,
"test": 9
}

dictionary["pear"] = dictionary.pop("banana")
print dictionary
print("lengte:", len(dictionary))
dictionary["banana"] = dictionary.pop("apple")
print dictionary
print("lengte:", len(dictionary))
