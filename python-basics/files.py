"""
f is 
"""

file_name = "some_file.txt"

f = open(file_name, mode="a", encoding="utf-8")
f.write("\n\nAdd this Please")
f.close()

with open(
    file_name,
) as of:
    file_data = of.read()

print(file_data)

# files = []
# for i in range(1000000):
#     files.append(open("some_file.txt", "r"))
#     print(i)
