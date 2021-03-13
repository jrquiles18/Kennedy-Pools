from orator.migrations import Migration


class AddCellPhoneColumnToUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string('cell_phone')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
