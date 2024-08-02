def distribute_apples():
    apples = []
    while True:
        weight = int(input("Enter apple weight in gram (-1 to stop) : "))
        if weight == -1:
            break
        apples.append(weight)
    
    total_weight = sum(apples)
    
    total_amount = 50 + 30 + 20  
    proportion = {
        "Ram": 50 / total_amount,
        "Sham": 30 / total_amount,
        "Rahim": 20 / total_amount
    }
    
    target_weights = {
        "Ram": proportion["Ram"] * total_weight,
        "Sham": proportion["Sham"] * total_weight,
        "Rahim": proportion["Rahim"] * total_weight
    }
    
    # Allocate apples
    allocations = {
        "Ram": [],
        "Sham": [],
        "Rahim": []
    }
    
    def find_person_to_allocate():
        min_diff = float('inf')
        person = None
        for p in allocations:
            current_weight = sum(allocations[p])
            target_weight = target_weights[p]
            if target_weight - current_weight < min_diff:
                min_diff = target_weight - current_weight
                person = p
        return person
    
    for apple in sorted(apples, reverse=True):
        person = find_person_to_allocate()
        if person:
            allocations[person].append(apple)
    
    print("Distribution Result :")
    for person in allocations:
        print(f"{person} : {' '.join(map(str, allocations[person]))}")

distribute_apples()
