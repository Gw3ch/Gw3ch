### Get the most repeated guest in a list of friends, but it will take precedence if a friend is already repeated.

"""
Dictionary for friend's guests
"""
friend_list = {}

friend_list["Manuel Arce"] = "Laura Rojas", "Rebeca Jara", "Olman Ulate", "Diana Sancho", "Teresa Oviedo", 
friend_list["Miguel Segura"] = "Mario Vargas", "Manuel Lopez", "Diego Solis", "Rebeca Jara",
friend_list["Adriana Fallas"] = "Olman Ulate", "Diego Sandi", "Sergio Romero", "Cristiano Ronaldo",
friend_list["Lorena Torres"] = "Luis Sandi", "Sergio Romero", "Laura Rojas", "Eduardo Ramos", "Oscar Moreno",
friend_list["Marianela Salazar"] = "Diego Calvo", "Diego Solis", "Mario Vargas", "Rebeca Jara",
friend_list["Rebeca Morera"] = "Oscar Maroto", "Lorena Torres", "Teresa Oviedo", "Rebeca Jara", "Oscar Ruiz",
friend_list["Luis Salas"] = "Teresa Oviedo", "Rebeca Jara", "Diego Fallas", "Olman Ulate", "Fabricio Ramirez",
friend_list["Oscar Ulate"] = "Mariapaz Vargas", "Mario Salazar", "Enrique Pena", "Diego Pais", "Cristiano Ronaldo"


"""
Extract the Friends name only
"""
# Extract the most repeated guest with precedence between lists.

# Lista de los amigos principales
list_hosts = []
# Lista para sacar most common item
list_all_names = []
# Lista para el most common item2
list_rest_names = []


for hosts in friend_list:
    # Print solo los hosts en strings por reglon
    #print(hosts)
    list_hosts.append(hosts)

    for guests in friend_list[hosts]:
        list_all_names.append(guests)

    most_common_item = max(list_all_names, key = list_all_names.count)
    rebeca = most_common_item

############# Testings ############
# Print rebeca que es el most_common_item en un reglon solo.
#print(rebeca)

# Print hasta hosts en data type:list[]
#print(list_hosts)

list_hosts.append(rebeca)

# Print de hosts + rebeca en data type:list[]
#print(list_hosts)


'''
Intento de descartar por condicionales pero no funciono
'''
    #if most_common_item in list(friend_list[hosts]):
    #    rebeca = (most_common_item)
    
'''
Si los condicinales sirvieron este seria el else y en vez de Adriana Fallas y Oscar Ulate
'''
rest_names = ["Adriana Fallas", "Oscar Ulate"]
for names2 in rest_names:    
    norebeca = (list(friend_list[names2]))
    for guests2 in norebeca:
        list_rest_names.append(guests2) 
    most_common_item2 = max(list_rest_names, key = list_rest_names.count)
    cristiano = most_common_item2 
list_hosts.append(cristiano)

inp = input("Desea ver la lista final de personas que van a asistir ? (Escriba SI o NO y luego presione 'Enter'): ")
if inp == "SI":
    print(list_hosts)
elif inp == "NO":
    print("Vuelva a ejecutar el programa y escriba SI, si desea ver la lista.")
else:
    print("Error!, ninguna opcion valida seleccionada, vuelva a ejecutar el programa y escriba SI o NO.")

############### Testing ############### 

#print(list(friend_list["Manuel Arce"]))

#for n in friend_list["Manuel Arce"]:
#    print(n[1])

#for n in friend_list["namelist"]:
 #   print(n)

#for n in friend_list["Miguel Segura"]

#for names in friend_list:
 #   value = list((friend_list[names]))
  #  print(value)

    


