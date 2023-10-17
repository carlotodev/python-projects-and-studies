segundos_str = input("Insira o número de segundos que deseja converter: ")
tempo_segs = int(segundos_str)

horas = tempo_segs // 3600
sobra = tempo_segs % 3600
total_min = sobra // 60
total_segs = sobra % 60
total_horas = horas % 24
total_dias = horas // 24

print(segundos_str, "equivale a", total_dias, "dia(s)", total_horas, "hora(s)", total_min, "minuto(s) e", total_segs, "segundo(s)")
