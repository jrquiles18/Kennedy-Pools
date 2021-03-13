"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/','HomeController@show').name('home'),
    Get('/login', "LoginController@show").name('login'),
    Get('/login/forgot', "PasswordController@forgot").name('forgot_password'),
    Get('/register', "RegisterController@show").name('register'),
    Get('/registered', "RegisteredController@show").name('registered'),
    Get('/schedule', "ScheduleController@show").name('schedule'),
    Get('/account', "AccountController@show").name('account'),
    Get('/account/cancel',"AccountCancelController@show").name('account_cancel'),
    Get('/account/update', "AccountUpdateController@show").name('account_update'),
    Get('/account/password', "PasswordController@show").name('password'),
    Get('/password/reset/get/@id', "PasswordController@link").name('link'),
    Get('/account/cleaning', "PoolCleaningController@show").name('pool_cleaning'),
    Get('/contact', "ContactController@show").name('contact'),
    Get('/schedule', "ScheduleController@logout").name('schedule_logout'),
    #Get('/', 'WelcomeController@show').name('welcome'),

    Post('/','HomeController@logout').name('home_logout'),

    Post('/register', "RegisterController@register").name('account_register'),
    Post('/login', "LoginController@store").name('login_user'),
    Post('/login/forgot', "PasswordController@send").name('send'),
    # Post('/schedule', "ScheduleController@logout").name('schedule_logout'),
    Post('/account', "AccountController@logout").name('account_logout'),
    Post('/account/cancel', "AccountCancelController@cancel").name('account_cancel'),
    Post('/account/update', "AccountUpdateController@update").name('update_account'),
    #Post('/account/update', "AccountUpdateController@logout_user").name('account_update_logout'),
    Post('/account/password', "PasswordController@update").name('password'),
    Post('/password/reset/get/@id', "PasswordController@reset").name('reset'),
    Post('/account/cleaning', "PoolCleaningController@logout").name('pool_cleaning_logout'),
    Post('/contact', "ContactController@contact").name('contact_submit_form'),
    Post('/schedule', "ScheduleController@schedule").name('schedule'),

    #Dashboard ROUTES
    Get('/dashboard', "dashboard.HomeDashboardController@show").name('home_dashboard'),
    Get('/admin', "dashboard.AdminController@show").name('admin_login'),
    Get('/admin/dashboard/', "dashboard.AdminDashboardController@show").name('admin_dashboard'),
    Get('/tech', "dashboard.PoolTechController@show").name('pool_tech_login'),
    Get('tech/dashboard', "dashboard.PoolTechDashboardController@show").name('pool_tech_dashboard'),
    Get('/dashboard/admin/setup', "dashboard.AdminSetupController@show").name('admin_account_setup'),
    Get('/dashboard/tech/setup', "dashboard.PoolTechSetupController@show").name('pool_tech_account_setup'),
    Get('/admin/technicians', "dashboard.TechniciansController@show").name('pool_technicians'),
    Get('/admin/customers', "dashboard.CustomerAccountsController@show").name('customer_accounts'),
    Get('/admin/schedules', "dashboard.CustomerSchedulesController@show").name('customer_schedules'),

    Post('/dashboard/admin/setup', "dashboard.AdminSetupController@register").name('admin_account_register'),
    Post('/dashboard/tech/setup', "dashboard.PoolTechSetupController@register").name('pool_tech_account_register'),
    Post('/admin', "dashboard.AdminController@login").name('admin_login'),
    Post('/tech', "dashboard.PoolTechController@login").name('pool_tech_login'),
    Post('/admin/dashboard', "dashboard.AdminController@logout").name('admin_logout'),
    Post('/tech/dashboard', "dashboard.PoolTechController@logout").name('pool_tech_logout'),
    Post('/admin/technicians', "dashboard.TechniciansController@logout").name('technicians_logout'),
    Post('/admin/customers', "dashboard.CustomerAccountsController@logout").name('customers_logout')





    #Admin ROUTES

]

from masonite.auth import Auth
ROUTES += Auth.routes()
