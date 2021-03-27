#!/bin/bash

echo "Hello World"

declare -r CLAUSE_LENGTH=3
declare -r NUM_VARIABLES=20
a=2
a=$((a+1))
echo $a

for num_clauses in 20 40 60 80 100 120 140 160 180 200
    do
        num_success=0
        echo $num_success
        for i in {1..50}
            do
            echo $num_clauses
               
            output=$(./makewff -cnf $CLAUSE_LENGTH $NUM_VARIABLES $num_clauses|timeout 10s ./walksat)

            found_string=$(echo "$output" | tail -n1)

            if [[ $found_string == "ASSIGNMENT FOUND" ]]; then
                #echo $found_string
                num_success=$((num_success+1))
                echo $(echo "$output" | grep "mean flips until assign =") >> "res.txt"
            fi
            done

        echo "$num_clauses,$num_success" >> "res.txt"
    done

