import hashlib

def crack(hash):
    
    for i in range(100000):
        
        pin = str(i).zfill(5)
      
        pin_hash = hashlib.md5(pin.encode()).hexdigest()
       
        if pin_hash == hash:
            return pin
