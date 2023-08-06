from dataclasses import dataclass


@dataclass

class NumberNode:
    value: float

    def __repr__(self) :
        return f"{self.value}"
    

#Add node
@dataclass
class AddNode:
    node_a: any
    node_b: any 

    def __repr__(self) :
        return f"({self.node_a}+{self.node_b})"

# Subtract node

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self) :
        return f"({self.node_a}-{self.node_b})"
    
#multiply node

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self) :
        return f"({self.node_a}*{self.node_b})"
    
# Division node

@dataclass
class DivisionNode:
    node_a: any
    node_b: any

    def __repr__(self) :
        return f"({self.node_a}/{self.node_b})"
    
@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"
    
@dataclass 
class MinusNode:
    node: any

    def __repr__(self) :
        return f"(-{self.node})"