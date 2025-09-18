movie = [8.0,7.5,5.4,9.1,6.3,6.5,2.1,4.8,3.3]

indx = 0

for i in range(len(movie)):
    if movie[i] >= 6:
        indx +=1
        print(indx,movie[i])

print("there is only",indx,"films gretater then movie reating 6")

