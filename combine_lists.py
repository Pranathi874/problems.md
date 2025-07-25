import json

def is_more_than_half_inside(a, b):
    a_left, a_right = a['positions']
    b_left, b_right = b['positions']

    overlap_left = max(a_left, b_left)
    overlap_right = min(a_right, b_right)
    overlap = max(0, overlap_right - overlap_left)

    len_a = a_right - a_left
    len_b = b_right - b_left

    return overlap > len_a / 2 or overlap > len_b / 2

def combine_elements(el1, el2):
    return {
        "positions": el1["positions"],
        "values": el1["values"] + el2["values"]
    }

def combine_lists(list1, list2):
    combined = []
    used = [False] * len(list2)

    for item1 in list1:
        merged = False
        for idx2, item2 in enumerate(list2):
            if not used[idx2] and is_more_than_half_inside(item1, item2):
                combined.append(combine_elements(item1, item2))
                used[idx2] = True
                merged = True
                break
        if not merged:
            combined.append(item1)

    for idx2, item2 in enumerate(list2):
        if not used[idx2]:
            combined.append(item2)

    return sorted(combined, key=lambda x: x["positions"][0])

print("Enter first list (as JSON):")
input1 = input()
print("Enter second list (as JSON):")
input2 = input()

list1 = json.loads(input1)
list2 = json.loads(input2)

result = combine_lists(list1, list2)

print("\nCombined result:")
print(json.dumps(result, indent=2))
