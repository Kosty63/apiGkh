"""Add table

Revision ID: 9a6ebf5c96bb
Revises:
Create Date: 2025-02-27 18:29:52.692025

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9a6ebf5c96bb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("city", sa.String(length=50), nullable=False),
        sa.Column("street", sa.String(), nullable=False),
        sa.Column("house_number", sa.String(length=10), nullable=False),
        sa.Column("apartment_number", sa.String(length=10), nullable=False),
        sa.Column("postal_code", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "services",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("service_name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("tariff", sa.Integer(), nullable=False),
        sa.Column("unit", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone_number", sa.String(length=15), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "personal_accounts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("addresses_id", sa.Integer(), nullable=False),
        sa.Column("balance", sa.Integer(), nullable=False),
        sa.Column("debt", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["addresses_id"],
            ["addresses.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["owners.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "charges",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("personal_account_id", sa.Integer(), nullable=False),
        sa.Column("charge_date", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.Integer(), nullable=False),
        sa.Column("volume", sa.Integer(), nullable=False),
        sa.Column("unit", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["personal_account_id"],
            ["personal_accounts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["service_id"],
            ["services.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "meters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("personal_account_id", sa.Integer(), nullable=False),
        sa.Column("meter_type", sa.String(), nullable=False),
        sa.Column("installation_date", sa.String(), nullable=False),
        sa.Column("last_check_date", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["personal_account_id"],
            ["personal_accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "payments_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("personal_account_id", sa.Integer(), nullable=False),
        sa.Column("payment_date", sa.String(), nullable=False),
        sa.Column("amount", sa.String(), nullable=False),
        sa.Column("payment_method", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["personal_account_id"],
            ["personal_accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "meter_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("meter_id", sa.Integer(), nullable=False),
        sa.Column("reading_date", sa.Integer(), nullable=False),
        sa.Column("value", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["meter_id"],
            ["meters.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("meter_history")
    op.drop_table("payments_history")
    op.drop_table("meters")
    op.drop_table("charges")
    op.drop_table("personal_accounts")
    op.drop_table("users")
    op.drop_table("services")
    op.drop_table("owners")
    op.drop_table("addresses")

