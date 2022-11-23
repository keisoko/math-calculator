import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantNamespace:
    LIST_OPERATION: str = "addition"


constant = ConstantNamespace()


def calculate_value(operator: str, *args: int) -> int | float | str:
    match operator:
        case "addition":
            return f"The result of addition is {sum(args)}"
        case "subtraction":
            return f"The result of subtracting {args[1]} from {args[0]} is {args[0] - args[1]}"
        case "multiplication":
            return f"The result of multiplying {args[0]} by {args[1]} is {args[0] * args[1]}"
        case "division":
            return (
                f"The result of dividing {args[0]} by {args[1]} is {args[0] / args[1]}"
            )
        case "exponent":
            return f"The result of raising {args[0]} to the power of {args[1]} is {args[0] ** args[1]:,}"
        case "modulo":
            return f"The remainder of the modulo operation between {args[0]} and {args[1]} is {args[0] % args[1]}"
        case "root":
            return f"The square root of {args[0]} is {math.sqrt(args[0])}"
        case "cube root":
            return f"The cube root of {args[0]} is {math.cbrt(args[0])}"
        case _:
            return "Wrong operator"


def execute_main():
    math_operation = "addition"
    first_number = 27
    second_number = 10
    print(calculate_value(math_operation, first_number, second_number))

    list_of_numbers_to_sum = [27, 35, 48, 60]
    print(calculate_value(constant.LIST_OPERATION, *list_of_numbers_to_sum))

    root_operation = "cube root"
    number_to_be_rooted = 729
    print(calculate_value(root_operation, number_to_be_rooted))


if __name__ == "__main__":
    execute_main()
