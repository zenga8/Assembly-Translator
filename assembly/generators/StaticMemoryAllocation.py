from ..helpers.helper import is_constant_name

class StaticMemoryAllocation():

    def __init__(self, global_vars: dict()) -> None:
        self.__global_vars = global_vars

    def generate(self):
        print('; Allocating Global (static) memory')
        for name, (label_num, value) in self.__global_vars.items(): #depending on the variables, we assign different memory allocations
            if is_constant_name(name): 
                s = f"{f'.EQUATE {str(value)}':<10}" #constants
            elif value is not None:
                s = f"{f'.WORD {str(value)}':<10}" #initial values
            else:
                s = f"{'.BLOCK 2':<10}" #unknowns (e.g., inputs, while loops)
            s = "\t\t" + s
            print(f'{str("var"+str(label_num)+":"+s):<9}   ; {name}')
