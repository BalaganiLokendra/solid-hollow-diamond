N = int(input())
i = N - 1
while i >= 0 :
    left_space = " "*i
    stars = "* "*(N-i)
    print(left_space+stars)
    i = i - 1
j = 1
while j < N:
    if j == N-1:
        left_space = " "*(j)
        stars = "* "
        print(left_space+stars)
    else:
        left_space = " "*(j)
        stars_gap = "  "*(N-j-2)
        stars = "* "
        print(left_space+stars+stars_gap+stars)
    j = j + 1