## **interim-2025-dnsop-01 minutes**


[Chat Log](https://datatracker.ietf.org/meeting/interim-2025-dnsop-01/materials/chatlog-interim-2025-dnsop-01-202502171600-00)

### Drafts

* draft-ietf-dnsop-generalized-notify (IETF LastCall)

* draft-berra-dnsop-keystate

* draft-johani-dnsop-delegation-mgmt-via-ddns

* draft-leon-distributed-multi-signer

* draft-johani-tld-zone-pipeline

[Slides](https://datatracker.ietf.org/doc/slides-interim-2025-dnsop-01-sessa-towards-distributed-multi-signer/)

*Chairs suggest walking through the presentation*

Presentation Summary:

### **Coordination & Automation Challenges**

* New Zealand runs an in-house multi-tier DNS that has been manually managed.
* Automating secure communication between MSAs is a priority before defining synchronization protocols.

### **Protocols & Synchronization Issues**

* **HSYNC RR Set**: Designed to facilitate smooth transitions in signing states.
* Addressed concerns about ensuring identical configurations across multiple providers.
* Debate over whether the SOA record needs full synchronization or just selective fields (e.g., technical contact email).

### **Security Considerations**

* Discussed secure zone transfers, emphasizing the need for **TLS, VPNs, or other secure methods** to prevent attacks.
* Agreed that **exposing zone transfer details is a security risk**, so they should remain confidential.

### **Future Work & Next Steps**

* Further discussions needed on **how MSAs synchronize data** and establish **secure communication**.
* Encouragement to review drafts and contribute to ongoing discussions.

Ed Lewis: "SIGN/NOSIGN" would be more mnemonic than "YES/NO" in the RDATA field

Johan: agreed

Kazunori Fujiwara: The model seems to be similar to the multi-singer controller.

Stephane: 8483 described an intermediary case: signers in different organizations but coordinating closely by human means.

Johan:  yes, but it can be more difficult

Stephane Bortzmeyer: Do you require that the SOA is in sync across all vendors?

Johan: The Serial Number, not so munich, the other parts (contacts, etc) yes.

Johan: They will different SOA but must have keys in sync

Bob Harold: TSIG ?

Johan: TSIG can be used to for zone transfer, or something else that is secure

Suzanne Woolf: Integrated architecture but several drafts that tie them together.
Still hard to take something concrete out of this, other than more discussions.
