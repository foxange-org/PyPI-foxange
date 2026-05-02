from pathlib import Path

def collect_input(*value)->list:
    return_value = list()
    for input_text in value:
        temp:str = str(input(input_text))
        return_value.append(temp)
    return return_value

def input_to_file(*value,path,end='',sep="\n")->None:
    all_input_value:str = ""
    for input_value in value:
        all_input_value += input_value + sep
    all_input_value+=end
    with open(path,"w") as f:
        f.write(all_input_value)

def sanitize_input(text,*strings)->str:
    for string in strings:
        text = text.replace(string, "")
    return text

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
