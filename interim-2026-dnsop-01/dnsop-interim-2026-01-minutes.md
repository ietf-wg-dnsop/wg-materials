# DNSOP Interim Meeting Minutes

Chairs: Benno Overeinder and Ondřej Surý (absent)
Secretary: Peter Thomassen and Shumon Huque (absent)


## Note Well, Agenda, etc.

The meeting follows the IETF Note Well and Code of Conduct.


## Structured DNS Errors

Presentation of latest revision of draft-ietf-dnsop-structured-dns-error by Dan Wing.

Key changes since IETF Last Call (now in -16):

* Clarified that clients may handle returned information however they want.
* Requests use their own new OPTION-CODE.
* Allows “S” sub-error ENUMs any time.
* Created an IANA registry for sub-error codes.

Discussion:

* Confirmed intent that clients are not required to act on the information.
* Chairs and authors will ensure the IESG understands this was intentional (w/ WG consensus).


## Public Resolver Errors / DNS Filtering Details for Applications

Presentation of latest revision of draft-nottingham-public-resolver-error (renamed to draft-nottingham-dnsop-censorship-transparency) by Mark Nottingham.

Problem statement:

* DNS filtering/censorship is increasing.
* Users cannot distinguish filtering from technical failures.
* Lack of transparency creates user confusion and support load.

Earlier versions:

* Focused on trusted resolver registry.

New approach (draft-02):

* Uses Filtering Incident Databases (e.g., Lumen Database).
* Any resolver can reference such databases.
* Browsers/apps decide which databases to trust.

Implementation status:

* Chrome implementation in progress (with Google Public DNS and Cloudflare).
* Planned behind a feature flag in Chrome M147 (April).

Discussion points

Privacy concerns:

* Users accessing filtering databases may reveal browsing activity.
* Gautam Akiwate offered to contribute text addressing privacy.

Dependency on Structured DNS Errors:

* Draft depends on signalling mechanism but could adapt if needed.
* No incompatibility between the drafts.

IANA registry discussion:

* Concern: censorship-related registry may provide little value.
* Counterpoint: registry provides transparency.
* No consensus reached; issue remains open.


## Working Group Open Discussion

### Structured DNS Errors

* During interim it was suggested to have an additional review, including one from DNS Directorate.
* Chairs will confirm WGLC procedure with AD.

### Public Resolver Errors

* Clear interest from WG to continue work.
* Suggestion to:
  * Present updated draft at next IETF meeting.
  * After IETF, plan Call for Adoption on the mailing list.
