"""empty message

Revision ID: 6767e9b4fdab
Revises: 
Create Date: 2021-05-31 15:54:18.723507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6767e9b4fdab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_residencias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model_residencias')
    # ### end Alembic commands ###
