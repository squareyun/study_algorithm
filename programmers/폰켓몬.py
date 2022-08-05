# TITLE: 폰켓몬 (https://school.programmers.co.kr/learn/courses/30/lessons/1845)
# TYPE: hash
# DATE: 20220804
# AUTHOR: squareyun

def solution(nums):
    answer = len(nums) // 2
    nums = set(nums)
    return answer if len(nums) > answer else len(nums)