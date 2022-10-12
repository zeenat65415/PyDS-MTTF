# func-3 in this we can pass input and return output
def word_count(msg):#msg becomes parameter or arguement
 words = msg.split()#The split() mwthod splits string into a list
 return len(words)#return

words = word_count("This is time to go home")#fn call,TypeError:word_count() missing 1 required positional argument: 'msg'
print(words)

#     types of Parameter Styles-
# =>required parameter
# =>default parameter
# =>variable arguements
# =>keyword arguements


#Parameters
# Parameters are the variables in the definition of a function.In other words ,
#  they exist in the function signature and will be used as variables in the function body .
#whereas,
# Arguements
# Arguements are the actual values that were passed to the function when we call it.
# In other words,an arguement could be an integer,a string or any object.