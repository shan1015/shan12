int1=int(input())
nums=list(map(int,input().split()))
tem=0
div=len(nums)
for i in range(int1):
    tem+=nums[i]
res=tem//div
print(res)
