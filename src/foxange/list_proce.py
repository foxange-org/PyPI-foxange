def remove(value:list,condition=None)->list:
    return_list:list = []
    for _ in value:
        if condition is None:
            return_list.append(_)
        elif not condition(_):
            return_list.append(_)
    return return_list

def unique(value:list):
    seen = set()
    result = []
    for item in value:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def rotate(value:list,inx:int)->list:
    n = len(value)
    shift = inx % n
    return value[-shift:] + value[:-shift] if shift != 0 else value[:]

def spread(*args):
    result = []
    for arg in args:
        if isinstance(arg, (list, tuple)):
            result.extend(arg)
        else:
            result.append(arg)
    return tuple(result)

if __name__ == "__main__":
    print("this is a test this file 's def , if you want use , no open the file,use from foxange import list_proce")
    print("down is tset:")
    
    print("remove:value->[[1,2,3,4,5],lambda x:x%2==0]")
    print("return value:", remove([1,2,3,4,5],lambda x:x%2==0))