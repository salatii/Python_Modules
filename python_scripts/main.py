import sys
def returnvalue(str) :
    if str == "hi" :
        return "yes"
    else :
        return "no"
print("calling python function with parameters:")
print(sys.argv[1])
str = sys.argv[1]
res = returnvalue(str)
print(res)
with open("C:/Users/natha/IdeaProjects/demo/src/main/java/com/example/demo/python/file.txt", 'w') as target:
    target.write(res)