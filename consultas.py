from sqlalchemy import or_, desc
from sqlalchemy.orm import Session
from schema import engine, Cliente, Producto, Repartidor, Pedido

with Session(engine) as session:
    # 1. 
    productos_activos = session.query(Producto).filter(Producto.activo == True).all()
    print("--- Productos Activos ---")
    for p in productos_activos:
        print(f"- {p.nombre}: ${p.precio}")

    pedidos_caros = session.query(Pedido).filter(Pedido.total > 15000).all()
    print("\n--- Pedidos con total mayor a $15.000 ---")
    for p in pedidos_caros:
        print(f"- Pedido ID {p.id}: ${p.total} (Estado: {p.estado})")

    repartidores_inactivos = session.query(Repartidor).filter(Repartidor.activo != True).all()
    print("\n--- Repartidores Inactivos ---")
    for r in repartidores_inactivos:
        print(f"- {r.nombre} {r.apellido}")

    # 2.
    pedidos_pendientes_o_proceso = session.query(Pedido).filter(
        or_(Pedido.estado == "Pendiente", Pedido.estado == "En proceso")
    ).all()
    print("\n--- Pedidos Pendientes o En Proceso ---")
    for p in pedidos_pendientes_o_proceso:
        print(f"- Pedido ID {p.id}: {p.estado}")

    pizzas = session.query(Producto).filter(Producto.nombre.contains("Pizza")).all()
    print("\n--- Productos que contienen 'Pizza' ---")
    for p in pizzas:
        print(f"- {p.nombre}")

    # 3.
    pedido_mas_caro = session.query(Pedido).order_by(desc(Pedido.total)).first()
    print("\n--- Pedido de mayor valor ---")
    if pedido_mas_caro:
        print(f"- Pedido ID {pedido_mas_caro.id} con un total de ${pedido_mas_caro.total}")