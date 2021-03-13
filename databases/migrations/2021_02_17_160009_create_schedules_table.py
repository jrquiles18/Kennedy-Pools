from orator.migrations import Migration


class CreateSchedulesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('schedules') as table:
            table.increments('id')
            table.string('service')
            table.string('month')
            table.string('day')
            table.string('time')
            table.string('daytime')

            table.integer('schedule_id').unsigned()
            table.foreign('schedule_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('schedules')
