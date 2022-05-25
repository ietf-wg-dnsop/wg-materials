# DNS Operations (DNSOP) Working Group
## interim-2022-dnsop-01


### Chairs
* Benno Overeinder [benno@nlnetlabs.nl](benno@nlnetlabs.nl)
* Suzanne Woolf [suzworldwide@gmail.com](suzworldwide@gmail.com)
* Tim Wicinski [tjw.ietf@gmail.com](tjw.ietf@gmail.com)

### IESG Overlord
* Warren Kumari [warren@kumari.net](warren@kumari.net)

### Document Status
* [Github](https://github.com/ietf-wg-dnsop/wg-materials/blob/main/dnsop-document-status.md)
* [Datatracker](https://datatracker.ietf.org/wg/dnsop/documents/)

* [Propose Slides](https://datatracker.ietf.org/meeting/interim-2022-dnsop-01/session/dnsop)


## Session interim-2021-dnsop-03

* Date: 24 May 2022
* Time: 17:00-18:00 UTC
* MeetEcho: [https://meetings.conf.meetecho.com/interim/?short=45d75893-b015-4b13-b835-204c9de2b003](https://meetings.conf.meetecho.com/interim/?short=45d75893-b015-4b13-b835-204c9de2b003)

* Jabber:  [dnsop@jabber.ietf.org](dnsop@jabber.ietf.org)
* Minutes: [https://notes.ietf.org/notes-ietf-interim-2022-dnsop-01-dnsop](https://notes.ietf.org/notes-ietf-interim-2022-dnsop-01-dnsop)


## Agenda

### Administrivia

* Agenda Bashing, Blue Sheets, etc,  10 min

### Current Working Group Business

*   DNSSEC Automation
    - https://datatracker.ietf.org/doc/draft-wisser-dnssec-automation/
    - Ulrich Wisser and Shumon Huque, 25 min
    - Chairs Action:

ksk/zsk working but need more explicit handling of CSK

basic working of algorithms. but work through implementation pieces

Currently has an implementation that works with dynamic updates and an interface with deSEC is in development

*   Automatic DNSSEC Bootstrapping using Authenticated Signals from the Zone's Operator,
    - https://datatracker.ietf.org/doc/draft-ietf-dnsop-dnssec-bootstrapping/
    - Peter Thomassen and Nils Wisiol, 25 min
    - Chairs Actions:

https://blog.apnic.net/2022/03/08/authenticated-bootstrapping-of-dnssec-delegations/

several implementations done or in progress

three issues

- operator be required to serve bootstrapping issues for all domains?

Ben Schwartz: Should not be required and wrong technically

Wes Hardaker: Should not unless we have a good reason

- do we need an IANA action?

- Delegations within a bootstrapping zone

- Tuple with (name, RRType)

  - Solution Options

    - different record type
    - hashed naming scheme (ruled out)
    - bootstrap under _dsauth
    - disallow CDS/CDNSKEY usage for subzone rollover
    - disallow zone cuts underneath _dsauth 
    - underscore prefix for actual signal
    

Peter van Dijk:  How would you know if something is the leaf domain or not?

Ben: Can't rollover these domains unless bootstrapping

John Levine: Corner Case but leans toward #5 

Peter: people think of #6 ? 

Nils: Ben's comment from chat - #6 needs it's own #5 

Warren Kumari: Burning code points using #1. 

Roger Murray: Personally like #1, but maybe sending more queries. 


```
[16:57:19] <Suzanne Woolf_web_480> I was thinking some salsa maybe....
[16:57:28] <Roger Murray_web_463> something would be nice..
[16:57:42] <sftcd> testing (to see if input from this side of the old matrix.org integration still works)
[16:57:53] <Tim Wicinski_web_605> it does seem to
[16:57:55] <Roger Murray_web_463> or someone just breathing into a mic so we know audio works. ;)
[16:59:14] <Benno Overeinder_web_501> I have the church bells on the hour.
[16:59:16] <Roger Murray_web_463> :smiley:
[16:59:48] <Duane Wessels_web_244> all audio sounds bad to me
[17:00:07] <Duane Wessels_web_244> maybe warrens poor audio was echoing from tim
[17:00:17] <Peter van Dijk_web_695> Tim is ruining all audio, I think (seriously) when unmuted
[17:00:20] <Roger Murray_web_463> Benno sounds good
[17:00:22] <Duane Wessels_web_244> right
[17:00:33] <Tim Wicinski_web_605> so I should not present then !
[17:00:46] <Paul Wouters_web_224> Love the meetecho cross site scripting attack when you are not yet logged into the datatracker when going to the meetecho link
[17:01:18] <Roger Murray_web_463> the conundrum of being impressed or scared.. ;)
[17:01:26] <Paul Wouters_web_224> Had to open a tab manually and login then go to meetecho link
[17:02:14] <Peter van Dijk_web_695> Tim's audio is still pretty bad
[17:02:25] <Vladimír Čunát_web_274> yes
[17:02:57] <Tim Wicinski_web_605> Thanks for letting me know - I had some real pokey connections to meetecho
[17:03:26] <Tim Wicinski_web_605> (i now owe Peter and Vladimir a drink for getting me out of the speaking!)
[17:03:38] <Tim Wicinski_web_605> Taking minutes in https://notes.ietf.org/notes-ietf-interim-2022-dnsop-01-dnsop?edit
[17:04:34] <Suzanne Woolf_web_574> My sound check was fine but I can't get the speaker to switch to my headset....first problem I can remember with meetecho
[17:05:18] <sftcd> fwiw, my draft got here via dispatch not secdispatch (though IMO there's too much dispatchery in general:-)
[17:05:35] <Andrew Campling_web_163> Meetecho has generally worked well for me - using Edge on Windows 10
[17:05:42] <Suzanne Woolf_web_574> Stephen, my mistake, sorry
[17:05:49] <sftcd> no probs
[17:10:02] <Tim Wicinski_web_605> Ulrich - could you mute
[17:10:17] <Vladimír Čunát_web_274> Much better.
[17:13:15] <Tim Wicinski_web_605> Suggestion - add an Implementation Section in the Appendix
[17:14:15] <Tim Wicinski_web_605> oh wait now I see it in #8
[17:14:41] <Roger Murray_web_463> feel free to contact me or Johan if anyone has any questions or comments.
[17:14:54] <Peter van Dijk_web_695> audio is cursed today
[17:14:57] <Tim Wicinski_web_605> Thanks Roger/Johan
[17:16:23] <Ulrich Wisser_web_147> Thank you! I have to leave, sorry
[17:16:29] <Peter van Dijk_web_695> thanks Ulrich!
[17:16:31] <Tim Wicinski_web_605> Thanks Ulrich!
[17:19:58] <Roger Murray_web_463> https://blog.apnic.net/2022/03/08/authenticated-bootstrapping-of-dnssec-delegations/
[17:22:46] <sftcd> +1 to ben - saying REQUIRED there seems unnecessary and wrong technically
[17:24:36] <sftcd> I tend to setup new zones with both external and in-balliwick NSes so also wondered about Ben's question
[17:26:14] <John Levine_web_333> yes, reserve _dsauth
[17:26:22] <Kim Davies_web_705> +1
[17:26:24] <Benjamin Schwartz_web_210> +1
[17:26:26] <Tim Wicinski_web_605> +1
[17:26:35] <Peter van Dijk_web_695> _domainkey is intermediate too, etc. etc.
[17:26:41] <Tim Wicinski_web_605> We can help Peter
[17:26:45] <Suzanne Woolf_web_574> Registry policy for https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#underscored-globally-scoped-dns-node-names is expert review
[17:26:53] <Donald Eastlake_web_373> I can help with IANA text.
[17:26:54] <Suzanne Woolf_web_574> One of the experts s here :-)
[17:28:10] <Vladimír Čunát_web_274> Frederico A C Neves, Paul Wouters
[17:28:31] <Suzanne Woolf_web_574> Yep thanks
[17:28:32] <Tim Wicinski_web_605> Paul is my Expert
[17:28:54] <Paul Wouters_web_224> Yes i can help
[17:29:20] <Paul Wouters_web_224> iPhone meetecho client is …. Not easy
[17:33:40] <Benno Overeinder_web_501> Thanks Paul!
[17:39:32] <Peter van Dijk_web_695> my audio is not working
[17:39:40] <Peter van Dijk_web_695> i'll go to the list later
[17:39:57] <Benjamin Schwartz_web_210> Peter: Have you clicked the mic icon?
[17:40:00] <Peter van Dijk_web_695> ok - number 3, I don't get it. How would you know if something is the leaf domain or not?
[17:40:02] <Peter van Dijk_web_695> Ben, I did!
[17:40:21] <Peter van Dijk_web_695> Meetecho then showed a popup saying it could not hear me. It did work right here 45 minutes ago
[17:40:49] <Vladimír Čunát_web_274> 1. sounds easiest to me.
[17:40:49] <Peter van Dijk_web_695> ok, thanks!
[17:40:54] <Andrew Campling_web_163> @PVD Local muting button on your mic?
[17:41:17] <Peter van Dijk_web_695> Andrew, that would be news! I'll debug later :)
[17:42:17] <Tim Wicinski_web_605> It would be helpful to me if we had some examples with all records
[17:44:15] <Benjamin Schwartz_web_210> Why do they need to be enumerated?
[17:44:45] <Nils Wisiol_web_169> Vladimir, 1 may be easy now but 6 would generalize easier (lets say you want signal DNSKEYs).
[17:45:09] <sftcd> #5 seems reasonable to me
[17:45:23] <Tim Wicinski_web_605> #6 seems more general
[17:45:28] <Peter van Dijk_web_695> 6 just feels wrong, no objective argument
[17:45:29] <John Levine_web_158> Not opposed to #6 but it seems like solving a non problem
[17:45:46] <Benjamin Schwartz_web_210> Does #6 actually solve the problem?
[17:45:59] <Peter van Dijk_web_695> 6 solves the problem if a domain name does not contain _signal or _dsauth
[17:46:01] <Benjamin Schwartz_web_210> What if _dsauth is actually the apex of another zone?
[17:46:08] <John Levine_web_158> Yes, can’t zone cut at non hostname
[17:46:13] <Peter van Dijk_web_695> we had a similar discussion in the dns error reporting draft, where these sentinels on both sides turned out to not solve things
[17:46:42] <John Levine_web_158> Oh wait yes you can
[17:46:53] <Peter van Dijk_web_695> you can zone cut at any non-escaped period
[17:47:08] <Roger Murray_web_463> #1 is easier to communicate and avoids risks of confusion with cds/cdnskey as used to
[17:47:10] <Benjamin Schwartz_web_210> So I think #6 needs its own version of #5
[17:47:14] <Roger Murray_web_463> today
[17:47:17] <Benjamin Schwartz_web_210> or #3
[17:47:51] <Tim Wicinski_web_605> cds/cdnskey deployment has been slow
[17:48:49] <Warren Kumari_web_495> No hats : I think 1 is cleanest...
[17:49:29] <Warren Kumari_web_495> I missed what the downside to #1 is, other than burning codepoints...
[17:51:30] <Warren Kumari_web_495> Thanks
[17:52:27] <Suzanne Woolf_web_574> The other concern I have about this issue is that the mechanics are getting complicated, we will need very precise language around them
[17:53:36] <Vladimír Čunát_web_274> Implementing a new RRtype that's a copy of another one should be easy, surely.  And only parties interested in this bootstrapping will need it, I believe.
[17:53:38] <Peter van Dijk_web_695> yes - 1 is simple
[17:53:46] <Peter van Dijk_web_695> Vladimir, yes
[17:53:57] <Tim Wicinski_web_605> Will add jabber log to minutes
[17:54:30] <Benno Overeinder_web_501> Stephen, are you ready to go next?
[17:54:35] <Vladimír Čunát_web_274> (Though I can't estimate what kind of other signalling and thus types might be useful in future.)
[17:54:36] <sftcd> sure
[17:57:41] <Sean Turner_web_856> For the record, I hope the answer is not no. I hope it's yep we know about this and can provide useful innpuit.
[17:58:24] <Benjamin Schwartz_web_210> Note that this not needed for an ordinary HTTP CDN
[17:59:12] <Tim Wicinski_web_605> Thanks Ben
[17:59:57] <Tim Wicinski_web_605> If there was only a TLS chair in this meeting...
[18:00:31] <Warren Kumari_web_495> My comment from the mail included: "to my mind that makes it seem much more like it should be adopted in something like TLS, with some input / review from DNSOP / HTTPBIS…"
[18:01:15] <Roger Murray_web_463> +1 on the format
[18:01:18] <sftcd> yeah warren's correct as always:-)
[18:01:20] <Tim Wicinski_web_605> I want to thank everyone!
[18:01:30] <Peter Thomassen_web_115> Thank you to the chairs that make it happening
[18:01:44] <Warren Kumari_web_495> @sftd: "vaya con dios" :-P
[18:02:12] <Peter van Dijk_web_695> thanks!
```
