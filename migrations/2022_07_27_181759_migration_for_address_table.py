"""MigrationForAddressTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForAddressTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("address") as table:
            table.increments("id")
            table.integer('user_id').unsigned()
            table.foreign('user_id', name='address_user_id_foreign').references('id').on('user')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("address")
