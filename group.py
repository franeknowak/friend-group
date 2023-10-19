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

def forget(person1: str, person2: str):
    # This function removes connection between two people in the friend group dictionary
    del my_group[person1]['connections'][person2]
    del my_group[person2]['connections'][person1]

def add_person(name: str, age: int, job: str, relations: dict):
    # This function adds a new person and updates connections between them and already existing group members

    # First add the new person to the group
    my_group[name]['job'] = job
    my_group[name]['age'] = age
    my_group[name]['connections'] = relations

    # Update the existing members connection list
    for person in relations:
        my_group[person]['connections'][name] = relations[person]
