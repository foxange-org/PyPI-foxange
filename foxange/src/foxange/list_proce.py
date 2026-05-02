def remove(value:list,condition=True)->list:
    return_list:list = []
    for _ in value:
        if not condition(_):
            return_list.append(_)
    return return_list

if __name__ == "__main__":
    print("this is a test this file 's def , if you want use , no open the file,use from foxange import list_proce")
    print("down is tset:")
    
    print("remove:value->[[1,2,3,4,5],lambda x:x%2==0]")
    print("return value:", remove([1,2,3,4,5],lambda x:x%2==0))