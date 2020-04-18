
# DNS Operations (DNSOP) Working Group
## interim-2020-dnsop-01

* Date: 14 April 2020
* Time: 1400-1600 UTC
* Webex: https://ietf.webex.com/ietf/j.php?MTID=m706bba8b48e3db3db02d72f0941b2630

###
* Jabber:  dnsop@jabber.ietf.org
* EtherPad: https://etherpad.ietf.org:9009/p/interim-2020-dnsop-01

### Chairs
* Tim Wicinski tjw.ietf@gmail.com
* Suzanne Woolf suzworldwide@gmail.com
* Benno Overeinder benno@nlnetlabs.nl

### IESG Overlord
* Warren Kumari warren@kumari.net

### Document Status
* https://github.com/DNSOP/wg-materials/blob/master/dnsop-document-status.md

### Datatracker
* https://datatracker.ietf.org/wg/dnsop/documents/

# Agenda

## Administrivia
    * Agenda Bashing, Blue Sheets, etc,  10 min
    * Updates of Old Work, Chairs, 10 min

## Current Working Group Business

###  Service binding and parameter specification via the DNS
    - https://datatracker.ietf.org/doc/draft-ietf-dnsop-svcb-httpssvc/
    - Ben Schwartz, 15 min
    - Chairs Action: ?
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-svcb-httpssvc-slides/

Stephen Farrell:  Keep the ALPN port; 
Paul Vixie: I proposed removing port number. add a warning that operators should avoid using non-default ports for general Internet use. 
Non-default ports may be firewalled in client networks, so may appear to work in testing but may not work for some clients/users.
Ben Schwartz: We can fix this with 1-2 sentences

Chairs Action:  Want to encourage Interop testing, and WGLC before 108

### DNS Query Name Minimisation to Improve Privacy (bis)
    - https://datatracker.ietf.org/doc/draft-ietf-dnsop-rfc7816bis/
    - Ralph Dolmans, 15min
    - Chairs Action: How close to WGLC?
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-draft-ietf-dnsop-rfc7816bis/

Ralf Weber: don't minimize forwarding; don't recommend complex mechanisms
Jim Reid: query limiting - wording on labels
Stehane Bortzmeyer: number of queries - SHOULD is reasonable (also, see section 7.1 of RFC 1035)
Paul Vixie: 1) auth misconfig hard to detect, mixed-mode authority and the delegation has disappeared. 
with qtype=NS, answer in answer section. 2) rate limiting have ddos implications. 
Joe Abley: not all qtypes are equal. choice of qtype - use 1 qtype and use SOA as an option. 
Ralph Dolmans: maybe small set of qtypes
Joe Abley: any benefit to a small set?
Paul Vixie: Agree with Joe, SOA should be in the mix
Mark Andrews: Forwarders should be trusted, but can't trust beyong forwarder
Warren Kumari: Why are we not using the original qtype 
Ralph Dolmans: Pick the most common qtype the upstream would use
Ralph Dolmans: Unbound switched from NS to A, NS queries are sometimes blocked, but A are not. 
Erik Nygren: A vs AAAA query. A may stick out more. 

Chairs Action: New Version, then working toward WGLC

#
## New Working Group Business

### Avoid IP fragmentation in DNS
    - https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-avoid-fragmentation/
    - Kazunori Fujiwara, 15 min
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-avoid-fragmentation-in-dns/

Joe Abley: this is useful
Ralf Weber: Useful
Paul Vixie: No intent to design Path MTU Discovery. Allow someone to do that.

Chairs Action: CfA sent

### The Delegation_Only DNSKEY flag
    - https://tools.ietf.org/html/draft-pwouters-powerbind-03
    - Paul Wouters, 10 min
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-slides-interim-2020-dnsop-01-draft-pwouters-powerbind/

Ben Schwartz: Likes DNSSEC transparency, Why does it need to be machine readable? 
Paul Wouters: How to put into resolvers? Send Q to list
Peter van Dijk: Authorative should check during loading; does not protect child apex delegation.
Ralf Weber: resolver has to do work. technical solution to political problem. 
Joe Abley: adding complexity must have problem to solve 
Paul Wouters: Large outside subset to never trust DNSSEC.
Wes Hardaker: DNSSEC transparency because don't trust DNSSEC properly 
Joe Abley: World is not as clean as it seems
Warren Kumari: Not sure how this behaves
Paul Wouters: Log all DS changes once this is set
Wes Hardaker: currently have to log every signed record for DNSSEC transparency. with this bit, only log DS records
Matthijs Mekking: 

Chairs Action: Will send out CfA

### Parameterized Nameserver Delegation with NS2 and NS2T
    - https://datatracker.ietf.org/doc/draft-tapril-ns2/
    - Tim April, 15 min
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-slides-draft-tapril-ns2/

Sam Weiler:  Child/Parent/both no restrictions. new record type that only appears on the parent is a can of worms. 
Matt Pounsett: if redesigning NS, remove the current ambiquity. 
Joe Abley:  Can allow clients to never use old polocy
Peter van Dijk: Agree with Sam/Joe, as a resolver implementor, this is scary. 
Alexander Dupuy: If done, present in parent, and in authority sections. 
Paul Hoffman:  Similiar to work done in ADD queue
Ralf Weber: Stub/resolver different than resolver/authorative
Ben Schwartz: Work like this is blocking current dprive work

Chairs Action: Need work and discussion with ADD/DPRIVE/DNSOP chairs

### DNS Catalog Zones & A Data Model for Configuring DNS Zone Provisioning
    - https://datatracker.ietf.org/doc/draft-toorop-dnsop-dns-catalog-zones/
    - https://datatracker.ietf.org/doc/draft-toorop-dnsop-dns-zone-provisioning-yang/
    - Willem Toorop, 15 min
https://datatracker.ietf.org/doc/slides-interim-2020-dnsop-01-sessa-cross-implementation-configuration-and-provisioning-management/

Wes Hardaker: would be good to suceed; should look at RFC6168
Paul Vixie:  supports; Will drop metazone in favor of this

Chairs Action: Catalog Zones - CfA 
Chairs Action: Yang - Needs work

#
## Reference

### BlueSheets

Attendees are asked to visit and enter your Name+Affiliation in the Blue-Sheet section of the DNSOP Etherpad.

### Mic Line Queue

The Mic Line will use the WebEx chat channel.  To get in the queue type q+ to leave type q-.
Please don't type questions or other things into the WebEx chat channel as that will make
managing the queue very hard for the chairs.  Please use the Jabber channel for side conversations.

When you connect into WebEx you should start off as auto-muted so you'll
need to unmute yourself to speak when called.

### Helpful Info & Prep

The IETF has prepared a couple of documents to help get everyone ready.

  https://www.ietf.org/how/meetings/107/session-participant-guide/

  https://www.ietf.org/how/meetings/107/session-presenter-guide/

Attendee List
==========
Warren Kumari, Google
Stephen Farell, Trinity College Dublin
Hugo Salgado, .CL
Ralph Dolmans, NLnet Labs
Donald Eastlake, Futurewei
Paul Ebersman, Neustar
Joe Abley, PIR
Joao Damas, APNIC
Willem Toorop, NLnet Labs
John Border, Hughes
Kazunori Fujiawra, JPRS
Mike Bishop, Akamai
Ted Hardie, Google
Murray Kucherawy, Facebook
Tim Wicinski, unaffialted
Stéphane Bortzmeyer, AFNIC
Sean Turner, sn3rd
Shumon Huque, Salesforce
Peter van Dijk, Open-Xchange PowerDNS 
Keith Mitchell, DNS-OARC
Ben Schwartz, Google
Yoshiro YONEYA, JPRS
Sam Weiler, W3C/MIT
John Dickinson Sinodun IT
Vittorio Bertola, Open-Xchange
David Kinzel, Shaw Communications
Ralf Weber, Akamai Technologies
Scott Hollenbeck, Verisign
Michael Gibbs, Verisign
Ash Wilson, Valimail
Eric Orth, Google
Michael Hausding, SWITCH
Jerry Lundström, DNS-OARC
Witold Kręcicki, ISC
Puneet Sood, Google
Paul Vixie, Farsight
Jim Popovitch, DomainMail, LLC (just curious)
Shinta Sato, JPRS
Ladislav Lhotka, CZ.NIC
Joey Salazar, ARTICLE19
Dick Franks, unaffiliated
Zaid AlBanna, Verisign
Tim April, Akamai Technologies
Mallory Knodel, CDT
Matthijs Mekking, ISC
Roland van Rijswijk-Deij, NLnet Labs
Fredereico Neves, Nic.br
Cathy Aronson, ARIN
Mark Andrews, ISC
Pieter Lexis, Open-Xchange PowerDNS
Jeff Osborn, ISC
Duane Wessels, Verisign
Shane Kerr, NS1
Erik Nygren, Akamai
Matthew Pounsett, DNS-OARC
Bernie Innocenti, Google
Petr Špaček, CZ.NIC
James Gould, Verisign
Vladimir Cunat, cz.nic
Denesh Bhabuta, DNS-OARC
daniel migault
Jim Reid, RTFM llp
Alexander Dupuy, Google
David Blacka, Verisign
Robert Story, USC/ISI
Chi-Jiun Su, Hughes Network Systems
Mauricio Vergara Ereche, ICANN
Claire Pershan, unaffiliated
Michael Richardson, Sandelman Software Works
Wes Hardaker, ISI
Kaustubha Govind, Google Chrome
Marc Groeneweg, SIDN
Hugo Kobayashi, NIC.br
Paul Wouters, Red Hat
Paul Hoffman, ICANN
Benno Overeinder, NLNet Labs
Suzanne Woolf, PIR
Dan McArdle, Google/Chrome
