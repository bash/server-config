#!/bin/bash

mkdir -p $HOME/rpmbuild/SOURCES
rm $HOME/rpmbuild/SOURCES/root.tar.gz
tar -zcvf $HOME/rpmbuild/SOURCES/root.tar.gz ./usr ./etc

rpmbuild -bb package.spec --define "_release $TRAVIS_JOB_ID"
