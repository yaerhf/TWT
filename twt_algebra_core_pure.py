import numpy as np
from clifford.g4 import *

class Cl4EnginePure:
    """
    Pure CPU Academic implementation of the TWT Algebra engine.
    This strictly uses the non-commutative functions built-in to the python `clifford` library.
    It serves directly as the math validity benchmark for the Torch engine.
    """
    def __init__(self):
        pass

    def mul(self, A, B):
        """
        Pure Geographic Product on MVArrays.
        A and B are instantiated `clifford` MVArrays.
        """
        return A * B
        
    def rev(self, A):
        """
        Reverse the multivector grid
        """
        return ~A
        
    def add(self, A, B):
        return A + B
        
    def sub(self, A, B):
        return A - B

engine_pure = Cl4EnginePure()
