"""init

Revision ID: 401b5bed879d
Revises: 
Create Date: 2023-11-03 22:41:57.321252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '401b5bed879d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(120), nullable=False),
        sa.Column('address', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(14), unique=True, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    )


def downgrade() -> None:
    op.execute(sa.DDL("DROP TABLE users"))
