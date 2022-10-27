import view 
import model



def function_start():
    global first_choice 
    first_choice = view.welcome_screen()
    return first_choice



if __name__ == '__main__':
    # calling the welcome screen function via the start function in the controller.
    function_start()
    if first_choice == "R":
        # Get the registration data and then get to the Model for the database Fetching
        register_data = view.register()
        user_result = model.check_and_register_user(register_data[0] , register_data[1])
        if user_result == True:
            view.common_message("User registered and redirecting to the login page")
            view.Login_screen()
    elif first_choice == "L":
        # Getting the login details from the login screen in the view model and sharing the details to the controller
        login_details = view.Login_screen()
        returned_data  = model.check_and_login_user(login_details[0] , login_details[1])
        if returned_data == True:
            view.common_message("Login Successful redirecting to the login page")
            # Have to define the login page here so that user can see and request books
            
    elif first_choice == "A":
        admin_details = view.admin()
        result  = model.search_admin(admin_details[0] , admin_details[1])
        if result:
            view.common_message("Successful login Redirecting to the admin page")
            maindetail = model.admin_details()
            print(maindetail[0] , maindetail[1])
            view.admin_page(maindetail[0] , maindetail[1])
        else:
            view.common_message("Login Failed Please check the username and password")
            view.common_message("redirecing to the welcome screen")
            function_start()
    else:
        print("Please Enter a valid choice Starting Welcome Screen Again")
        function_start()