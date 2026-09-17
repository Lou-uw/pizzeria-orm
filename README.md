# Pizzería - TP Integrador ORM

## Integrantes
- Lourdes Soto, Alba Condori

## Caso Elegido: Caso D — Pizzeria / Restaurante
Sistema de gestión de pedidos, clientes, productos y repartidores.

## Estructura del proyecto
- `schema.py`: Modelos y creación de las tablas SQLite.
- `seed.py`: Carga de datos de prueba en la base de datos.
- `consultas.py`: Consultas requeridas con SQLAlchemy.

## Instrucciones para correr el codigo

1. Instalar los paquetes correspondientes
sudo apt update
sudo apt install python3-venv python3-full

2. Activar el entorno virtual 
source venv/bin/activate

3. Instalar SQLALchemy
pip install sqlalchemy

4. Ejecutar las consultas 
python consultas.py

### Solución de posibles errores
1. Eliminar el archivo de la base de datos local:
rm restaurante.db

2. Recrear la base de datos y las tablas:
python schema.py

3. Volver a cargar los datos de prueba:
python seed.py

4. Correr las consultas nuevamente:
python consultas.py

Gracias por ver. 