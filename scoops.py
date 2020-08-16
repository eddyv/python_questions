class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        scoops = []
        for i in self.ingredients:
            for j in self.toppings:
                scoops.append([i,j])
        return scoops

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    # emptymachine = IceCreamMachine([],[])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
    # print(emptymachine.scoops())