#Function is basiclly some line of code that could be used several times just by calling it

#Function in python start with def

def NumberCheckingFunc():
  a = 5
  if a % 2 == 0:
    print("its even")
  else:
    print("its odd")


#now we can call the function
NumberCheckingFunc()

#here the function is doesnt need any argument because we are not setting the parameter in the function
#example for function with paramater and argument 

def ParameterFunc(a):
  print(a)

ParameterFunc(10)

#if there is a paramater then an argument is needed, and a parameter is only for one argument
