from orator.migrations import Migration


class CreateOneTimeServicesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('one_time_services') as table:
            table.increments('id')
            table.string('service')
            table.string('customer_name')
            table.string('address')
            table.string('email')
            table.string('cell_phone')
            table.string('service_date')
            table.string('service_time')
            table.string('service_state').nullable()
            table.string('cancelled_on').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('one_time_services')


__fillable__ = ['service', 'service_date', 'service_time', 'customer_name', 'address', 'service_state', 'cancelled_on']