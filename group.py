"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill': {
                'job': 'Biologist',
                'age': 26,
                'connections': {
                    'Zalika': 'friend',
                    'John': 'partner'}},
            'Zalika': {
                'job': 'Artist',
                'age': 28,
                'connections': {
                    'Jill': 'friend',
                    'Nash': 'landlord'}},
            'John': {
                'job': 'Writer',
                'age': 27,
                'connections': {
                    'Jill': 'partner',
                    'Nash': 'cousin'}},
            'Nash': {
                'job': 'chef',
                'age': 34,
                'connections': {
                    'John': 'cousin',
                    'Zalika': 'landlord'}}}

def average_age(dic):
    age_list = []
    for person in dic:
        age_list.append(dic[person]['age'])
    return sum(age_list)/len(age_list)

print(average_age(my_group))