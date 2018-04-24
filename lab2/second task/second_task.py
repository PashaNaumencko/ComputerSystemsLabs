from BitVector import BitVector


def subtraction(first_num, second_num):
    return BitVector(size=32, intVal=first_num.int_val() - second_num.int_val())


def division(divident, divisor):
    remainder = BitVector(intVal=1, size=32)
    quotient = BitVector(size=32)
    print("divident:", divident)
    print("divisor: ", divisor)
    print("Step by step calculation:")
    print("Searching for the first 1 in divident")
    i = 0
    while not divident[i]:
        i += 1
    print("Position of first 1:", i)
    print("Writing remainder as first half of result register")
    while i != len(divident):
        print(remainder, quotient)
        print("Checking if divisor is greater than remainder")
        if divisor >= remainder:
            print("If true, expanding remainder with next divident symbol")
            remainder.shift_left_by_one()
            remainder[-1] = divident[i + 1]
        else:
            print("If false, subtracking divisor from remainder and shift remainder to the left")
            print("and set 1 in quotient in the according divident index")
            remainder = subtraction(remainder, divisor)
            remainder.shift_left_by_one()
            quotient[i - 32] = 1
        i += 1
    print("Final result:", remainder, quotient)
    print("Final result in decimal: quotient:", quotient.int_val(), ", remainder:", remainder.int_val())



