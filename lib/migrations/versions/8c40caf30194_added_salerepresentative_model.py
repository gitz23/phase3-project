"""Added SaleRepresentative model

Revision ID: 8c40caf30194
Revises: 035890f4dea8
Create Date: 2023-09-11 16:09:59.146753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c40caf30194'
down_revision = '035890f4dea8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salesreps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salesreps')
    # ### end Alembic commands ###
