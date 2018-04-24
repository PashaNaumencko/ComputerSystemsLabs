from third_task import multiplication, print_number


try:
    print("Enter a first number:", end="")
    first_num = int(input(), 2)
    print("Enter a second number:", end="")
    second_num = int(input(), 2)
    print("Entered numbers:\nfirst number:", first_num, "second number:", second_num)
    print("Multiplication")
    print_number(multiplication(first_num, second_num))
except Exception as e:
    print_number(e.__str__())
