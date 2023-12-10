from iperf import client, parser

def test_iperf():
    server_ip = '192.168.103.10'
    
    # Викликаємо функцію client для отримання результатів тесту
    result, error = client(server_ip)
    
    # Перевірка наявності помилок при виконанні тесту
    assert error is None, f"Помилка при виконанні iperf тесту: {error}"

    # Вивід результатів тесту
    print("Результати iperf тесту:")
    print(result)

    # Викликаємо функцію parser для обробки виводу та отримання інтервалів
    result_list = parser(result)

    # Перевірка наявності інтервалів
    assert result_list, "Не знайдено інтервалів у виводі iperf тесту"

    # Перевірка, чи інтервали задовольняють умови
    for value in result_list:
        assert value['Transfer'] > 2 and value['Bitrate'] > 20, f"Не виконані умови для інтервалу: {value}"

# Виклик тесту
test_iperf()
