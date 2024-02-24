MAX_ITER=10
ITERATION=0
CONVERGED=false
while [ $CONVERGED == false ]; do
    let ITERATION++

    echo $ITERATION

    if [ $ITERATION -eq $MAX_ITER ]; then
        CONVERGED=true
    fi
done