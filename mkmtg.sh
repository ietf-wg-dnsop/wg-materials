#!/bin/sh
# simple script to do the doc preperation for an upcoming ietf meeting
# this fails for interims

WG=dnsop
ECHO=

if test $# -ne 1; then
    echo "usage: <num>"
    exit 1
fi

mtg=$1

IETF="${WG}-ietf$1"

if test -d "${IETF}"; then
    echo "${IETF} already exists"
    exit 1
fi
echo "Creating ${IETF}..."

${ECHO} mkdir -p "${IETF}"

${ECHO} cp ${WG}-templates/${WG}-agenda-requests-template.md "${IETF}"/"${IETF}"-agenda-requests.md

${ECHO} sed -e "s/%%MTG%%/${mtg}/g"  ${WG}-templates/${WG}-agenda-template.md > "${IETF}"/"${IETF}"-agenda.md

${ECHO} ln -s "${IETF}"-agenda-requests.md "${IETF}"/README.md
