# Makefile for source rpm: perl-DBI
# $Id$
NAME := perl-DBI
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
