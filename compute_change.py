def compute_change(amount):
    # Convert dollars to cents to avoid floating-point issues
    cents = round(amount * 100)

    values = [
        ("$100", 10000),
        ("$50", 5000),
        ("$20", 2000),
        ("$10", 1000),
        ("$5", 500),
        ("$1", 100),
        ("Quarter", 25),
        ("Dime", 10),
        ("Nickel", 5),
        ("Penny", 1),
    ]

    for name, value in values:
        count = cents // value
        if count > 0:
            print(f"{name}: {count}")
        cents %= value

print(compute_change(186.41))
print("$186.41")
print("-------------")
print(compute_change(37.89))
print("37.89")
