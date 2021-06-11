from orator.migrations import Migration


class DropColumnsFromSchedulesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.drop_column('service_date', 'service_time')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
