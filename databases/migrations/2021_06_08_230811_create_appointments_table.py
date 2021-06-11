from orator.migrations import Migration


class CreateAppointmentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('appointments') as table:
            table.string('pool_technician')
            table.string('customer_name')
            table.string('customer_address')
            table.string('service_requested')
            table.string('service_date')
            table.string('service_time')
            table.integer('customer_id').unsigned()
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('appointments')
