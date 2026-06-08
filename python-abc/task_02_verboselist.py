class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        items = list(items)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)


vl = VerboseList()
vl.append(1)
vl.append(2)
vl.append(3)
vl.extend([4, 5, 6])
vl.remove(3)
vl.pop()
vl.pop(0)
