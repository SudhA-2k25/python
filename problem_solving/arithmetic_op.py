def arithmetic_op(a , b):
    add = a + b
    sub = b - a
    mul = a * b 
    if b!=0:
        div = a/b
    else:
        print(f"{a}/{b} is not defined")
    return add , sub , mul , div
addition , subtraction , multi , divi = arithmetic_op(2,9)
print(f"addition = {addition}")
print(f"subtraction = {subtraction}")
print(f"multiplication = {multi}")
print(f"division = {divi}")
