#!/usr/bin/env python
# prints out agenda and timetable from agenda requests

import argparse

alltimes = []
alltalks = {}

def addtalk(agendaitem):
    #       wgdoc = bool('draft-ietf-dnsop' in url)
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
            agendaitem = {'title': title}
        if 'Datatracker URL' in l:
            url = fields[-1]
            wgdoc = bool('draft-ietf-dnsop' in url)
            agendaitem.setdefault('url', fields[-1])
            agendaitem.setdefault('wgdoc', wgdoc)
        if 'Requester Email' in l:
            agendaitem.setdefault('email', ' '.join(fields[3::]))
        if 'Time Requested' in l:
            agendaitem.setdefault('time', fields[3])

    addtalk(agendaitem)


def printitem(docs):
    lines = []
    for i in docs:
        lines.append(f"*   {i.get('title')}")
        lines.append(f"    - {i.get('url')}")
        lines.append(f"    - {i.get('email')}, {i.get('time')} min")
        lines.append("    - Chairs Action:")
        lines.append("")
        alltimes.append(f"{i.get('title')}\t{i.get('email')}\t{i.get('time')}\n")
    return lines

def printitems():
    newlines = []

    alltimes.append('### Current Working Group Business\n')
    newlines.append('### Current Working Group Business\n')
    newlines.extend(printitem(alltalks.get('wgdocs')))

    alltimes.append('### For Consideration\n')
    newlines.append('### For Consideration\n')
    newlines.extend(printitem(alltalks.get('nonwgdocs')))

    for l in newlines:
        print(l)

    print("------\n\n# timetable")
    for t in alltimes:
        print(t)

def main():
    parser = argparse.ArgumentParser(description='print agenda')
    parser.add_argument('session', help='session')
    # parser.add_argument('--verbose', action='store_true', help='Be more Verbose')
    args = parser.parse_args()

    requestfile = f"dnsop-ietf{args.session}/dnsop-ietf{args.session}-agenda-requests.md"
    lines = readf(requestfile)
    getitems(lines)
    printitems()

if __name__ == "__main__":
    main()
