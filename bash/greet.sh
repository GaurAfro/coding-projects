# Create a Bash script that takes command-line arguments.

# Create a Bash script named greet.sh that takes a name as a command-line argument and prints a greeting message using that name. If no name is provided, it should print "Hello, stranger!"

name=$1

if [ -z "$name" ]
then
    echo "Hello, stranger!"
else
    echo "Hello, $name!"
fi
