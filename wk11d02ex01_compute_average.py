def computeAverage(numbers):
    total = 0
    count = 0
    for i in range(0, len(numbers)):
        num = numbers[i]
        total = total + num
        count = count + 1
 
    return total / count
 
 
if __name__ == "__main__":
    count = int(input())
    numbers = [0] * count
 
    for i in range(count):
        print(f"Input the value of the {i + 1} number")
        numbers[i] = int(input())
 
    average = computeAverage(numbers)
    print(f"Average: {average}")
 
