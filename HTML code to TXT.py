#goal, make a program to automatically convert <> into &lt; and &gt;
user_input = input("Convert Text:")
changed_result1 = user_input.replace("<","&lt;") 
changed_result2 = changed_result1.replace(">","&gt;")
print(changed_result2)
