from first_task import multiplication
from BitVector import BitVector

try:
    print("Enter a multiplicand:", end="")
    multiplicand = BitVector(intVal=int(input(), 2), size=32)
    print("Enter a multiplier:", end="")
    multiplier = BitVector(intVal=int(input(), 2), size=32)
    multiplication(multiplicand, multiplier)
except Exception as e:
    print(e.__str__())
