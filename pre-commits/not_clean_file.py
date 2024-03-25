
def bad_function (x, y ):  
  result = x+y
 return result

def another_bad_function():  
    x = 10
  y = 20
  return x + y


def main():
    print(bad_function(10, 20))
    print(another_bad_function())

if __name__ == "__main__":
    main()