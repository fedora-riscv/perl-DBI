#!/bin/bash
#
# Copyright (C) 2010 Red Hat, Inc.
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Script was a bit changed for DBI, because command below breaks tar index
# tar -f <tarball> --delete <file>
# Jitka Plesnikova <jplesnik@redhat.com>

version=$1
[ -z "$version" ] && { echo "Usage: $0 <version>"; exit 1; }

# files to be removed without the main DBI-<version>/ prefix
declare -a REMOVE
REMOVE[${#REMOVE[*]}]="lib/DBI/FAQ.pm"

# no changes below this line should be needed

orig="DBI-${version}"
orig_tgz="${orig}.tar.gz"
repackaged="${orig}_repackaged"
repackaged_tgz="${repackaged}.tar.gz"

# pre checks
[ ! -f "${orig_tgz}" ] && { echo "ERROR: ${orig_tgz} does not exist"; exit 1; }
[ -f "${repackaged_tgz}" ] && { echo "ERROR: ${repackaged_tgz} already exist"; exit 1; }

# repackage
tdir=`mktemp -d tmpXXXXXX`
pushd "${tdir}"

tar -xpzf ../${orig_tgz}
for file in "${REMOVE[@]}"; do
    rm -rf "${orig}/${file}"
done
tar -cpzf ../"${repackaged_tgz}" "${orig}"

popd
rm -rf "${tdir}"

# post checks
RET=0
for file in "${REMOVE[@]}"; do
    found=$(tar -ztvf "${repackaged_tgz}" | grep "${file}")
    [ -n "$found" ] && { echo "ERROR: file ${file} is still in the repackaged archive."; RET=1; }
done

[ $RET == 0 ] && echo "Sucessfully repackaged ${orig}: ${repackaged_tgz}"

exit $RET
