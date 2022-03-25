def asteroidCollision(asteroids):
  stack = [asteroids[0]]

  for asteroid in asteroids[1::]:
    keep = True # flag to decide whether we keep the left moving asteroid or not after collisions are over
    while stack and stack[0] > 0 and asteroid < 0: # while stack isn't empty & asteroids collide
      if stack[0] == abs(asteroid): # if colliding asteroids are the same size, destroy both
        stack.pop(0)
        keep = False
        break
      elif stack[0] < abs(asteroid): # if asteroid moving left is larger than asteroid moving right, destroy asteroid in stack
        stack.pop(0)
        keep = True
      else: # if asteroid moving left is smaller than asteroid moving right, destroy current asteroid
        keep = False
        break

    if keep == True:
      stack.insert(0, asteroid)

  return(stack[::-1])

# asteroidCollision([5,10,-5,-14])
# asteroidCollision([10,2,-5])
asteroidCollision([8,8,-8,-8])
# asteroidCollision([-2,-1,1,2])
asteroidCollision([-2,-2,1,-2])