file = 'f.txt'
counts = {}

with open(file) as f:
    for line in f:
        if line.startswith('From '):
            parts = line.split()
            if len(parts) > 1:
                sender = parts[1]  # göndəricinin email ünvanı
                counts[sender] = counts.get(sender, 0) + 1

for sender, count in counts.items():
    print(sender, count)
