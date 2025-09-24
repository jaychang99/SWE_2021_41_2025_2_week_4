def isHappy(n):
    def get_next(num): 
        total = 0 
        while num > 0:  
            digit = num % 10 
            total += digit * digit 
            num //= 10 
        return total 

    seen = set() 
    while n != 1 and n not in seen:  
        seen.add(n) 
        n = get_next(n) 

    return n == 1 

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)

  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")

  print("Results saved to /app/bind_mount/output.txt")