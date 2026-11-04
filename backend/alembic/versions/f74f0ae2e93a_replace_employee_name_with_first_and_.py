"""replace employee name with first and last name

Revision ID: f74f0ae2e93a
Revises: 763e6c2437e9
Create Date: 2026-11-04 21:51:40.685812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f74f0ae2e93a'
down_revision: Union[str, Sequence[str], None] = '763e6c2437e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Add new columns
    op.add_column(
        'users',
        sa.Column('first_name', sa.String(50), nullable=True)
    )

    op.add_column(
        'users',
        sa.Column('last_name', sa.String(50), nullable=True)
    )

    # 2. Transfer existing data
    op.execute("""
        UPDATE public.users
        SET
            first_name = split_part(trim(employee_name), ' ', 1),
            last_name = CASE
                WHEN position(' ' IN trim(employee_name)) > 0
                THEN substring(
                    trim(employee_name)
                    FROM position(' ' IN trim(employee_name)) + 1
                )
                ELSE ''
            END
        WHERE employee_name IS NOT NULL
    """)

    # 3. Remove old column
    op.drop_column('users', 'employee_name')

    # 4. Make first_name mandatory
    op.alter_column(
        'users',
        'first_name',
        existing_type=sa.String(50),
        nullable=False
    )