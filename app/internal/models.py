from sqlalchemy import MetaData, Column, String, Date, Integer, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

meta = MetaData()
Base = declarative_base()

class Dokter(Base): 
    __tablename__ = 'dokter'
    kode_dokter   = Column(String(6), primary_key = True)
    nama_dokter   = Column(String(100), nullable=False)
    tgl_lahir     = Column(Date, nullable=False)
    jenis_kelamin = Column(String(1), nullable=False)
    alamat        = Column(String(200))
    telpon        = Column(String(15))
    poli          = Column(String(50), nullable=False)
    tarif         = Column(Integer)

    orders = relationship("TeleOrder", back_populates="dokters")

class Pasien(Base): 
    __tablename__  = 'pasien'
    kode_pasien    = Column(String(6), primary_key = True)
    nama_pasien    = Column(String(100), nullable=False)
    tgl_lahir      = Column(Date, nullable=False)
    jenis_kelamin  = Column(String(1), nullable=False)
    alamat         = Column(String(200))
    telpon         = Column(String(15))

    orders = relationship("TeleOrder", back_populates="pasiens")

class TeleOrder(Base): 
    __tablename__   = 'tele_order'
    kode_order_tele = Column(String(10), primary_key = True)
    kode_pasien     = Column(String(6), ForeignKey("pasien.kode_pasien"), nullable=False) 
    kode_dokter     = Column(String(6), ForeignKey("dokter.kode_dokter"), nullable=False) 
    waktu_order     = Column(DateTime, nullable=False)
    rencana_periksa = Column(DateTime, nullable=False) 
    keluhan         = Column(Text, nullable=False)

    teles = relationship("Tele", back_populates="orders")
    pasiens = relationship("Pasien", back_populates="orders")
    dokters = relationship("Dokter", back_populates="orders")

class Tele(Base): 
    __tablename__   = 'tele'
    kode_tele       = Column(String(10), primary_key = True)
    kode_order_tele = Column(String(10), ForeignKey("tele_order.kode_order_tele"), nullable=False)
    waktu_periksa   = Column(DateTime, nullable=False) 
    catatan_dokter  = Column(Text)

    orders = relationship("TeleOrder", back_populates="teles")