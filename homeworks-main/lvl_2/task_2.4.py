# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
  s = s.replace('!','')
  return s


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
  if s[-1] == '!':
    s = s[:-1]
    return s
  else:
    return s


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
  s_list = s.split(' ')
  s_list_out = []
  for i in s_list:
    L = 0
    for j in i:
      if j == '!':
        L += 1
    if L != 1:
      s_list_out.append(i)
  return ' '.join(s_list_out)

A1 = remove_exclamation_marks("Hi! Hello!")
print('A1 ->', A1)
A2 = remove_exclamation_marks("")
print('A2 ->', A2)
A3 = remove_exclamation_marks("Oh, no!!!")
print('A3 ->', A3)

B1 = remove_last_em("Hi!")
print('B1 ->', B1)
B2 = remove_last_em("Hi!!!")
print('B2 ->', B2)
B3 = remove_last_em("!Hi")
print('B3 ->', B3)

C1 = remove_word_with_one_em("Hi!")
print('C1 ->', C1)
C2 = remove_word_with_one_em("Hi! Hi!")
print('C2 ->', C2)
C3 = remove_word_with_one_em("Hi! Hi! Hi!")
print('C3 ->', C3)
C4 = remove_word_with_one_em("Hi Hi! Hi!")
print('C4 ->', C4)
C5 = remove_word_with_one_em("Hi! !Hi Hi!")
print('C5 ->', C5)
C6 = remove_word_with_one_em("Hi! Hi!! Hi!")
print('C6 ->', C6)
C7 = remove_word_with_one_em("Hi! !Hi! Hi!")
print('C7 ->', C7)

# В пункте C сделал покороче
def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])
