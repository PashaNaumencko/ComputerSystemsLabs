from second_task import division
from BitVector import BitVector


try:
    print("Enter a divident:", end="")
    divident = BitVector(intVal=int(input(), 2), size=64)
    print("Enter a divisor:", end="")
    divisor = BitVector(intVal=int(input(), 2), size=64)
    division(divident, divisor)
except Exception as e:
    print(e.__str__())
