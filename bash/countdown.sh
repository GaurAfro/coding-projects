# Create a Bash script that uses a for loop.

# Create a script named countdown.sh that takes a number as a command-line argument and counts down to zero from that number. For example, if you run ./countdown.sh 5, it should print:

# Counting down from 5...
# 5
# 4
# 3
# 2
# 1
# 0
# If no number is provided, it should print "No number provided."

# take any number from command line

number=$1

if [ -z "$number" ]
then
    echo "No number provided."
else
    echo "Counting down from $number..."
    while [ $number -gt 0 ]
    do
        echo $number
        number=$(( $number - 1 ))
    done
fi
