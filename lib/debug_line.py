print('v' * 30 + '\n' + str(_dbg_i + 2) + '\t' + _dbg_code[_dbg_i] + ('' if _dbg_code[_dbg_i].endswith('\n') else '\n') + '^' * 30)
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
            