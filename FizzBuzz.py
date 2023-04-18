def replace_with_fizzbuzz(int_list):
    for i in range(len(int_list)):
        if int_list[i]%15 == 0:
            int_list[i] = "FizzBuzz"
        elif int_list[i]%3 == 0:
            int_list[i] = "Fizz"
        elif int_list[i]%5 == 0:
            int_list[i] = "Buzz"
    return int_list

int_list = list(range(1, 101, 1))

fizzbuzz_list = replace_with_fizzbuzz(int_list)

print(fizzbuzz_list)
