# Count words


str_input = input("Please Enter a string ? ")

def count_words(x):
    count = 0
    for i in range(len(x)):
        if x[i] == " ":
            count
        else :
            count +=1
    return count


print(count_words(str_input.strip()))