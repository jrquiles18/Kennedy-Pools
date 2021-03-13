from orator.migrations import Migration


class CreateAdministratorsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('administrators') as table:
            table.increments('id')
            table.string('admin_name')
            table.string('admin_cell_phone')
            table.string('admin_address')
            table.string('admin_email').unique()
            table.string('admin_username').unique()
            table.string('admin_password').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('administrators')
