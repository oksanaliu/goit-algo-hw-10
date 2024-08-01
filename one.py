import pulp

# Створення проблеми максимізації
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість Лимонаду
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі: максимізувати загальну кількість вироблених продуктів
prob += x + y, "Total_Products"

# Обмеження ресурсів
prob += 2*x + 1*y <= 100, "Water"
prob += 1*x <= 50, "Sugar"
prob += 1*x <= 30, "Lemon_Juice"
prob += 2*y <= 40, "Fruit_Puree"

# Розв'язання проблеми
prob.solve()

# Виведення результатів
print("Статус розв'язання:", pulp.LpStatus[prob.status])
print("Кількість Лимонаду:", pulp.value(x))
print("Кількість Фруктового соку:", pulp.value(y))
print("Максимальна загальна кількість продуктів:", pulp.value(prob.objective))