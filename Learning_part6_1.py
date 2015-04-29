class Adder(object):
    def add(self, x, y):
        print("Not Implemented")
    
class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        x.update(y)
        new_dict = {key : x[key] for key in x}
        return new_dict
            
