#!/usr/bin/env python
# prints out agenda and timetable from agenda requests

# run this
# pr-agenda.py <session> [--write]

import argparse

alltimes = []
alltalks = {}

def addtalk(agendaitem):
    if agendaitem:
        if agendaitem.get('wgdoc'):
            alltalks.setdefault('wgdocs', []).append(agendaitem)
        else:
            alltalks.setdefault('nonwgdocs', []).append(agendaitem)

def readf(filename):
    with open(filename, encoding="ascii") as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

    if '## Requests' in lines:
        item = lines.index('## Requests')
        lines = lines[item+1::]

    return lines

def getitems(newlines):
    agendaitem = {}
    for l in newlines:
        if not l:
            continue
        fields = l.split()
        if l.startswith('*'):
            # new agenda item
            addtalk(agendaitem)
            title = ' '.join(fields[1:])
            title = title.replace('Draft name: ', '')
            agendaitem = {}
            agendaitem.setdefault('title', title)
        if 'Datatracker URL' in l:
            url = fields[-1]
            wgdoc = bool('draft-ietf-dnsop' in url)
            agendaitem.setdefault('url', fields[-1])
            agendaitem.setdefault('wgdoc', wgdoc)
        if 'Requester Email' in l:
            agendaitem.setdefault('email', ' '.join(fields[3::]))
        if 'Time Requested' in l:
            agendaitem.setdefault('time', fields[3].replace('min', ''))
        if 'DocType' in l:
            doctype = ' '.join(fields[2::]).lower()
            if doctype not in ['current', 'for consideration', 'i-d']:
                agendaitem.setdefault('doctype', ' '.join(fields[2::]))
        if 'Remark' in l:
            agendaitem.setdefault('remark', ' '.join(fields[2::]))


    addtalk(agendaitem)


def printitem(docs):
    lines = []
    for i in docs:
        lines.append(f"*   {i.get('title')}")
        lines.append(f"    - {i.get('url')}")
        lines.append(f"    - {i.get('email')}, {i.get('time')}")
        lines.append("    - Chairs Action:")
        if i.get('remark'):
            lines.append(f"    - Remark: {i.get('remark')}")
        if i.get('doctype'):
            lines.append(f"    - DocType: {i.get('doctype')}")
        lines.append("")
        alltimes.append(f"{i.get('title')}\t{i.get('email')}\t{i.get('time')}\n")
    return lines

def writef(filename, records):
    with open(filename, "w", encoding="ascii") as f:
        for r in records or []:
            f.write(f"{r}\n")

def printitems(args):
    newlines = []

    alltimes.append("Opening, Note Well and Chairs Updates\tChairs\t15\n")
    alltimes.append("Hackathon Results\tChairs\t10\n")

    alltimes.append('\n### Current Working Group Business\n')
    newlines.append('\n### Current Working Group Business\n')
    newlines.extend(printitem(alltalks.get('wgdocs')))

    alltimes.append('\n### For Consideration\n')
    newlines.append('\n### For Consideration\n')
    newlines.extend(printitem(alltalks.get('nonwgdocs')))

    print("------\n# Agenda\n")
    if args.write:
        ofile = f"dnsop-ietf{args.session}-docs.md"
        writef(ofile, newlines)
        print(f"import {ofile} into dnsop-ietf{args.session}/dnsop-ietf{args.session}-agenda.md")
    else:
        for t in newlines:
            print(t)

    print("------\n# Timetable\n")
    if args.write:
        ofile = f"dnsop-ietf{args.session}-times.tsv"
        writef(ofile, alltimes)
        print(f"import {ofile} into timetable")
    else:
        for t in alltimes:
            print(t)

def main():
    parser = argparse.ArgumentParser(description='Convert Agenda Requests into Agenda')
    parser.add_argument('session', help='Meeting Number (1##)')
    parser.add_argument('--write', action='store_true', help='Write Files')
    # parser.add_argument('--verbose', action='store_true', help='Be more Verbose')
    args = parser.parse_args()

    requestfile = f"dnsop-ietf{args.session}/dnsop-ietf{args.session}-agenda-requests.md"
    lines = readf(requestfile)
    getitems(lines)
    printitems(args)

if __name__ == "__main__":
    main()
