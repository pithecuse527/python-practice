def hanoi_tower(n,org,tmp,to):
    if (n==1):
        print("원판 1을",org,"에서",to,"로 옮긴다.")
    else:
        hanoi_tower(n-1, org, to, tmp)
        print("원판",n,"을",org,"에서",to,"로 옮긴다.")
        hanoi_tower(n-1, tmp, org, to)

hanoi_tower(64, 'A', 'B', 'C')
