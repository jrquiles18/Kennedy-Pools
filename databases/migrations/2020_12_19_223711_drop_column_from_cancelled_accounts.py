from orator.migrations import Migration


class DropColumnFromCancelledAccounts(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('cancelled_accounts') as table:
            table.drop_column('cancel_date')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('cancelled_accounts') as table:
            pass
