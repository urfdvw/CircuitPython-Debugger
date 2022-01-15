"""
This library is for debugging a single file, code.py

currently able to
- debug line by line with indentions

todo
- breakpoints
- jump in and out of indentions
- function local variables
- white lines in the source code

"""

#%% function to printout variables and value
def vars():
    for v in dir():
        if not ( v.startswith('_dbg_') or v == 'vars'):
            print(v + ':\t' + str(locals()[v]))

#%% read 'code.py' as text
_dbg_code = []
_dbg_file = open('code.py', 'r')
_dbg_file.readline()
            
while True:
    _dbg_line_raw = _dbg_file.readline()
    if not _dbg_line_raw:
        break
    _dbg_code.append(_dbg_line_raw)
_dbg_file.close()

#%% read debug code snip
_dbg_file = open('./lib/debug_line.py', 'r')
_dbg_debugline = _dbg_file.read()
_dbg_file.close()

#%% combine original code and debug code
_dbg_code_out = ''

def _dbg_indent_lines(lines, n):
    return '\n'.join([' ' * n + l for l in lines.split('\n')])

for _dbg_i, _dbg_line in enumerate(_dbg_code):
    _dbg_indent = len(_dbg_line) - len(_dbg_line.lstrip())
    _dbg_code_out += _dbg_indent_lines('_dbg_i = ' + str(_dbg_i) + '\n' + _dbg_debugline, _dbg_indent) + '\n'
    _dbg_code_out += _dbg_line + '\n'

#%% start debugging
print('\n' * 3)
print('-' * 15, 'start debugging', '-' * 15)
print('Send empty string to run the current line.')
print('Send python command to debug.')
print('Send `vars()` to see variables')
print('\n' * 3)

# print(_dbg_code_out)

exec(_dbg_code_out)

#%% cancel running the original script
import sys
sys.exit()