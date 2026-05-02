Python 's use:
1.see this command:
pip install foxange

2.use
foxange have many def
(1) input 's def:\n
  collect_input(*value) : return is list,can input big of one 's value
  like this: 
    command: print(collect_input("test1>","test2>"))
    run:
      test1> 0
      test2> 0
      ['0','0']
  input_to_file(*value,path,end='',sep="\n") : it don't have return value,it can inputed value add a file
  sanitize_input(text,*strings) : can del text 's *string str
(2) list_proce 's def:
  remove(value:list,condition=True) : can del don't is condition 's value
