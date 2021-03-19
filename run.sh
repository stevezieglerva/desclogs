python3 /Users/sziegler/Documents/Github/desclogs/desclogs.py $1
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Quit"
else
    . ~/temp/temp_shell.sh

    echo ""
    echo "Re-run command:"
    cat ~/temp/temp_shell.sh
    cat ~/temp/temp_shell.sh | pbcopy
    echo ""

fi



