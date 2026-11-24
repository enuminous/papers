# Where Does the Heat Go?

*Matthew Chenoweth Wright · Monolithic LLC · November 24, 2026*

One day in February 2025, a machine in France held a glowing ring of gas for 22 minutes. You could have eaten lunch in the time it took. All the while, heat was leaving that ring and landing on parts inside the machine. If you want to know how close we are to fusion power, those parts are worth a look.

The machine is called WEST. It is a tokamak, a device shaped a bit like a doughnut. Inside, the gas gets so hot that electrons break free from atoms. This mix of charged bits is called *plasma*. Magnets can steer it. The goal of fusion research is to get the centers of light atoms to join and give off energy. A power plant would have to keep doing that and send electricity out to homes.

In the French test, heaters fed energy into the plasma. Pieces made of a metal called tungsten faced the glow. A cooling system carried heat away from them. The team kept the plasma going for 1,337 seconds. Think about what that asks of a cooling system. It has to do its job in the last second as well as it did in the first.

Researchers in Britain are working on the other end of that problem. Can they spread the heat out *before* it hits the metal? Their MAST Upgrade machine uses magnets to guide hot particles toward an exhaust part called a *divertor*. In 2026 the team reported another trick. A little nitrogen at the edge let some energy leave as light. Less heat hit the hottest spot. Think of a bright spot made by a magnifying glass. The same sunlight can warm a whole leaf or scorch one tiny patch.

At Monolithic, we asked a smaller question with a computer model. We took 16 cases. In each one, the model told us how much heat hit the hottest patch on a metal slab. We drew a line at about 1,527 degrees Celsius. That was a mark we chose so we could compare the cases. Different metals and joints have different limits.

Four cases went over our line. Then we ran all 16 again. Each slab got exactly as much heat as before. We changed just one thing. For one second, heat left the back of the slab more slowly. This time, seven cases went over.

All those tiles existed inside a computer. Now we have a question we can ask a real piece of metal. Heat the front of a small sample. Measure how quickly its back cools. Use a heat camera to watch the hot spot. Does it reach the temperature the computer predicted? If it doesn't, the difference can tell us what we left out.

It's easy to picture the future of fusion as a bright ring in a dark room. Picture the back of the tile, too. Somebody has to know how hot it gets there.

### Sources

- [WEST team's account of the 1,337-second experiment](https://irfm.cea.fr/en/2025/02/west-sets-a-new-plasma-duration-record/)
- [UKAEA’s August 2026 account of the nitrogen experiment](https://www.gov.uk/government/news/under-pressure-record-plasma-for-uk-flagship-machine)
- [UK Atomic Energy Authority on MAST Upgrade and its exhaust experiments](https://www.ukaea.org/work/mast-upgrade/)
- [Monolithic's OPENSTEP-009 calculation, cases and test conditions](https://github.com/enuminous/Tokamak/tree/0aa630b4d7e7d825f256f4ac440b5cdd6f8320e3/benchmarks/openstep-009)
