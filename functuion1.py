def count_lower_upper(s):
    counts = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
    return counts

test_string = "Hello World! This is a Test String."

result = count_lower_upper(test_string)
print("Uppercase Letters:", result["uppercase"])
print("Lowercase Letters:", result["lowercase"])
