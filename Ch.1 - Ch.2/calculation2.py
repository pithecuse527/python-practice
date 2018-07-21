def calVolume(r):
    PI = 3.141592
    volume = (4.0 / 3.0) * (PI * r**3)

    print(volume)

def lightToPC():                # PC = Proxima Centauri
    PC_DISTANCE = 40 * 10**12
    LIGHT_SPEED = 300000        # light speed unit => 'km/sec'

    secs = PC_DISTANCE / LIGHT_SPEED
    light_year = secs / (60.0 * 60.0 * 24.0 * 365.0)
    print(light_year)

def voyagerToPC():
    PC_DISTANCE = 40 * 10**12
    VOYAGER_SPEED = 6 * 10**4   # voyager speed unit => 'km/h'
    
    hour = PC_DISTANCE / VOYAGER_SPEED
    print(hour)
    

calVolume(5.0)
lightToPC()
voyagerToPC()

