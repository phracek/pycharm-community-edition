#!/bin/sh

RESULT_DIR="`pwd`/results"
if [ -d $RESULT_DIR ]; then
    rm -rf $RESULT_DIR
fi
mkdir $RESULT_DIR

# check if the source is downloaded
SOURCE_LINK=$(rpmspec -P pycharm-community.spec | grep Source0 | sed -E "s/Source0:[[:space:]]*(.*)/\1/g")
SOURCE_FILE=$(echo $SOURCE_LINK | sed -E "s/.*\/(.*)/\1/g")
if [ ! -f $SOURCE_FILE ]; then
    echo "'$SOURCE_FILE' not found -> downloading..."
    echo
    wget --user-agent="Mozilla/5.0" $SOURCE_LINK
fi

echo "Building SRPM..."
SRPM=$(rpmbuild -bs pycharm-community.spec --define "_sourcedir `pwd`" --define "_srcrpmdir $RESULT_DIR" | sed -E "s/Wrote: (.*)/\1/g")

echo "Building RPMs using mock..."
mock --rebuild $SRPM --resultdir=$RESULT_DIR

echo
echo "SRPM and RPMs are written in $RESULT_DIR"
