from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """Run the migrations."""
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('firstname')
            table.string('lastname')
            table.string('address')
            table.string('email').unique()
            table.string('username').unique()
            table.string('password').unique()
            table.string('remember_token').nullable()
            table.timestamp('verified_at').nullable()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop('users')
