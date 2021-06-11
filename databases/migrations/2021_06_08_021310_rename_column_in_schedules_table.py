from orator.migrations import Migration


class RenameColumnInSchedulesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.drop_column('cancelled_on')
            table.string('service_state').default('Active')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
