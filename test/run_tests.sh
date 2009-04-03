#!/bin/bash
testfiles=`ls test_*.py`
export LD_LIBRARY_PATH=/opt/cvs/lib/
export PKG_CONFIG_PATH=/opt/cvs/lib/pkgconfig/
export PYTHONPATH=/opt/cvs/lib/python2.5/site-packages/:../.libs

for t in $testfiles
do
    fname=`basename $t`
    echo -n "RUNNING TEST: $fname ..."
    python $t &> "$t.log"

    #check if test finished
    grep "FINISHED" "$t.log" -q
    if [ $? -eq 0 ]
    then
        echo "(ok)"
    else
        cat "$t.log"
        echo "(failed)"
    fi
done



