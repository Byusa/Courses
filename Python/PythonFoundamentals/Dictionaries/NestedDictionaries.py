# Nested Dictionaries
my_family = {
    "child1": {
        "name":"Claudine",
        "year": 1984
    },
    "child2": {
        "name": "Byusa",
        "year": 1993
    },
    "child3": {
        "name": "Bella",
        "year": 2009
    }
}
print(my_family)

# Add three dictionaries into one
child1 = {
        "name":"Claudine",
        "year": 1984
    }
child2 = {
        "name": "Byusa",
        "year": 1993
    }
child3 = {
        "name": "Bella",
        "year": 2009
    }
my_family = { "child1": child1, "child2": child2, "child3": child3 }
print(my_family)