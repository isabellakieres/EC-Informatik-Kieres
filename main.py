def count_integer(numbers, integer):
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == integer:
            count += 1

    if count >= 1:
        return count

    elif count < 1:
        return "42"


def list_func(numbers, integer):
# I don't know how to solve this one


def compare_lists(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements


def remove_duplicates(lst):
    return list(set(lst))


def dict_func(dictionary):
    type = dictionary.get("Type", "unknown type")
    brand = dictionary.get("Brand", "unknown brand")
    price = dictionary.get("Price", "unknown price")
    print("You have a {} from {} that costs {}.".format(type, brand, price))
    dictionary["OS"] = "Linux"
    print(dictionary)










