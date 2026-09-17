from sqlalchemy.orm import Session 
from schema import engine, Cliente, Producto, Repartidor, Pedido 

with Session(engine) as session:
    # 10 Clientes
    clientes = [
        Cliente(nombre="Juan", apellido="Sanchez", telefono="1156854433", direccion="Av. Corrientes 4400"),
        Cliente(nombre="Dylan", apellido="Rosas", telefono="1107432675", direccion="Av. Saenz 3557"),
        Cliente(nombre="Samuel", apellido="Huallpa", telefono="1104940367", direccion="Cosquin 1222"),
        Cliente(nombre="Camila", apellido="Cori", telefono="1128384844", direccion="Cañada de Gomez 23"),
        Cliente(nombre="Milena", apellido="Fonceca", telefono="1182982349", direccion="Ferre 670"),
        Cliente(nombre="Lucas", apellido="Gomez", telefono="1134567890", direccion="Av. Rivadavia 1200"),
        Cliente(nombre="Maria", apellido="Lopez", telefono="1198765432", direccion="Belgrano 450"),
        Cliente(nombre="Sofia", apellido="Perez", telefono="1155443322", direccion="San Martin 890"),
        Cliente(nombre="Mateo", apellido="Diaz", telefono="1166778899", direccion="Lavalle 1500"),
        Cliente(nombre="Lucia", apellido="Torres", telefono="1122334455", direccion="Pueyrredon 300")
    ]

    # 10 Productos (variedad de activos/inactivos)
    productos = [ 
        Producto(nombre="Pizza calabresa", descripcion="Salsa de tomate, calabresa, mozzarella y oregano", precio=15000, activo=True),
        Producto(nombre="Pizza pepperoni", descripcion="Salsa de tomate, pepperoni, mozzarella y oregano", precio=12000, activo=True),
        Producto(nombre="Pizza jamon y queso", descripcion="Salsa de tomate, jamon, mozzarella y oregano", precio=11000, activo=False),
        Producto(nombre="Pizza pollo catupiry", descripcion="Salsa de tomate, pollo, catupiry, mozzarella y oregano", precio=17000, activo=True),
        Producto(nombre="Papas fritas", descripcion="Porcion de papas fritas con bacon y cheddar", precio=10000, activo=True),
        Producto(nombre="Pizza fugazzeta", descripcion="Mozzarella y cebolla", precio=13000, activo=True),
        Producto(nombre="Pizza napolitana", descripcion="Salsa, mozzarella, tomate en rodajas y ajo", precio=14000, activo=True),
        Producto(nombre="Empanada de carne", descripcion="Empanada cortada a cuchillo", precio=2000, activo=True),
        Producto(nombre="Empanada de jamon y queso", descripcion="Rellena de jamon y queso", precio=1800, activo=False),
        Producto(nombre="Gaseosa 1.5L", descripcion="Gaseosa Coca-Cola", precio=3500, activo=True)
    ] 

    # 10 Repartidores (variedad de activos/inactivos)
    repartidores = [
        Repartidor(nombre="Lucas", apellido="Cabanias", activo=True),
        Repartidor(nombre="Rolando", apellido="Cabanias", activo=False),
        Repartidor(nombre="Natalia", apellido="Cabanias", activo=True),
        Repartidor(nombre="Ricardo", apellido="Cabanias", activo=False),
        Repartidor(nombre="Aurora", apellido="Villa", activo=False),
        Repartidor(nombre="Carlos", apellido="Gimenez", activo=True),
        Repartidor(nombre="Esteban", apellido="Quito", activo=True),
        Repartidor(nombre="Mariana", apellido="Rios", activo=False),
        Repartidor(nombre="Gonzalo", apellido="Morales", activo=True),
        Repartidor(nombre="Valeria", apellido="Sosa", activo=True)
    ]

    # 10 Pedidos (nombres corregidos: cliente_id y repartidor_id)
    pedidos = [
        Pedido(fecha="2026-03-01", total=27000, estado="Entregado", cliente_id=1, repartidor_id=3),
        Pedido(fecha="2026-03-01", total=12000, estado="Entregado", cliente_id=2, repartidor_id=1),
        Pedido(fecha="2026-03-02", total=15000, estado="Entregado", cliente_id=3, repartidor_id=3),
        Pedido(fecha="2026-03-02", total=17000, estado="En proceso", cliente_id=4, repartidor_id=6),
        Pedido(fecha="2026-03-03", total=20000, estado="Pendiente", cliente_id=5, repartidor_id=1),
        Pedido(fecha="2026-03-03", total=13000, estado="Entregado", cliente_id=6, repartidor_id=7),
        Pedido(fecha="2026-03-04", total=8000, estado="Cancelado", cliente_id=7, repartidor_id=9),
        Pedido(fecha="2026-03-04", total=34000, estado="En proceso", cliente_id=8, repartidor_id=10),
        Pedido(fecha="2026-03-05", total=5000, estado="Pendiente", cliente_id=9, repartidor_id=6),
        Pedido(fecha="2026-03-05", total=14000, estado="Entregado", cliente_id=10, repartidor_id=7)
    ]

    # Pasamos una sola lista con todos los elementos a add_all
    session.add_all(clientes + productos + repartidores + pedidos)
    session.commit()
    print("Datos sembrados exitosamente.")