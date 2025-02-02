import pulp


limits = {"water": 100, "sugar": 50, "juice": 30, "pulp": 40}

fj = {"pulp": 2, "water": 1}
lemonade = {
    "water": 2,
    "sugar": 1,
    "juice": 1,
}

model = pulp.LpProblem("squeeze", pulp.LpMaximize)
juice_bottles = pulp.LpVariable("Juice", lowBound=0)
lemonade_bottles = pulp.LpVariable("Lemonade", lowBound=0)
model += (
    fj["water"] * juice_bottles + lemonade["water"] * lemonade_bottles
    <= limits["water"],
    "Water Limit",
)
model += lemonade["sugar"] * lemonade_bottles <= limits["sugar"], "Sugar Limit"
model += lemonade["juice"] * lemonade_bottles <= limits["juice"], "Juice Limit"
model += fj["pulp"] * juice_bottles <= limits["pulp"], "Pulp Limit"
model += juice_bottles + lemonade_bottles, "Maximize Drinks"
model.solve()
print(f"Juice bottles: {pulp.value(juice_bottles)}")
print(f"Lemonade bottles: {pulp.value(lemonade_bottles)}")
