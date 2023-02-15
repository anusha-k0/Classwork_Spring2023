def error_function():
    a = '1'
    b = 2
    try: 
        c = a+b
    except TypeError:
        a = int(a)
        c = a+b 
    return c
    
def main():
    c = error_function()
    print(c)
        
if __name__ == '__main__':
    main()