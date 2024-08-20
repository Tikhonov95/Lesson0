def find_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
password = find_password(n)
print(f"Нужный пароль: {password}")