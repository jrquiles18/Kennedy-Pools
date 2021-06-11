from orator.migrations import Migration


class AddCancelledAppointmentToSchedules(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.drop_column('cancelled_on')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
