#!/bin/sh
set -e

RESULT_DIR="`pwd`/results"
if [ -d $RESULT_DIR ]; then
    rm -rf $RESULT_DIR
fi
mkdir $RESULT_DIR
[ $EUID -eq 0 ] && chown -v :mock $RESULT_DIR

function download_file {
    echo "Downloading $1 from URL $2"
    if [ ! -f $1 ]; then
        wget --user-agent="Mozilla/5.0" $2 -O $1
    else
        echo "File $1 already exists."
    fi

}
# check if the source is downloaded
SOURCE_LINK=$(rpmspec -P pycharm-community.spec | grep Source0 | sed -E "s/Source0:[[:space:]]*(.*)/\1/g")
SOURCE_FILE=$(echo $SOURCE_LINK | sed -E "s/.*\/(.*)/\1/g")
if [ ! -f $SOURCE_FILE ]; then
    echo "'$SOURCE_FILE' not found -> downloading..."
    echo
    wget --user-agent="Mozilla/5.0" $SOURCE_LINK
fi

CNT=`rpmspec -P pycharm-community.spec | grep ^Source | wc -l`
CNT=`expr $CNT - 4`
for (( i=1; i <= $CNT ; i++ ))
do
    FILE_NAME=$(rpmspec -P pycharm-community.spec | grep Source$i: | sed -E "s/Source$i:[[:space:]]*(.*)/\1/g")
    URL=$(grep "Source$i" pycharm-community.spec | sed -E "s/#Source$i[[:space:]]*(.*)/\1/g")
    echo "$URL"
    download_file $FILE_NAME $URL
done

echo "Building SRPM..."
SRPM=$(rpmbuild -bs pycharm-community.spec --define "_sourcedir `pwd`" --define "_srcrpmdir $RESULT_DIR" | sed -E "s/Wrote: (.*)/\1/g")
[ $EUID -eq 0 ] && chown -v :mock $SRPM

echo "Building RPMs using mock..."
/usr/bin/mock --rebuild $SRPM --resultdir=$RESULT_DIR

echo
echo "SRPM and RPMs are written in $RESULT_DIR"
