from orator.migrations import Migration


class AddRememberTokenColumnToOneTimeServices(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('one_time_services') as table:
            table.string('remember_token').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('one_time_services') as table:
            pass
