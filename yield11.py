# def provider():
#     for i in range(4):
#         yield i
#
# p=provider()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

ll=[1,2,3,"aa",'bb']
def ss():
    for i in ll:
        print("start")
        yield i  #yield相当于return+暂停+记录上一次运行位置
        print("end")

s=ss()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


