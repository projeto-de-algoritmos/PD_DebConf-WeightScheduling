from event import include_weight, transform_type_in_value, find_best_schedule

def agenda_formatada(selected_day, data):
    print("______________________________________________________________________")
    print(f"    {selected_day}")
    print("______________________________________________________________________")
    print(f"    Hour    -   Activity ")
    print("______________________________________________________________________")
    for d in data:
        print(f"{d['horario_inicio']} - {d['horario_fim']} | {d['titulo']}")
    print("______________________________________________________________________")

def menu_choose_day(weight_event_type):
    while True:
        print(" ")
        print("______________________________________________________________________")
        print("     Escolha o dia de evento que você quer participar:")
        print("1. Monday")
        print("2. Tuesday")
        print("3. Wednesday")
        print("4. Thursday")
        print("5. Friday")
        print("6. Saturday")
        print("7. Sunday")
        print("0. Exit")

        choice = input("Selecione a opção equivalente de 0 a 7: ")

        if choice == '0':
            print("Saindo... Até mais!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            selected_day = days[int(choice) - 1]
            data_with_weight = include_weight(selected_day)
            final_data = transform_type_in_value(data_with_weight, weight_event_type)
            # find_best_schedule(final_data)
            agenda_formatada(selected_day, find_best_schedule(final_data))
            break
        else:
            print("Escolha inválida. Por favor escolha um número de 0 a 7.")

def menu_choose_weight():
    event_type = ['Long talk (45 minutes)', 'Short talk (20 minutes)', 'BoF (45 minutes)', 'Workshop (2h)', 'Other']
    print(" ")
    print("______________________________________________________________________")
    print("     Escolha qual tipo de evento você prefere:")

    weight_event_type = {}
    value = 25

    while event_type:
        for e, i in enumerate(event_type):
            print(f"{e} - {i}")
        
        n = len(event_type)
        choice = int(input("Selecione a opção equivalente de 0 a 4: "))
        if choice >= 0 and choice < n:
            choice = event_type.pop(choice)

            weight_event_type[choice] = value
            value = value - 5
        else:
            print(f"Escolha inválida. Por favor escolha um número de 0 a {n-1}.")

    return weight_event_type


def main():
    weight_event_type = menu_choose_weight()
    menu_choose_day(weight_event_type)

if __name__ == "__main__":
    main()