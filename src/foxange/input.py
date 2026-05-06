from pathlib import Path

def collect_input(*value)->list:
    return_value = list()
    for input_text in value:
        temp:str = str(input(input_text))
        return_value.append(temp)
    return return_value

def sanitize_input(text,*strings)->str:
    for string in strings:
        text = text.replace(string, "")
    return text

def numeric_input(text,min,max,notvalid=None):
    string = input(text)
    size = len(string)    
    if size>=min and size<=max:
        return string
    else:
        return notvalid

def choice_input(title, value: list, input_text: str) -> list:
    print(title)
    for idx, opt in enumerate(value, start=1):
        print(f"{idx}. {opt}")
    user_input = input(input_text)
    if user_input.isdigit():
        idx = int(user_input) - 1
        if 0 <= idx < len(value):
            return [idx, value[idx]]
    else:
        if user_input in value:
            idx = value.index(user_input)
            return [idx, user_input]
    return [None, None]

def confirm(text,yes_str:list=["yes"],no_str:list=["no"]):
    string = input(text+f"[{yes_str[0]}/{no_str[0]}]")
    if string in yes_str :
        return True
    elif string in no_str:
        return False
    else :
        return None

if __name__ == "__main__":
    print("this is test the input.py's def ,if you want use input.py work,no open this the file,from foxange import input")
    print("down is test input.py 's def ...")
    print("i will print can return value 's def 's value and return 's path...")
    
    print("test collect_input: value->[test1>,test2>]")
    print("return 's value(path:cmd):",collect_input("test1>","test2>"))
    
    # print("test input_to_file: value->['hello','foxange',path='test']")
    # print("return 's value(path:test):no return")
    # input_to_file("hello","foxange",path='test.txt')
    
    print("test sanitize_input: value->['hello','e','o']",flush=True)
    print("return 's value(path:cmd):",sanitize_input("hello",'e','o'))
    
    print("test numeric_input:value -> ['test>',10,20]")
    print("return 's value(path:cmd):",numeric_input("test>",10,20))
