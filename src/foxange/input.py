from pathlib import Path

def collect_input(*value)->list:
    return_value = list()
    for input_text in value:
        temp:str = str(input(input_text))
        return_value.append(temp)
    return return_value

def input_to_file(*value,path,mode='w',end='',sep="\n")->None:
    all_input_value:str = ""
    for input_value in value:
        all_input_value += input_value + sep
    all_input_value+=end
    with open(path,mode) as f:
        f.write(all_input_value)

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

def choice_input(title,value:list,input_text:str)->list:
    print(title)
    temp = 1
    for _ in value:
        print(f"{temp}.{_}")
    string = input(input_text)
    if string.isdigit():
        if string in value:
            return [value.index(string),string]
        else : return [None,None]
    else :
        return [int(string),value[string]]

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
    
    print("test input_to_file: value->['hello','foxange',path='test']")
    print("return 's value(path:test):no return")
    input_to_file("hello","foxange",path='test.txt')
    
    print("test sanitize_input: value->['hello','e','o']",flush=True)
    print("return 's value(path:cmd):",sanitize_input("hello",'e','o'))
    
    print("test numeric_input:value -> ['test>',10,20]")
    print("return 's value(path:cmd):",numeric_input("test>",10,20))
