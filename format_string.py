def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    str = ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
    return str
nm=([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]) #defining the list name
print(namelist(nm))