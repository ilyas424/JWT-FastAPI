"""01_initial

Revision ID: 3d1ea20dc03e
Revises: cccbd5a4f682
Create Date: 2023-02-24 21:48:00.523410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d1ea20dc03e'
down_revision = 'cccbd5a4f682'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('login', sa.String(length=256), nullable=True))
    op.add_column('users', sa.Column('hash', sa.String(length=256), nullable=True))
    op.drop_constraint('users_name_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['login'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_name_key', 'users', ['name'])
    op.drop_column('users', 'hash')
    op.drop_column('users', 'login')
    # ### end Alembic commands ###
