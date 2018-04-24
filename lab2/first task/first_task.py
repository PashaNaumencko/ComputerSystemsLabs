from BitVector import BitVector


def multiplication(multiplicand, multiplier):
    carry = 0
    register = BitVector(intVal=multiplier.int_val(), size=64)
    print("Initial register:", register)
    for i in range(30, -1, -1):
        if register[-1]:
            for y in range(31, -1, -1):
                if carry:
                    if register[y + 1] & multiplicand[y]:
                        register[y + 1] = 1
                        carry = 1
                    elif register[y + 1] | multiplicand[y]:
                        register[y + 1] = 0
                        carry = 1
                    else:
                        register[y + 1] = 1
                        carry = 0
                else:
                    if register[y + 1] & multiplicand[y]:
                        register[y + 1] = 0
                        carry = 1
                    elif register[y + 1] | multiplicand[y]:
                        register[y + 1] = 1
                    else:
                        register[y + 1] = 0
            print("Add multiplicand to register:", register)
        print("Shift register by one:", register)
        register.shift_right_by_one()
    print("Final result:", register)
    print("Final result in decimal:", register.int_val())


