def isValid(s):
  stack = []

  for i in s:
    if i == '(' or i == '{' or i == '[':
      stack.append(i)
    
    if i == ')' or i == '}' or i == ']':
      if not stack:
        return False
      char = stack.pop()
      if i == ')' and char != '(' or i == '}' and char != '{' or i == ']' and char != '[':
        return False
  
  if stack:
    return False
  else:
    return True

print(isValid('[{{[}}]'))