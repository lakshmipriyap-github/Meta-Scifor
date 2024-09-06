'''
In a forest, trees grow with unique patterns. Define a Tree class with
growth() method generating tree patterns. Derive Pine and Oak classes
inheriting Tree. Implement recursion to visualize the growth pattern of
each tree. Instructions: Define a Tree class with a growth() method
generating tree patterns. Derive Pine and Oak classes inheriting Tree,
overriding the growth() method. Use recursion to visualize the growth
pattern of both a Pine tree and an Oak tree.
'''
class Tree:
    def growth(self):
        self.pattern = "Tree pattern"
        return self.pattern

class Pine(Tree):
    def growth(self):
        self.pattern = "Pine pattern"
        return self.pattern
class Oak(Tree):
    def growth(self):
        self.pattern = "Oak pattern"
        return self.pattern

def DisplayPattern(obj):
    print(f"{obj.growth()}")

obj = Tree()
DisplayPattern(obj)

obj1 = Pine()
DisplayPattern(obj1)

obj2 = Oak()
DisplayPattern(obj2)