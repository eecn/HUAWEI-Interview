def shell_sort(numbers):
    lens = len(numbers)
    gap =1
    while  gap<(lens//3):
        gap = gap*3 + 1
    while gap>0:
        for i in range(gap,lens):
            curNum ,preIndex = numbers[i],i-gap
            while preIndex>=0 and curNum<=numbers[preIndex]:
                numbers[preIndex+gap] = numbers[preIndex]
                preIndex = preIndex - gap
        gap = gap //3
    return numbers
