def add_time(start, duration,day_week='None'):

  s1 = start
  s2 = duration
  dw = day_week.lower()

  sf1 = s1.split(sep=' ')
  sf2 = s2.split(sep=' ')
  
  n1 = sf1[0].split(sep=':')
  n2 = sf2[0].split(sep=':')

  hour = int(n1[0]) + int(n2[0])
  minu = int (n1[1]) + int(n2[1])
  
  if sf1[1] == 'PM':
    hour = hour + 12
  
  nm = 0
  nt = 0

  if minu > 60:
    nm = minu //60
    minu = minu -nm*60 
    hour += nm

  if hour > 24:
    nt = hour // 24
    hour = hour - nt*24    

  if hour == 0:
    ht = 12
  else:
    ht = hour
  
  if hour > 12:
    ht = ht - 12
  
  if minu > 10:
    new_time = str(ht) +':'+ str (minu)

  if minu <10:
    new_time = str(ht) +':0'+ str (minu)

  if hour//12 > 0:
    new_time += ' PM'
  else:
    new_time += ' AM'

  days = 0

  for i in range(0,nt):
    days += 1
  
  if dw != 'none':
    lst_dw = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    li = lst_dw.index(dw)
    ki = li + int(days)
    if ki >= 7:
      nw = ki//7
      ki = ki - nw*7
    
    new_time += ', ' + lst_dw[ki].capitalize()

  if days != 0:
    if days == 1:
      new_time += ' (next day)'
    if days >= 2:
      new_time += ' (' + str(days) + ' days later)' 

  return new_time