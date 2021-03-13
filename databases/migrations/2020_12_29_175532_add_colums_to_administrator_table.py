from orator.migrations import Migration


class AddColumsToAdministratorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('administrators') as table:
            table.string('remember_token').nullable()
            table.timestamp('verified_at').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('administrators') as table:
            pass
