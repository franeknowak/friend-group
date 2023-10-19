"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill' : {
        'job': 'biologist',
        'age': 26,
        'connections': {
            'Zalika': 'Friend',
            'John': 'Partner'
        }
    },
    'Zalika' : {
        'job': 'artist',
        'age': 28,
        'connections': {
            'Jill': 'Friend'
        }
    },
    'John' : {
        'job': 'writer',
        'age': 27,
        'connections': {
            'Jill': 'Partner'
        }
    },
    'Nash' : {
        'job': 'chef',
        'age': 34,
        'connections': {
            'John': 'Cousin',
            'Zalika': 'Landlord'
        }
    },
}

print(my_group)
