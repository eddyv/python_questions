def group_by_owners(files):
    owners = {}
    for k, v in files.items():
        owners.setdefault(v, []).append(k)    
    
    return owners

#   Example case: Correct answer
#   Each owner has a single file: Correct answer
#   Various files: Correct answer
#   Function group_by_owners is called more than one time: Correct answer 

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))