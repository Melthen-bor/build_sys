import utils
import os
class lang_ext:
  def __init__(self,lang):
    self.lang=lang
    self.exts=[]
  def reg_ext(self,ext):
    self.exts+=[ext]
lang_exts=[]
def register_lang(lang):
  global lang_exts
  lang_exts+=[lang_ext(lang)]
def get_lang(lang):
  global lang_exts
  count=0
  while True:
    if lang_exts[count].lang==lang:
      return count
    count+=1
def use_gcc(lang,name,gl,libs):
  global lang_exts
  lib_arg=''
  if libs:
    lib_arg+=get_arguments(remove_ext(get_file_types(os.listdir(os.getcwd()+'\\li
  get_file_types(os.listdir(os.getcwd()+'\\src'),lang_exts[get_lang(lang)].exts)
  
