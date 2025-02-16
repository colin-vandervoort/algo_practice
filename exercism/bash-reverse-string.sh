#!/usr/bin/env bash

# if [ "$#" -eq 1 ]; then
#     orig="$1"
#     length="${#orig}"

#     for (( idx=$((length-1)); idx>=0; idx-- )); do
#         echo -n "${orig:$idx:1}"
#     done
#     echo
# fi

orig="$1"
length="${#orig}"
[ "$length" -eq 0 ] && exit 0

for idx in $(seq $((length-1)) 0); do
    echo $idx
    # echo -n "${orig:$idx:1}"
done
echo