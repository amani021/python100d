#-------- DAY 68 "extra exercise" --------
arr = []
size = int(input("How much the elements do you want in an array? "))
print("Enter the elements:")
for x in range(size):
    arr.append(input())
print("\nNow, the array with your elements is:\n", " ".join(arr))
