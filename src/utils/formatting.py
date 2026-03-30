def separator():
    print("—" * 40)

def fmt(n: float) -> float | int:
    if float(n).is_integer(): # if n is 1.0  
        return int(n) # 1.0 -> 1

    return n