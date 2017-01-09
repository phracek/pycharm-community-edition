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

echo "Downloading sources..."
/usr/bin/perl spectool.pl --all --get-files pycharm-community.spec

echo "Building SRPM..."
set -o pipefail
SRPM=$(rpmbuild -bs pycharm-community.spec --define "_sourcedir `pwd`" --define "_srcrpmdir $RESULT_DIR" | sed -E "s/Wrote: (.*)/\1/g")
[ $EUID -eq 0 ] && chown -v :mock $SRPM


ls -la /etc/mock/
[ -z $MOCK_CONFIG ] && MOCK_CONFIG="fedora-rawhide-x86_64"
if [ ! -f "/etc/mock/$MOCK_CONFIG.cfg" ]; then
    MOCK_CONFIG="fedora-rawhide-x86_64"
fi
echo "Building RPMs using mock...$(basename $MOCK_CONFIG)"
/usr/bin/mock -r $(basename "$MOCK_CONFIG") --rebuild $SRPM --resultdir=$RESULT_DIR

echo
echo "SRPM and RPMs are written in $RESULT_DIR"
