# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

a = int(input())
b = input()
list = []
for i in b:
    list.append(i)

print(a*int(list[2]))
print(a*int(list[1]))
print(a*int(list[0]))
print(a*int(b))
