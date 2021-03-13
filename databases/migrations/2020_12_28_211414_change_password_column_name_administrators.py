from orator.migrations import Migration


class ChangePasswordColumnNameAdministrators(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('administrators') as table:
            table.drop_column('admin_password')
            table.string('password').unique()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('administrators') as table:
            pass
