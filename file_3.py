md = {
    "Stockholm": ["shitty place", "dirty"],
    "Göteborg": ["people talk funny", "less dirty"],
}

for i, j in md.items():
    print(f" People will say this about {i}")
    for q in j:
        print(f"it is very {q} there")
