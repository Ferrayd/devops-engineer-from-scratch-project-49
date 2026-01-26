### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ferrayd/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Ferrayd/devops-engineer-from-scratch-project-49/actions)

# Brain Games

Серия математических головоломок для тренировки мозга.

## Описание

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

1. Калькулятор. Арифметические выражения, которые необходимо вычислить
2. Прогрессия. Поиск пропущенных чисел в последовательности чисел
3. Определение четного числа
4. Определение наибольшего общего делителя
5. Определение простого числа

## Установка
make build
make package-install

## Игры

### 1. Brain Even — Проверка на чётность

Определите, является ли число четным или нечетным.

**Запуск:**
brain-even

[![asciicast](https://asciinema.org/a/8iPpqECdpk9RCeMd.svg)](https://asciinema.org/a/8iPpqECdpk9RCeMd)

Пример вывода (победа)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!

Пример вывода (поражение)

Welcome to the Brain Games!
May I have your name? Bill
Hello, Bill!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!

---

### 2. Brain Calc — Калькулятор

Вычислите результат случайного математического выражения (сложение, вычитание, умножение).

**Запуск:**
brain-calc

[![asciicast](https://asciinema.org/a/MUG6A1oNQOmnx0w1.svg)](https://asciinema.org/a/MUG6A1oNQOmnx0w1)

Пример вывода (победа)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!

Пример вывода (поражение)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Sam!

---

### 3. Brain GCD — Наибольший общий делитель

Найдите наибольший общий делитель двух чисел.

**Запуск:**
brain-gcd

[![asciicast](https://asciinema.org/a/VHv0qy2gntuoZG1Y.svg)](https://asciinema.org/a/VHv0qy2gntuoZG1Y)

Пример вывода (победа)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!

Пример вывода (поражение)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!

---

### 4. Brain Progression — Арифметическая прогрессия

Найдите пропущенное число в арифметической прогрессии.

**Запуск:**
brain-progression

[![asciicast](https://asciinema.org/a/j4Rao0ActGpB4HjW.svg)](https://asciinema.org/a/j4Rao0ActGpB4HjW)

Пример вывода (победа)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!

Пример вывода (поражение)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 1
'1' is wrong answer ;(. Correct answer was '15'.
Let's try again, Sam!

---

### 5. Brain Prime — Простое ли число?

Определите, является ли число простым.

**Запуск:**
brain-prime

[![asciicast](https://asciinema.org/a/p5oE4aN2b0I3OJ8d.svg)](https://asciinema.org/a/p5oE4aN2b0I3OJ8d)

Пример вывода (победа)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
Question: 10
Your answer: no
Correct!
Question: 13
Your answer: yes
Correct!
Congratulations, Sam!

Пример вывода (поражение)

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: no
'no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, Sam!