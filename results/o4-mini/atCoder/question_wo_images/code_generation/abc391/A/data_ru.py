def main():
    # Считываем направление
    D = input().strip()
    
    # Отображение каждой буквы на противоположную
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    
    # Строим ответ путём замены каждой буквы
    result = ''.join(opposite[c] for c in D)
    
    # Выводим результат
    print(result)

if __name__ == "__main__":
    main()