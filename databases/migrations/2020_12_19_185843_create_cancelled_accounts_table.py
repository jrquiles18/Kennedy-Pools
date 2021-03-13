from orator.migrations import Migration


class CreateCancelledAccountsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cancelled_accounts') as table:
            table.increments('id')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.date('cancel_date')
            table.long_text('cancel_reason')
            table.long_text('suggestions')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cancelled_accounts')
