import requests

# Прокси с логином и паролем для HTTPS и SOCKS5
http_proxy = "http://wO9GA4Rpdn:qHwPC4VGQo@78.153.143.229:23440"
socks5_proxy = "socks5://wO9GA4Rpdn:qHwPC4VGQo@78.153.143.229:23440"  # замените на SOCKS порт, если он доступен

# Используем прокси для HTTPS-запроса
proxies = {
    "http": http_proxy,
    "https": http_proxy,  # или используйте socks5_proxy, если хотите проверить SOCKS
}

try:
    # Запрос на сайт для проверки IP
    response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
    print("IP через прокси:", response.text)
except requests.exceptions.ProxyError as e:
    print("Ошибка прокси:", e)
except requests.exceptions.Timeout as e:
    print("Таймаут:", e)
except Exception as e:
    print("Неизвестная ошибка:", e)
