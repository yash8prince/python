marks = {
    "Yash": 100,
    "Prince": 69,
    34: "Harry"
}
print(marks.items()) # to show all items
print(marks.keys())
print(marks.values())
marks.update({"Yash":99, "Singh": 70}) # singh is added if not exist
print(marks)
print(marks.get("Yash2"))# prints none
print(marks["Yash2"])# returns an error


