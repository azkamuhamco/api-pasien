"""First Revision

Revision ID: b8b9998b8855
Revises: 
Create Date: 2023-03-18 12:04:36.358709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b9998b8855'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dokter',
    sa.Column('kode_dokter', sa.String(length=6), nullable=False),
    sa.Column('nama_dokter', sa.String(length=100), nullable=False),
    sa.Column('tgl_lahir', sa.Date(), nullable=False),
    sa.Column('jenis_kelamin', sa.String(length=1), nullable=False),
    sa.Column('alamat', sa.String(length=200), nullable=True),
    sa.Column('telpon', sa.String(length=15), nullable=True),
    sa.Column('poli', sa.String(length=50), nullable=False),
    sa.Column('tarif', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('kode_dokter')
    )
    op.create_table('pasien',
    sa.Column('kode_pasien', sa.String(length=6), nullable=False),
    sa.Column('nama_pasien', sa.String(length=100), nullable=False),
    sa.Column('tgl_lahir', sa.Date(), nullable=False),
    sa.Column('jenis_kelamin', sa.String(length=1), nullable=False),
    sa.Column('alamat', sa.String(length=200), nullable=True),
    sa.Column('telpon', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('kode_pasien')
    )
    op.create_table('tele_order',
    sa.Column('kode_order_tele', sa.String(length=10), nullable=False),
    sa.Column('kode_pasien', sa.String(length=6), nullable=False),
    sa.Column('kode_dokter', sa.String(length=6), nullable=False),
    sa.Column('waktu_order', sa.DateTime(), nullable=False),
    sa.Column('rencana_periksa', sa.DateTime(), nullable=False),
    sa.Column('keluhan', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['kode_dokter'], ['dokter.kode_dokter'], ),
    sa.ForeignKeyConstraint(['kode_pasien'], ['pasien.kode_pasien'], ),
    sa.PrimaryKeyConstraint('kode_order_tele')
    )
    op.create_table('tele',
    sa.Column('kode_tele', sa.String(length=10), nullable=False),
    sa.Column('kode_order_tele', sa.String(length=10), nullable=False),
    sa.Column('waktu_periksa', sa.DateTime(), nullable=False),
    sa.Column('catatan_dokter', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['kode_order_tele'], ['tele_order.kode_order_tele'], ),
    sa.PrimaryKeyConstraint('kode_tele')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tele')
    op.drop_table('tele_order')
    op.drop_table('pasien')
    op.drop_table('dokter')
    # ### end Alembic commands ###
