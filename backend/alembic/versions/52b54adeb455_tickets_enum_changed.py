"""tickets enum changed

Revision ID: 52b54adeb455
Revises: 026b0ac6fc17
Create Date: 2026-10-28 22:14:31.596779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52b54adeb455'
down_revision: Union[str, Sequence[str], None] = '026b0ac6fc17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename status enum values
    op.execute(
        "ALTER TYPE status RENAME VALUE 'OPEN' TO 'Open'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'IN_PROGRESS' TO 'In Progress'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'RESOLVED' TO 'Resolved'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'CLOSED' TO 'Closed'"
    )

    # Rename priority enum values
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'LOW' TO 'Low'"
    )
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'HIGH' TO 'High'"
    )
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'URGENT' TO 'Urgent'"
    )


def downgrade() -> None:
    # Restore priority enum values
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'Low' TO 'LOW'"
    )
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'High' TO 'HIGH'"
    )
    op.execute(
        "ALTER TYPE priority RENAME VALUE 'Urgent' TO 'URGENT'"
    )

    # Restore status enum values
    op.execute(
        "ALTER TYPE status RENAME VALUE 'Open' TO 'OPEN'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'In Progress' TO 'IN_PROGRESS'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'Resolved' TO 'RESOLVED'"
    )
    op.execute(
        "ALTER TYPE status RENAME VALUE 'Closed' TO 'CLOSED'"
    )