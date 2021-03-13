from orator.migrations import Migration


class CreatePoolCleaningsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pool_cleanings') as table:
            table.increments('id')
            table.integer('service_id').unsigned()
            table.foreign('service_id').references('id').on('users')
            table.string('pool_technician')
            table.text('service_performed')
            table.date('service_date')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pool_cleanings')
