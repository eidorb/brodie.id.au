```{post} 24 April, 2020
:author: Brodie Blackburn
```
# Purdue model

```{figure} purdue.jpg
:alt: At least it does not identify as a Pie Ass Fuck?

Well, *technically*, it should identify as Purdue Level 3.15149 Pi As Fuck because it's a genderless XIoT device.
```

The [Purdue model](https://en.wikipedia.org/wiki/Purdue_Enterprise_Reference_Architecture) is not a security architecture model.


## A brief history of networks

In the not-so-distant past, today’s ubiquitous network technologies weren’t so common.
Even less so in industrial control system (ICS) networks.
Trendy folk were starting to use a force called “the Ethernet”.
While others began to summon the “the Internet Protocol”.

Ethernet, a LAN technology, operates on shared media.
Back then, people claim, you’d have to get physical because it was very challenging to ram something into a big-ass coaxial cable, or something like that.
All frames (yes, even non-broadcast frames) competed for an opportunity to speak at the cable.
If two hosts piped up at the same time, a collision would occur.
Those frames would be forever lost.
Until a host tries to speak again. \
A retransmission.

Modern networks use switches and full-duplex Ethernet.
This segments the LAN into many collision domains.
Frames can, for the most part, exist without fear of collision and certain oblivion.

There’s nothing to stop you connecting an old school bus network or hub to your modern network.
But in that particular segment, you’ll lose the benefits of a collision-free modern network.


## Ethernet adoption in ICS networks

The IT world was reaping the benefits of the simplicity and interoperability of Ethernet networks.

The ICS world would like some too, please.

New expansion card product lines became available on the market.
Engineers began installing sensors and controllers with Ethernet capabilities.
This got rid of lots of point-to-point serial cabling.
Tapping into an Ethernet bus was *simp*ler.

Then SCADA servers and HMI computers began to appear on the network.
And production management systems. \
And building management systems too. \
Some solar thing. \
And metering. \
IOT...

Why not connect to the administrative staff's computer network too.
It's easier to run reports that way.

Long-term production history databases. \
Payroll systems in some places. \
Backup server spaces.

Countless. \
Hidden. \
Disgraces.

Don't forget printers for all those nuisance alarms!

Uh-oh! \
LAN performance started to tank.
All systems were speaking at the same time.
Ethernet cannot guarantee delivery of frames.
Especially not with all these collisions.

This new Ethernet LAN was rubbish!
It had poor performance and was unreliable.
The engineers required (close to) deterministic performance, otherwise their systems would be unreliable.
Like the network.


## A solution

The Purdue Enterprise Reference Architecture was created to help with network performance[^1].
It is a simple guide to segmenting networks by function.
Network engineers may have designed networks like this without a model.
Others could follow the reference architecture and achieve good enough results.

Why? A network with one collision domain is about as bad as it gets.
If the number of hosts in the network is held constant, then creating more segments (collision domains) has to result in better performance. The more segments, the greater the performance.
But with more segments comes greater complexity, management overhead, and specialist skills.

The Purdue model attempts to strike a balance.

The Purdue model does not mention layer 3 segments (subnets) or even VLANs.
The Purdue model instructs you to perform layer 1 segmentation.
And modern networks kinda already do this for you.
In modern networks, each host typically lives in its own collision domain.
The blue cable binding host with switch.

Poor performance due solely to collisions is probably not much of an issue in well-configured networks.
You can achieve good network performance with a single flat network today.
But high-performance flat networks have downsides too.


## A common misconception

Engineers were at ease.
Their networks had low error rates.
The Purdue model worked.
And networks continued to perform acceptably on into this age of modern networks.

But did it work *because* of the Purdue model?
Because in spite of models, modern flat networks are essentially collision-free.

Security became a thing.
Or maybe a lack of security had started to get physical?

Some had assumed the instructions were to interpret each Purdue level as a layer 3 network.
And everything would be okay with a firewall between those networks.
But the Purdue model is more about reliability and less about information security.
Firewalls between levels is a start, but I think we can do better.

Forcing your square networks in a round Purdue model will result in bizarre pseudo-levels.
Like level 3.5: *RUN DMZ*.
No, it is not in the Purdue Enterprise Reference Architecture[^1].
Notice any confusion that arises when attempting to fit a square network management interface in a round Purdue level.
If the Purdue model is a network segmentation model, then network management is out of scope.

If you find yourself face-to-face with the Purdue model in a conference call, please confirm you are not speaking with an LLM.

[^1]: http://scadamag.infracritical.com/index.php/2018/03/01/purdue-model-history/
