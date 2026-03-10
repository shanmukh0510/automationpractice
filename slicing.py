numbers = [1,3,5,7,788,9,90,34,556,78,88,6,4,54]
           #0, 1,2,3                        ,-4,-3,-2-1

print(numbers[-1])


# slicing
#[start: stop : step]

print(numbers[2:10:2])


# reverseing string

name = "vijaykumar"

print(name[::-1])

reverse_string = ""
for i in name:
    reverse_string =   i + reverse_string

    print(reverse_string)

