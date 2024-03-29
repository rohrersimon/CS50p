# exercises=("einstein" "faces" "indoor" "playback" "tip")
# exercises=("deep" "bank" "extensions" "interpreter" "meal")
# exercises=("camel" "coke" "twttr" "plates" "nutrition")
# exercises=("fuel" "taqueria" "grocery" "outdated")
# exercises=("emojize" "figlet" "adieu" "game" "professor" "bitcoin")
# exercises=("bank" "fuel" "plates" "twttr")
# exercises=("lines" "pizza" "scourgify" "shirt")
# exercises=("numb3rs" "um" "watch" "working" "response")
exercises=("jar" "seasons" "shirtificate")
ProblemSet='8'

# Loop through the exercises and check each exercise
for string in "${exercises[@]}"; do
    cd /workspaces/105282514/'Problem Set '$ProblemSet/$string

    #check50 cs50/problems/2022/python/$string
    submit50 cs50/problems/2022/python/$string

    #read -p "Press Enter to continue... "

done

# generate requirements.txt
pip freeze > requirements.txt
