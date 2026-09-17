from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase): 
    pass 

class Cliente(Base): 
    __tablename__ = "clientes" 
    id = Column(Integer, primary_key=True, autoincrement = True) 
    nombre = Column(String) 
    apellido = Column(String) 
    telefono = Column(String) 
    direccion = Column(String) 

    pedidos = relationship("Pedido", back_populates="cliente")

class Producto(Base): 
    __tablename__ = "productos" 
    id = Column(Integer, primary_key=True, autoincrement = True) 
    nombre = Column(String) 
    descripcion = Column(String) 
    precio = Column(Integer) 
    activo = Column(Boolean) 

class Repartidor(Base): 
    __tablename__ = "repartidores" 
    id = Column(Integer, primary_key=True, autoincrement = True) 
    nombre = Column(String) 
    apellido = Column(String) 
    activo = Column(Boolean) 

    pedidos = relationship("Pedido", back_populates="repartidor")

class Pedido(Base): 
    __tablename__ = "pedidos" 
    id = Column(Integer, primary_key=True, autoincrement = True) 
    fecha = Column(String) 
    total = Column(Integer) 
    estado = Column(String) 
    cliente_id = Column(Integer, ForeignKey("clientes.id")) 
    repartidor_id = Column(Integer, ForeignKey("repartidores.id")) 

    cliente = relationship("Cliente", back_populates="pedidos")
    repartidor = relationship("Repartidor", back_populates="pedidos")

engine = create_engine("sqlite:///restaurante.db") 
Base.metadata.create_all(engine)