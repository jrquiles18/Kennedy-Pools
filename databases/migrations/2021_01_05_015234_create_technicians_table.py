from orator.migrations import Migration


class CreateTechniciansTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('technicians') as table:
            table.increments('id')
            table.string('pool_tech_name')
            table.string('pool_tech_cell_phone')
            table.string('pool_tech_address')
            table.string('pool_tech_email').unique()
            table.string('pool_tech_username').unique()
            table.string('password').unique()
            table.string('remember_token').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('technicians')
