# Shutdown

def shutdown():
    user_input = input("Should we shut down you computer? yes/no")
    if user_input == "yes":
        print("Shutting down...")
        import os
        os.system("shutdown /s /t 1")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry")
shutdown()