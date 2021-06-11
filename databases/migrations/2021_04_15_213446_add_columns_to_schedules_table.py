from orator.migrations import Migration


class AddColumnsToSchedulesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.string('service_date').nullable()
            table.time('service_time').nullable()
    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
