names_set = {"Alice", "Andrew", "Bob", "Bill", "Amanda", "Ben"}

set_a = {name for name in names_set if name.startswith("A")}
set_b = {name for name in names_set if name.startswith("B")}

print("Names starting with A:", set_a)
print("Names starting with B:", set_b)

