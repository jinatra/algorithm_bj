def solution(arr):
    answer = []
    while True:
        n = len(arr)
        if n == 1:
            answer += arr
        arr.reverse()
        if n % 2 == 0:
            k = n // 2
            return arr[:k], arr[k:]
        else:
            k = (n-1) // 2
            return arr[:(k+1)], arr[k+1]
    return answer

print(solution([1,2,3,4,5]))
