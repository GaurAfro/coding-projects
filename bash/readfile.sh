# Create a Bash script that reads from a file.

# Create a Bash script named readfile.sh that reads from a text file line by line and prints each line to the console. The text file should be provided as a command-line argument. If no file is provided, it should print "No file provided."

# If you run ./readfile.sh myfile.txt, it should print:
# Reading file myfile.txt...
# line 1
# line 2
# line 3
# line 4
# line 5

file=$1

if [ -z "$file" ]
then
    echo "No file provided."
else
    echo "Reading file $file..."
    while read -r line
    do
        echo $line
    done < $file
fi
