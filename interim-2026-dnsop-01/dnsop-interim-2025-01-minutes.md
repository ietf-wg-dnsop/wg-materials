## **dnsop-interim-2025-01-minutes**

The interim meeting focused on the concept of a Distributed Multi-Signer architecture for a DNSSEC zone signing pipeline. The discussion centered around a set of new drafts presented to the DNSOP Working Group. These  drafts aim to address currently missing components needed to fully implement such an architecture.

Presenters:  
Johan Stenstam, Erik Bergstrom, and Leon Fernandez introduced the following drafts:

* draft-ietf-dnsop-generalized-notify (in IETF LastCall)  
    
* draft-berra-dnsop-keystate  
    
* draft-johani-dnsop-delegation-mgmt-via-ddns  
    
* draft-leon-distributed-multi-signer  
    
* draft-johani-tld-zone-pipeline

The slides from the presentations are available on Datatracker:  
https://datatracker.ietf.org/doc/slides-interim-2025-dnsop-01-sessa-towards-distributed-multi-signer/

Following the presentations, the session was opened for questions and discussions.

Ed raised a point about terminology, suggesting that "Sign/No Sign" would be a more intuitive and mnemonic way to represent the concept rather than "Yes/No." There was general agreement that this terminology would work well. It was also noted that in the protocol, this is simply a uint8 (an octet), meaning that different tokens could be used to represent various values as needed.

Stephane brought up a point regarding RFC 8483 and the idea of coordinating through human means. Johan acknowledged that such coordination does happen within organisations and is a well-known practice. An example was given of New Zealand, which has been running a multi-tier configuration manually and in-house for many years. While it is possible to manage coordination manually across organisational boundaries, the concern was raised that doing so is complex and challenging.

The discussion covered multi-signer configurations, highlighting different use cases, including simultaneous multi-signer setups and transitioning from one signer to another. The hsync RR set was designed to support both multi-signer and single-signer contexts, allowing gradual changes to reduce operational risk.

A key point was that while MSAs (Message Signing Authorities) can securely communicate, the details of how they synchronise DNS key information are still being developed. Future work may explore a model where a single provider distributes zones to others, ensuring consistency. However, zone transfer specifics are intentionally left out due to security concerns.

The need for SOA record synchronisation was debated, with agreement that while serial numbers may not need alignment, fields like the technical contact email should remain consistent. The discussion concluded with an acknowledgment that more work is needed to define which apex data elements require synchronization in multi-signer setups.

Steve raised the SOA question, noting that it arises due to multiple sources of change or truth in multi-signer setups. He suggested that the SOA primarily reflects the contents of the zone, while other elements—such as the number of providers, the set of name servers, and the set of keys—can change independently. While acknowledging that some might want an SOA equivalent for these components, he questioned whether it was necessary.

Suzanne then summarised and closed the session, emphasising that the meeting was held to discuss the integrated architecture that spans multiple drafts. While the generalized-notify draft is progressing through the pipeline, other related drafts together define the broader architecture. The discussion provided valuable insights, though no concrete conclusions were drawn yet. Participants were encouraged to continue discussions on the mailing list.

Zulip chat log: https://datatracker.ietf.org/meeting/interim-2025-dnsop-01/materials/chatlog-interim-2025-dnsop-01-202502171600-00

