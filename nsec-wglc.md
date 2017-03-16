Authors

I've been looking at the emails on the second WGLC, and I think we
are mostly there.  I see two outstanding items.

1.  Matthijs has a comment about the end of section 4 and start of
section 5:

  I do still think that the end of section 4 and start of section 5
  is too similar and can be combined such that it only quotes RFC
  4035 one time.
  Perhaps Section 5 can just start with:

  5.  Aggressive use of Cache

     This document relaxes the restriction given in Section 4.5 of
     [RFC4035], see Section 7 for more detail.

     If the negative cache of the validating resolver has sufficient.

-----
I went back and read the current draft, and I am in agreement here.
There does feel to be duplication.

2. JINMEI's email on 21 December 2016.  Link:

https://mailarchive.ietf.org/arch/msg/dnsop/lCEW5hef9zmMjKSX4J-KlM3mStY

There are a few debatable points, but the ones I tend to side with
are:

 - updates to rfc 4035 are still worded a bit weak. I will think of
 some options.

 - the name of the draft to reflect "DNSSEC-validated Cache" does
 make more sense.

I think this should now be e.g., "Aggressive use of DNSSEC-validated
cache" because of the equal weight given to the aggressive use of
deduced wildcards.

We can go through the other ones, but I think with these touched, we
should be ready to move it forward.

thanks
