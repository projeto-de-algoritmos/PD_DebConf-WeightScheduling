import json

class Event:
    def __init__(self, titulo, horario_inicio, horario_fim, tipo, valor):

        self.titulo = titulo
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.tipo = tipo
        self.valor = valor

    def as_dict(self):
        return {
            'titulo': self.titulo,
            'horario_inicio': self.horario_inicio,
            'horario_fim': self.horario_fim,
            'tipo': self.tipo,
            'valor': self.valor,
        }

def sort_by_finish_time(agenda):
    # Ordena eventos por ordem de término e transforma em dicionário
    event_objects = []
    for i in agenda:
        event_objects.append(Event(i['titulo'], i['horario_inicio'], i['horario_fim'], i['tipo'], i['valor']))

    sorted_events = sorted(event_objects, key=lambda event: event.horario_fim)
    sorted_events_as_dicts = [event.as_dict() for event in sorted_events]
    
    return sorted_events_as_dicts

def find_best_schedule(agenda):
    # Encontra os melhores horário levendo em consideração o valor de cada atividade e o menor tempo de ócio
    sorted_events = sort_by_finish_time(agenda)
    best_programming = []
    n = len(sorted_events)
    dp = [0] * n

    for i in range(n):
        current_weight = sorted_events[i]['valor']
        without_current = dp[i-1] if i-1 >= 0 else 0
        compatible_activities = [dp[j] + current_weight for j in range(i) if sorted_events[j]['horario_fim'] <= sorted_events[i]['horario_inicio']]
        if compatible_activities:
            dp[i] = max(compatible_activities)
        else:
            dp[i] = max(current_weight, without_current)

    best_programming = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            print(sorted_events[i]['valor'])
            best_programming.append(sorted_events[i])
            i -= 2
        else:
            i -= 1
    return list(reversed(best_programming))

def get_data(day):
    with open('./schedule.json', 'r') as fp:
        data_json = json.load(fp)
    return data_json[day]
    
def get_weight():
    with open('./events.json', 'r') as fp:
        data_type = json.load(fp)
    return data_type

def include_weight(day):
    data_day = get_data(day)
    data_type = get_weight()
    for data in data_day:
        title = data['titulo']
        for types in data_type:
            if types['titulo'] == title:
                data['tipo'] = types['tipo']
    return data_day

def transform_type_in_value(data_with_weight, weight_event_type):
    print(data_with_weight)
    print(weight_event_type)
    for data in data_with_weight:
        data['valor'] = weight_event_type[data['tipo']]
    return data_with_weight

