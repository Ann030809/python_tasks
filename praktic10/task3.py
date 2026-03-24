def print_case_counts(s:str):
   U = 0
   L = 0
   for i in range(len(s)):
      if s[i].isupper():
         U += 1
      else :
         L += 1 
   print(f'Букв в вернем регистре {U}')
   print(f'Букв в нижнем регистре {L}')
print_case_counts(input())