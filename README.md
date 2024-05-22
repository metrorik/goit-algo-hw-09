# Видача решти

Цей проєкт надає два алгоритми для вирішення проблеми видачі решти, використовуючи набір монет [50, 25, 10, 5, 2, 1].

## Алгоритми

### Жадібний алгоритм
Жадібний алгоритм спочатку вибирає найбільший номінал і рухається вниз. Він є ефективним за часовою складністю \(O(n)\), алгоритм може швидко видавати решту навіть для великих сум, але не завжди гарантує мінімальну кількість монет. Якщо набір монет не містить всіх можливих номіналів, алгоритм може не знайти оптимальне рішення.

### Динамічне програмування
Алгоритм динамічного програмування гарантує оптимальне рішення, досліджуючи всі можливі способи видачі решти. Він має часову складність \(O(n \times m)\) і використовує більше пам'яті, що робить його менш ефективним для великих сум. Але він є більш ефективним для складних наборів монет, де жадібний алгоритм може не знайти оптимальне рішення.

## Використання
Обидва алгоритми реалізовані на Python. Приклади їх використання наведені в коді.

## Порівняння ефективності
- **Жадібний алгоритм:** швидший, але може бути не оптимальним.
- **Динамічне програмування:** гарантує оптимальне рішення, але повільніший і використовує більше пам'яті.