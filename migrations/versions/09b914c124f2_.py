"""empty message

Revision ID: 09b914c124f2
Revises: 5356895fbdee
Create Date: 2024-06-19 19:58:13.685826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b914c124f2'
down_revision = '5356895fbdee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('nombre')
    )
    op.create_table('edad_objetivo',
    sa.Column('rango', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('rango')
    )
    op.create_table('influencer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('red_social', sa.String(length=50), nullable=False),
    sa.Column('er_instagram', sa.Float(), nullable=True),
    sa.Column('seguidores_instagram', sa.Integer(), nullable=True),
    sa.Column('er_tiktok', sa.Float(), nullable=True),
    sa.Column('seguidores_tiktok', sa.Integer(), nullable=True),
    sa.Column('imagen', sa.String(length=255), nullable=True),
    sa.Column('estilo_de_vida', sa.String(length=50), nullable=True),
    sa.Column('sexo', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pais_objetivo',
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('nombre')
    )
    op.create_table('categoria_table',
    sa.Column('influencer_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['influencer_id'], ['influencer.id'], ),
    sa.ForeignKeyConstraint(['nombre'], ['categoria.nombre'], ),
    sa.PrimaryKeyConstraint('influencer_id', 'nombre')
    )
    op.create_table('edad_objetivo_table',
    sa.Column('influencer_id', sa.Integer(), nullable=False),
    sa.Column('rango', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['influencer_id'], ['influencer.id'], ),
    sa.ForeignKeyConstraint(['rango'], ['edad_objetivo.rango'], ),
    sa.PrimaryKeyConstraint('influencer_id', 'rango')
    )
    op.create_table('pais_objetivo_table',
    sa.Column('influencer_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['influencer_id'], ['influencer.id'], ),
    sa.ForeignKeyConstraint(['nombre'], ['pais_objetivo.nombre'], ),
    sa.PrimaryKeyConstraint('influencer_id', 'nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pais_objetivo_table')
    op.drop_table('edad_objetivo_table')
    op.drop_table('categoria_table')
    op.drop_table('pais_objetivo')
    op.drop_table('influencer')
    op.drop_table('edad_objetivo')
    op.drop_table('categoria')
    # ### end Alembic commands ###