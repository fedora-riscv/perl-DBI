#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v 'perl(RPC::' |grep -v 'perl(Apache'
