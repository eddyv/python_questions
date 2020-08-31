class Greeter:

    def __init__(self, boss):
        self.boss = boss
        self.lastVisitor = None

    def enters(self, visitor):
        self.lastVisitor = visitor
        return None

    def greet(self):
        visitor = self.lastVisitor
        if visitor == None:
            return None
        if visitor == self.boss:
            self.lastVisitor = None
            return f'Hello, {self.boss}'
        else:
            self.lastVisitor = None
            return f'Welcome, {visitor}'
    
if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    g.enters('Chuck')
    g.enters('Dave')
    print(g.greet())
    g.enters('John')
    print(g.greet())
    print(g.greet())