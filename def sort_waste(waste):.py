def sort_waste(waste):
    return sorted(waste, key=lambda x: (x[1], x[0]), reverse=True)

waste = [ ("paper",20,5),("glass", 30, 2), ("plastic", 10, 3), ("metal", 40, 1)]
sorted_waste = sort_waste(waste)
print("Sorted Waste:")
print(sorted_waste)

def identify_reusable_materials(sorted_waste):
    reusable_materials = []
    for material in sorted_waste:
        if material[1] > 20:
            reusable_materials.append(material)
    print("materials that can be reused:")
    return reusable_materials

reusable_materials = identify_reusable_materials(sorted_waste)
print(reusable_materials)

def send_to_recycling_center(sorted_waste, reusable_materials):
    recyclable_materials = [material for material in sorted_waste if material not in reusable_materials]
    print("materials that can not be reused but recycled:")
    return recyclable_materials

recyclable_materials = send_to_recycling_center(sorted_waste, reusable_materials)
print(recyclable_materials)

def send_to_landfill(sorted_waste, reusable_materials, recyclable_materials):
    landfill_materials = [material for material in sorted_waste if material not in reusable_materials and material not in recyclable_materials]
    return landfill_materials

landfill_materials = send_to_landfill(sorted_waste, reusable_materials, recyclable_materials)
print("materials for landfilling:")
print(landfill_materials)