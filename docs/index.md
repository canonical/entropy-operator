A Juju charm deploying Pollen on a machine. Pollen is a scalable,
high performance, free software (AGPL) web server, that provides small
strings of entropy, over TLS-encrypted HTTPS or clear text HTTP connections.
You might think of this as 'Entropy-as-a-Service'.

Pollinate is a free software (GPLv3) script that retrieves entropy from one
or more Pollen servers and seeds the local Pseudo Random Number Generator (PRNG).
You might think of this as PRNG-seeding via Entropy-as-a-Service.

This charm simplifies initial deployment and operations of Pollen
on a machine, such as scaling the number of instances and clustering and more.
As such, the charm makes it easy for those looking to take control of their own
entropy generation whilst keeping operations simple.

For DevOps or SRE teams this charm will make operating Pollen simple and
straightforward through Juju’s clean interface. It will allow easy deployment
into multiple environments for testing of changes, and supports scaling out for
enterprise deployments.

## Project and community

Pollen is an open-source project that welcomes community contributions, suggestions, fixes and constructive feedback.

- [Read our Code of Conduct](https://ubuntu.com/community/code-of-conduct)
- [Join the Discourse forum](https://discourse.charmhub.io/tag/pollen)
- [Discuss on the Mattermost chat service](https://chat.charmhub.io/charmhub/channels/charm-dev)
- Contribute and report bugs to [the Pollen operator](https://github.com/canonical/pollen-operator)

## Contributing to this documentation

Documentation is an important part of this project, and we take the same open-source approach to the documentation as the code. As such, we welcome community contributions, suggestions and constructive feedback on our documentation. Our documentation is hosted on the [Charmhub forum](https://discourse.charmhub.io/) to enable easy collaboration. Please use the "Help us improve this documentation" links on each documentation page to either directly change something you see that's wrong, or ask a question, or make a suggestion about a potential change via the comments section.

If there's a particular area of documentation that you'd like to see that's missing, please [file a bug](https://github.com/canonical/pollen-operator/issues).

# Contents

1. [Tutorial](tutorial)
1. [How to](how-to)
  1. [Contribute](how-to/contribute.md)
  1. [Relate to COS](how-to/relate-to-cos.md)
1. [Reference](reference)
1. [Explanation](explanation)