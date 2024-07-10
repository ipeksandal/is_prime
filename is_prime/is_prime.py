def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True  # 2 asal bir sayıdır
    elif num % 2 == 0:
        return False  # Çift sayılar asal değildir (2 hariç)

    sqrt_num = int(num ** 0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False

    return True

test_numbers = [0, 1, 2, 3, 4, 5, 17, 25, 29, 31]
for number in test_numbers:
    if is_prime(number):
        print(f"{number} -> Asal sayı")
    else:
        print(f"{number} -> Asal değil")
test_number = int(input("Enter the number :"))
print(is_prime(test_number))
