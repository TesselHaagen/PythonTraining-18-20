from decimal import *

def frange(start: str, stop: str, step='1.0', endpoint=False):
    """
    Creates a sequence from start to stop with a stepsize.

    Argmunets:
    - start (str): the start point of the sequence
    - stop (str): the stop point of the sequence
    - step (str): the stepsize of the sequence
    - endpoint (bool): wether or not to include stop in the sequence

    Returns:
    A sequence of numbers

    """
    # Convert strings to Decimals
    start = Decimal(start)
    stop = Decimal(stop)
    step = Decimal(step)

    # Begin with an empty list
    seq = []
    while True:
        if endpoint and start > stop or not endpoint and start >= stop: # We stoppen als start groter wordt dan stop
                break
        
        # Append the start to the list
        seq.append(start)

        # Increase the step to the start value
        start = start + step
    


    return seq


print(frange('1.95', '2', '0.05', True))