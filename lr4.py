import datetime


def main():
    name = input("Название лекарства: ")
    scheduled_time_str = input("Запланированное время (ЧЧ:ММ): ")
    method = input("Способ применения (до еды/после еды/независимо): ").lower()
    frequency = input("Частота (один раз/каждые X часов): ").lower()

    scheduled_time = datetime.datetime.strptime(scheduled_time_str, "%H:%M").time()
    now = datetime.datetime.now()
    current_time = now.time()
    today = now.date()

    # Обработка однократного приема
    if frequency == "один раз":
        # Правило для однократного приема
        scheduled_dt = datetime.datetime.combine(today, scheduled_time)

        # Проверка необходимости сдвига времени для "после еды"
        if method == "после еды":
            scheduled_dt += datetime.timedelta(minutes=30)
            scheduled_time = scheduled_dt.time()  # Обновляем время

        # Если текущее время >= запланированного
        if current_time >= scheduled_time:
            print(f"Напоминание: Примите {name} в {scheduled_time.strftime('%H:%M')} {method}.")
        else:
            print(f"Напоминание сработает в {scheduled_time.strftime('%H:%M')}.")

    # Обработка периодического приема (без изменений)
    elif "каждые" in frequency:
        hours = int(frequency.split()[-1])
        next_time = datetime.datetime.combine(today, scheduled_time) + datetime.timedelta(hours=hours)
        print(f"Следующее напоминание для {name}: {next_time.strftime('%H:%M')}.")

    else:
        pass


if __name__ == "__main__":
    main()