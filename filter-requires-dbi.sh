#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v 'perl(Win32::ODBC' | grep -v 'perl(RPC::PlClient'
