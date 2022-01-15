#%% breakpoint function
def breakpoint():
    while True:
        _dbg_input = input('> Input:\n')
        print('> Output:')
        if _dbg_input:
            try:
                exec(_dbg_input)
            except Exception as e: 
                print('> ERROR:', e)
        else:
            break
#%% function to printout variables and value
def vars():
    
    for v in sorted(dir(), key=lambda v: [str(type(eval(v))), v]):
        if not ( v.startswith('_dbg_') or v in ['vars', 'breakpoint']):
            print(v, end = '\t')
            print(eval(v), end = '\t')
            print(type(eval(v)))