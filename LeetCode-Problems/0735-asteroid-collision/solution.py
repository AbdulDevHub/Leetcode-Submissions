class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        while stack and stack[-1] > 0 and asteroid < 0:
            diff = stack[-1] + asteroid

            # Current asteroid is bigger: destroy stack top, keep checking loop
            if diff < 0: stack.pop()
            # Stack top is bigger: destroy current asteroid, stop loop
            elif diff > 0: break
            # Both are equal size: destroy both, stop loop
            else:
                stack.pop()
                break
      
        # Executed ONLY if the loop completed without a 'break'
        # (incoming asteroid survived all collisions or no collision occurred)
        else: stack.append(asteroid)
    return stack
