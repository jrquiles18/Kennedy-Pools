from orator.migrations import Migration


class AddColumnBackToSchedulesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.string('service_time').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
