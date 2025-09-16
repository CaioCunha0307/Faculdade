# Leitura dos dados de início
dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(' : '))

# Leitura dos dados de fim
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(' : '))

# Conversão do tempo de início para segundos
total_segundos_inicio = (dia_inicio * 86400) + (hora_inicio * 3600) + \
                        (minuto_inicio * 60) + segundo_inicio

# Conversão do tempo de fim para segundos
total_segundos_fim = (dia_fim * 86400) + (hora_fim * 3600) + \
                     (minuto_fim * 60) + segundo_fim

# Cálculo da duração total em segundos
duracao_segundos = total_segundos_fim - total_segundos_inicio

# Conversão da duração total de volta para o formato D/H/M/S
dias = duracao_segundos // 86400
resto_segundos = duracao_segundos % 86400

horas = resto_segundos // 3600
resto_segundos = resto_segundos % 3600

minutos = resto_segundos // 60
segundos = resto_segundos % 60

# Impressão do resultado formatado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")