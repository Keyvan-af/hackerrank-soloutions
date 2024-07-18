st = input()
st_lower = [s for s in st if s.islower()]
st_upper = [s for s in st if s.isupper()]
st_od = [s for s in st if s.isdigit() and int(s)%2 == 1]
st_ev = [s for s in st if s.isdigit() and int(s)%2 == 0]
print("".join(sorted(st_lower) + sorted(st_upper) + sorted(st_od) + sorted(st_ev)))