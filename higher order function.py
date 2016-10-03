def test(func,arg):
	return func(func(arg))
	
def mult(x):
	return x * x
	
print(test(mult,2))
# This page can be found on 
# https://gist.github.com/874aa5a35996504af1d7573941f3a90f
