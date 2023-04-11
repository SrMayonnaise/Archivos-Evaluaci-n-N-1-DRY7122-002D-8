import json

with open("/home/devasc/labs/devnet-src/parsing/myfile.json", "r") as json_file:
    ourjson = json.load(json_file)

token = ourjson["token"]
print("Token :", token)

tiempo_restante = ourjson["tiempo_restante"]
print("Tiempo restante: ", tiempo_restante, "segundos")

token_reserva = ourjson["token_reserva"]
print("Token :", token)

tiempo_reserva = ourjson["tiempo_reserva"]
print("Tiempo restante: ", tiempo_restante, "segundos")
