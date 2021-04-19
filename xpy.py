# xpy
# https://github.com/Decimation/Nspire-Library
# Author: Read Stanton
# based off of eval_expr by Adrien "Adriweb" Bertrand
# https://github.com/TI-Planet/eval_expr

# Useful for eval
from math import sqrt, pi, e
from ti_system import * 

# Internal helper functions....
def _try_parse_num(s):
  try:
    f = float(s)
    return int(f) if int(f) == f else f
  except ValueError:
    return s

def _try_eval(thing):
  try:
    return eval("("+str(thing)+")")
  except:
    return thing

def _cleanstr(res):
  res = res[1:-1]  # to remove the quotes
  res = res.replace("*\uf02f", "j")  # complex i
  res = res.replace("\uf02f", "j")  # complex i
  res = res.replace("\u221a", "sqrt")
  res = res.replace("\u03c0", "pi")
  res = res.replace("\uf03f", "e")
  res = _try_parse_num(res)  # auto type...
  return res

# Public functions
def eval_expr(expr, trypyeval=False):
  TMP = "tmppy_"
  os_write(TMP, 'strsub(string('+str(expr)+'),"/","$%$")')  # eval and store
  res = os_read(TMP)  # retrieve stored value
  res = res.replace("$%$", "/")  # magic replacement
  res = _cleanstr(res)
  if trypyeval == True:
    res = _try_eval(res)
  return res

def call_func(funcname, *pyargs):
  fargs = ','.join(map(str, pyargs))
  expr = funcname + '(' + fargs + ')'
  res = eval_expr(expr)
  return res if res != expr else None
  
def eval_expr2(name):
  return _cleanstr(readST("string("+name+")"))
  
#def eval_expr2(name):
#  return _cleanstr(call_func('string',name))

def os_read(name):
  res = readST(name)
  return res

def os_write(name, val):
  writeST(name, val)

# Aliases for compat with other stuff
caseval = eval_expr
eval_native = eval_expr
