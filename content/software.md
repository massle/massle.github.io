+++
title = "Software"
+++

## Software
- `Plado` | available on [github](https://github.com/massle/plado) <br/>
(P)PDDL python library, including a PDDL parser, lifted successor generator, and a generic datalog engine. The library has full support of fluents, derived predicates (axioms), as well as probabilistic action effects. It features all components to write an automated planner in python from scratch. Example usages are provided in the *examples/* folder. Plado is available on pypi and can be installed via *pip install plado*. Plado is used as part of the Beluga AI challenge toolkit.

- `PFD` (Probabilistic Fast Downward) | [thesis version](https://zenodo.org/records/6992688/files/code.zip?download=1) | [JAIR16 version](https://massle.github.io/fd-prob-jair.zip) | fork available on [github](https://github.com/fai-saarland/probfd)<br/>
Extension of the [Fast Downward planning system](https://www.fast-downward.org) to probabilistic PPDDL (MDP) planning. Features a variety of heuristic search engines (like LAO*, LRTDP, FRET, i-dual) and a variety of heuristics (e.g., based on all-outcomes determinization and the large space of classical planning heuristics that readily ship with Fast Downward; probabilistic pattern databases; and probabilistic occupation-measure heuristics).

- `CDL-FD` (Conflict-Driven Learning Fast Downward) | [download](https://zenodo.org/records/6992688/files/code.zip?download=1)<br/>
Extension of the [Fast Downward planning system](https://www.fast-downward.org) by conflict-driven learning methods akin to conflict-driven clause learning in SAT. In a nutshell, in general state-space search, conflicts become dead ends, i.e., states without any solution path. CDL-FD ships variants of all common heuristic search algorithm (A*, GBFS) and heuristic-guided depth-first searches that identify such conflicts while search is running; refining a dead-end detector upon each such identification. Multiple dead-end detectors are supported (based on critical-path heuristics; dead-end traps; potential heuristics; and the state-equation heuristic). 

- **PPDDL Benchmark Suite** | [generators](https://github.com/massle/ppddl-generators) | [used in my thesis](https://zenodo.org/records/6992688/files/benchmarks.zip?download=1) | [JAIR16 acyclic](https://massle.github.io/ppddl-benchmarks-acyclic.tar.bz2) | [JAIR16 cyclic](https://massle.github.io/ppddl-benchmarks-cyclic.tar.bz2)<br/>
 Comprehensive set of PPDDL benchmarks composed of benchmarks from the IPPCs, Canadian traveler adaptations of resource-constrained classical planning benchmarks (NoMystery, Rovers, and TPP), and an MDP encoding of simulated network penetration testing. Each domain comes with a limited-budget as well as an unlimited-budget version. The suite consists of a suite of acyclic benchmarks (where the state space is acyclic, allowing particular algorithm enhancements) and cyclic benchmarks. 
