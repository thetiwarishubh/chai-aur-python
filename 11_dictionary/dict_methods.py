import json

data = {
    "college": "Delhi Institute of Technology",
    "location": {
        "city": "Delhi",
        "area": "Dwarka",
        "pincode": 110075
    },
    "students": {
        "S001": {
            "name": "Aarav Sharma",
            "age": 20,
            "branch": "CSE",
            "year": 2,
            "subjects": {
                "Python": 85,
                "DSA": 78,
                "Maths": 90
            },
            "hobbies": ["coding", "cricket", "music"],
            "address": {
                "city": "Delhi",
                "state": "Delhi",
                "pin": 110091
            }
        },
        "S002": {
            "name": "Priya Verma",
            "age": 21,
            "branch": "IT",
            "year": 3,
            "subjects": {
                "Python": 92,
                "DSA": 88,
                "DBMS": 81,
                "OS": 79
            },
            "hobbies": ["reading", "painting", "traveling"],
            "address": {
                "city": "Noida",
                "state": "UP",
                "pin": 201301
            }
        },
        "S003": {
            "name": "Rahul Meena",
            "age": 19,
            "branch": "ECE",
            "year": 1,
            "subjects": {
                "Electronics": 75,
                "Maths": 82,
                "Programming": 80
            },
            "hobbies": ["gaming", "football"],
            "address": {
                "city": "Faridabad",
                "state": "Haryana",
                "pin": 121001
            }
        },
        "S004": {
            "name": "Sneha Gupta",
            "age": 22,
            "branch": "CSE",
            "year": 4,
            "subjects": {
                "AI": 91,
                "ML": 89,
                "DL": 87,
                "Python": 95
            },
            "hobbies": ["AI research", "blogging", "music"],
            "address": {
                "city": "Ghaziabad",
                "state": "UP",
                "pin": 201002
            }
        }
    },
    "faculty": {
        "F001": {
            "name": "Dr. Anil Kumar",
            "subject": "Data Structures",
            "experience_years": 12
        },
        "F002": {
            "name": "Dr. Meera Joshi",
            "subject": "Artificial Intelligence",
            "experience_years": 10
        }
    },
    "library": {
        "total_books": 50000,
        "sections": {
            "programming": 12000,
            "electronics": 8000,
            "mechanical": 7000,
            "fiction": 15000,
            "others": 8000
        }
    }
}

# print(json.dumps(data, indent=4))


# clear()
# Removes all the elements from the dictionary
# print(data.clear())


# copy()
# Returns a copy of the dictionary
# x = data.copy()
# print(x)


# fromkeys()
# Returns a dictionary with the specified keys and value

# print(data.fromkeys("college"))

# get()
# Returns the value of the specified key
# x = data.get("college")
# print(x)


# print(data.items())
# print(data.keys())
# print(data.values())

# print(data.pop("college"))

# print(data.popitem())

def count_consonants(x):
    text = x.lower()
    count = set()
    splited_text = list(text)
    for i in splited_text:
        if i.isalpha() and i not in "aeiou":
            count.add(i)
    return count

print(count_consonants("Shubham tiwari"))