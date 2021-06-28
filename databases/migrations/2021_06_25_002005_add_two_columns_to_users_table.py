from orator.migrations import Migration


class AddTwoColumnsToUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string('re_activated').nullable()
            table.timestamp('reactivated_on').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
