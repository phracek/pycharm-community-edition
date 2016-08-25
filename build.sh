#!/bin/bash
set -e

RESULT_DIR="`pwd`/results"
if [ -d $RESULT_DIR ]; then
    rm -rfv $RESULT_DIR
fi
mkdir -v $RESULT_DIR
if [ $(id -u) -eq 0 ]; then
   chown -v :mock $RESULT_DIR
fi

MOCK_CONFIG="default"

echo "Downloading sources..."
/usr/bin/perl spectool.pl --all --get-files pycharm-community.spec

echo "Building SRPM..."
SRPM=$(rpmbuild -bs pycharm-community.spec --define "_sourcedir `pwd`" --define "_srcrpmdir $RESULT_DIR" | sed -E "s/Wrote: (.*)/\1/g")
[ $EUID -eq 0 ] && chown -v :mock $SRPM

echo "Building RPMs using mock..."
/usr/bin/mock -r ${MOCK_CONFIG} --rebuild $SRPM --resultdir=$RESULT_DIR

echo
echo "SRPM and RPMs are written in $RESULT_DIR"
