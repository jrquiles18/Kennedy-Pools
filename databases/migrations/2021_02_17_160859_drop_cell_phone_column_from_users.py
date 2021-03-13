from orator.migrations import Migration


class DropCellPhoneColumnFromUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.drop_column('cell_phone')
            

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
