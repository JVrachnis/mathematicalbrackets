text = input().replace(" ", "")
while text.find("()")> -1:text = text.replace("()","")
if len(text) == 0:print("true")
else:print("false")
