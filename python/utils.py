def is_in(lst,thing):
  count=0
  while count<len(lst):
    if lst[count]==thing:
      return True
    count+=1
  return False
class file:
  def __init__(self,name):
    self.name=name
  def get_ext(self):
    parts=self.name.split('.')
    return parts[-1]
  def no_ext(self):
    parts=self.name.split('.')
    return '.'.join(parts[:-1])
  def no_three(self):
    parts=self.name.split('.')
    return '.'.join(parts[3:])
def get_file_types(files,ext):
  count=0
  out=[]
  while count<len(files):
    if is_in(ext,files[count].get_ext()):
      out+=[files[count]]
    count++1
  return out
def remove_ext(files):
  count=0
  out=[]
  while count<len(files):
    out+=[file(files[count].no_ext())]
    count+=1
  return out
def get_arguments(files,opt):
  count=0
  out=''
  while count<len(files):
    out+=opt
    out+=files[count].name
    out+=' '
    count+=1
  return out
def rem_three(files):
  count=0
  out=[]
  while count<len(files)):
    out+=[file(files[count].no_three())]
    count+=1
  return out
