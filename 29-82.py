
length = int(input("Enter the length of the zander in centimeters: "))


limit = 42

if length >= limit:
    print("The zander meets the size limit. You can keep it!")
else:
    short = limit - length
    print(f"The zander is {short} cm below the size limit.")
    print("Please release the fish back into the lake.")
