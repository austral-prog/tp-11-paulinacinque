def read_file_to_dict(filename):
    ventas = {}			 
    try:
        with open(filename, "r") as archivo:           
            contenido = archivo.read()          
            lista_entradas = contenido.split(';')          
	
            for entrada in lista_entradas:     
                if entrada == '':
                    continue        
			
                producto, valor = entrada.split(':') 
                valor = float(valor)  
		
                if producto not in ventas:
                    ventas[producto] = [] 	       
                ventas[producto].append(valor)
		
        return ventas
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no existe")


def process_dict(data):
    for producto, lista in data.items():
        total = 0
        for valor in lista:
            total += valor
        promedio = total / len(lista)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
