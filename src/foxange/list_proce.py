def remove(value:list,condition=True)->list:
    return_list:list = []
    for _ in value:
        if not condition(_):
            return_list.append(_)
    return return_list

def unique(value:list):
    list_return = []
    for i in value:
        if not list_return.find(i):
            list_return.append(i)
    return list_return

def rotate(value:list,inx:int)->list:
    n = len(value)
    shift = inx % n
    return value[-shift:] + value[:-shift] if shift != 0 else value[:]

if __name__ == "__main__":
    print("this is a test this file 's def , if you want use , no open the file,use from foxange import list_proce")
    print("down is tset:")
    
    print("remove:value->[[1,2,3,4,5],lambda x:x%2==0]")
    print("return value:", remove([1,2,3,4,5],lambda x:x%2==0))