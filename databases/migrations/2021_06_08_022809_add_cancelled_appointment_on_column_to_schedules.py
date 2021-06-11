from orator.migrations import Migration


class AddCancelledAppointmentOnColumnToSchedules(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.string('cancelled_on').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
