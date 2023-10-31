import numpy as np

def multiply_z(ins, outs):
    Z = ins['Z']
    Z *= 10.0
    outs['Z'] = Z
    
    return True
