#!/bin/bash

version=$1
[ -z "$version" ] && { echo "Usage: $0 <version>"; exit 1; }

# files to be removed without the main DBI-<version>/ prefix
declare -a REMOVE
REMOVE[${#REMOVE[*]}]="lib/DBI/FAQ.pm"

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
