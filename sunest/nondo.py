def my_function(init=0, max_value=100):
    for i in range(init, max_value):
        print(i)

# Call the function
my_function()           # Default values: prints 0 to 99
my_function(5, 10)      # Custom values: prints 5 to 9
