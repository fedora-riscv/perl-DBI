#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v 'perl(Win32::ODBC' | grep -v 'perl(RPC::PlClient' | grep -v 'perl(DBD::<foo>)' | grep -v 'perl(RPC::PlServer)'

