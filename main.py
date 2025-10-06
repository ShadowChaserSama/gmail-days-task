file = 'mbox-short.txt?utm_source=chatgpt.com'  # fayl adin

counts = {}
with open(file) as f:
    for line in f:
        if line.startswith('From '):
            parts = line.split()
            if len(parts) > 2:
                day = parts[2]  # gun adi (Mon, Tue, Wed, ...)
                counts[day] = counts.get(day, 0) + 1

# neticeleri cap et
for day, count in counts.items():
    print(day, count)
