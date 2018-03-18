
total_time=0

for h in range(24):
    for m in range(60):
        if '3' in str(h) or '3' in str(m):
            total_time+=60

print(total_time)        
