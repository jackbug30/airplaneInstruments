#Font generator
#Goes by column instead of row

print("THE AMAZING FONT GENERATOR (C) 2023 BROADBERRY TOUCHEAD")
print("Enter pixel data column by column by rotating the character 90* CW,")
print("then enter each column by entering a nonspace for an 'on' pixel,")
print("or a space for an 'off' pixel.")
print("After entering the entire character, you will get the numerical data")
print("in a format that is easy to copy+paste into a text file. Ctrl+C to quit.")
print("ie:")
print("####                   Character:A")
print("#  #                     43210")
print("####       #####       1>#####")
print("#  #  ==>    # #  ==>  1>  # #  ==>   'A':[31, 5, 31],")
print("#  #       #####       2>#####")

while True:
    print("======================================================")
    cols = [0,0,0,0,0]
    character = input("Character:")
    print("  FEDCBA9876543210")
    for col in range(5):
        colData = input("{}>".format(col))
        if len(colData) < 16:
            colData += ' '*(16-len(colData))
        for pixel in range(len(colData)):
            if colData[pixel] == ' ':
                pass
            else:
                cols[col] += 2**(15-pixel)

    print(" '{}':{},".format(character, cols))
