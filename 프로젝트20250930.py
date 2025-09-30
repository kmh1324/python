##numbers = [1, 2, 3, 4, 5, 6]
##r_num = reversed(numbers)
##
##print("reversed_number :", r_num)
##print(next(r_num))
##print(next(r_num))
##print(next(r_num))
##print(next(r_num))
##print(next(r_num))


##output = [i for i in range(1, 101) if "{:b}".format(i).count('0') == 1]
##
##for i in output:
##    print("{} : {}".format(i, "{:b}".format(i)))
##print("합계:", sum(output))


##num = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
##num_count = {} 
##
##for i in num:
##    if i not in num_count:
##        num_count[i] = 0
##    
##    num_count[i] += 1
##    
##print(
##    f"{num}에서 사용된 숫자의 종류는 "
##    f"{len(num_count)}개입니다."
##)
##print("참고:", num_count)


##DNA = input("염기 서열을 입력해주세요: ")
##count = {'a': 0, 't': 0, 'g': 0, 'c': 0}
##
##for ch in DNA:
##    count[ch] += 1
##
##for key, value in count.items():
##    print(f"{key}의 개수: {value}")


##DNA = input("염기 서열을 입력해주세요: ")
##count = {}
##
##for i in range(0, len(DNA), 3):
##    codon = DNA[i:i + 3]
##    
##    if len(codon) != 3:
##        break
##    if codon not in count:
##        count[codon] = 0
##
##    count[codon] += 1
##    
##print(count)
    
    
##list1 = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
##list2 = []
##
##for i in list1:
##    if type(i) == list:
##        for j in i:
##            list2 .append(j)
##
##    else :
##        list2.append(i)
##        
##print(f"{list1}를 평탄화하면 {list2}입니다.")


##def print_3_times():
##    print("안녕하세요")
##    print("안녕하세요")
##    print("안녕하세요")
##
##print_3_times()


##def print_n_times(value, n):
##    for i in range(n):
##        print(value)
##
##print_n_times("안녕하세요", 5)


##278
