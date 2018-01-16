#!/bin/bash

mkdir -p $HOME/rpmbuild/SOURCES
tar -zcvf $HOME/rpmbuild/SOURCES/root.tar.gz ./root

rpmbuild -bb package.spec
