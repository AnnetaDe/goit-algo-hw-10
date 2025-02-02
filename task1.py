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


# Ініціалізація моделі2
model2 = pulp.LpProblem("Maximize Beverage Production", pulp.LpMaximize)
# Змінні
Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")
Juice = pulp.LpVariable("Juice", lowBound=0, cat="Continuous")
# Обмеження ресурсів
model2 += 2 * Lemonade + 1 * Juice <= 100  # Вода
model2 += 1 * Lemonade <= 50  # Цукор
model2 += 1 * Lemonade <= 30  # Лимонний сік
model2 += 2 * Juice <= 40  # Фруктове пюре
# Функція максимізації виробництва
model2 += Lemonade + Juice
# Розв'язання задачі
model2.solve()
# Виведення результатів
print("Виробити 'Лимонаду':", Lemonade.varValue)
print("Виробити 'Фруктового соку':", Juice.varValue)
