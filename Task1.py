#1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
#необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
#значений необходимо запускать скрипт с параметрами.

salary = float(input("Введите размер почасового оклада: "))
hours = float(input("Введите количество отработанных часов: "))
bonus = float(input("Введите величину премии: "))

def payday():
    try:

        pay = salary * hours + bonus
        print(f"Зарплата составила: {pay}")
    except ValueError:
        return print("Произошла чудовищная ошибка! Значения не считаются.")
payday()
