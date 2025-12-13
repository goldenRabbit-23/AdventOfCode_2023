# 🎄 Advent of Code 2023 – Python Solutions

Solutions for **Advent of Code 2023** written in Python.  
Each day lives in its own folder, with:

- `p1.py` – solution for Part 1  
- `p2.py` – solution for Part 2  

---

## 📅 Daily Overview

| Day | Title                    | Summary |
|-----|--------------------------|---------|
| 01  | Trebuchet?!              | Extract calibration values from text by finding first/last digits, then handling spelled-out digits. |
| 02  | Cube Conundrum           | Validate cube-drawing games against color limits, then compute minimum cube sets per game. |
| 03  | Gear Ratios              | Parse a schematic grid to find numbers touching symbols and compute special gear ratios. |
| 04  | Scratchcards             | Score scratchcards by matching numbers, then propagate card copies through the deck. |
| 05  | If You Give A Seed A Fertilizer | Map seeds through chained numeric ranges to locations, then handle massive seed ranges. |
| 06  | Wait For It              | Count charge-time strategies that beat race records, then solve one large combined race. |
| 07  | Camel Cards              | Rank hands in a custom card game, then re-rank with jokers as wildcards. |
| 08  | Haunted Wasteland        | Follow cyclic directions through a graph, then synchronize multiple walkers. |
| 09  | Mirage Maintenance       | Predict next and previous values of number sequences via differences. |
| 10  | Pipe Maze                | Traverse a looping pipe system and count enclosed tiles. |
| 11  | Cosmic Expansion         | Expand empty space between galaxies and compute pairwise distances. |
| 12  | Hot Springs              | Count valid spring arrangements with unknowns using dynamic programming. |
| 13  | Point of Incidence       | Find reflection lines in patterns, then fix exactly one incorrect cell. |
| 14  | Parabolic Reflector Dish | Simulate rolling rocks, then detect cycles over many iterations. |
| 15  | Lens Library             | Implement a custom hash and simulate lens boxes with add/remove operations. |
| 16  | The Floor Will Be Lava   | Trace laser beams through mirrors and splitters to count energized tiles. |
| 17  | Clumsy Crucible          | Find minimum-heat paths with movement constraints. |
| 18  | Lavaduct Lagoon          | Dig trenches and compute enclosed area, even with huge encoded inputs. |
| 19  | Aplenty                  | Route parts through workflows, then count all possible accepted parts. |
| 20  | Pulse Propagation        | Simulate logic modules sending pulses and detect synchronization cycles. |
| 21  | Step Counter             | Count reachable tiles after fixed steps on a repeating grid. |
| 22  | Sand Slabs               | Simulate falling 3D bricks and analyze structural dependencies. |
| 23  |                          |  |
| 24  |                          |  |
| 25  |                          |  |
---

## 🔍 Day-by-Day Details

### Day 01: Trebuchet?!

Each line of input contains mixed characters representing a calibration value.

**Part 1 – Numeric digits only**
- For each line, extract the **first and last numeric digit**.
- Combine them into a two-digit number and sum across all lines.

**Part 2 – Spelled-out digits**
- Digits may appear spelled out (`one`, `two`, …) and can overlap.
- Find the first and last digit *by value*, then sum as before.

---

### Day 02: Cube Conundrum

Each game consists of rounds where colored cubes are drawn from a bag.

**Part 1 – Possible games**
- Given maximum allowed counts for red, green, and blue cubes,
- Determine which games could have occurred and sum their IDs.

**Part 2 – Minimum cube set**
- For each game, find the minimum number of cubes of each color needed.
- Compute the product of these minimums and sum over all games.

---

### Day 03: Gear Ratios

You’re given a grid containing numbers, dots, and symbols.

**Part 1 – Part numbers**
- Identify numbers that touch **any symbol** (including diagonals).
- Sum all such numbers.

**Part 2 – Gear ratios**
- A `*` is a gear if it touches **exactly two numbers**.
- Multiply those two numbers and sum all gear ratios.

---

### Day 04: Scratchcards

Each scratchcard lists winning numbers and numbers you have.

**Part 1 – Card scoring**
- Count how many numbers match.
- Points double for each additional match.

**Part 2 – Card copying**
- Winning cards generate copies of subsequent cards.
- Track the total number of cards after all copies are applied.

---

### Day 05: If You Give A Seed A Fertilizer

Seeds are transformed through multiple mapping stages.

**Part 1 – Individual seeds**
- Apply each mapping in sequence to each seed.
- Find the minimum resulting location number.

**Part 2 – Seed ranges**
- Seeds are given as large ranges.
- Efficiently propagate intervals through all mappings to find the minimum location.

---

### Day 06: Wait For It

You race boats by holding a button to charge speed.

**Part 1 – Multiple races**
- For each race, count charge times that beat the record distance.
- Multiply the counts together.

**Part 2 – One big race**
- Combine all inputs into one race.
- Solve using math rather than brute force.

---

### Day 07: Camel Cards

Hands of cards are ranked with custom rules.

**Part 1 – Standard rules**
- Rank hands by type (pairs, full house, etc.) and card order.
- Sort hands and compute total winnings.

**Part 2 – Joker rules**
- Jokers (`J`) act as wildcards.
- Re-evaluate hand strengths with optimal joker usage.

---

### Day 08: Haunted Wasteland

You traverse a graph using repeating L/R instructions.

**Part 1 – Single start**
- Begin at `AAA` and follow instructions until reaching `ZZZ`.

**Part 2 – Multiple starts**
- Start at all nodes ending with `A`.
- Find the step count where all paths reach nodes ending in `Z` simultaneously.

---

### Day 09: Mirage Maintenance

Each line is a sequence of numbers.

**Part 1 – Next value**
- Repeatedly take differences until reaching zeros.
- Extrapolate the next value.

**Part 2 – Previous value**
- Use the same method to extrapolate the value *before* the sequence.

---

### Day 10: Pipe Maze

A maze of connected pipe characters forms a single loop.

**Part 1 – Loop distance**
- Starting at `S`, find the farthest point along the loop.

**Part 2 – Enclosed area**
- Determine how many grid tiles lie inside the loop.

---

### Day 11: Cosmic Expansion

A map of galaxies contains empty rows and columns.

**Part 1 – Small expansion**
- Duplicate every empty row and column once.
- Sum Manhattan distances between all galaxy pairs.

**Part 2 – Large expansion**
- Empty space expands by a huge factor.
- Compute distances efficiently without building the full grid.

---

### Day 12: Hot Springs

Each row describes springs with damaged groups and unknowns.

**Part 1 – Count arrangements**
- Replace `?` with `.` or `#` to match group sizes.

**Part 2 – Unfolded records**
- Repeat each record multiple times.
- Use dynamic programming to count valid arrangements.

---

### Day 13: Point of Incidence

You’re given patterns of `#` and `.`.

**Part 1 – Perfect reflection**
- Find a horizontal or vertical reflection line.

**Part 2 – Smudged reflection**
- Exactly one cell is wrong.
- Fix it to reveal a valid reflection.

---

### Day 14: Parabolic Reflector Dish

Rocks roll on a grid when tilted.

**Part 1 – Single tilt**
- Tilt north and compute the total load on the support beams.

**Part 2 – Spin cycles**
- Repeatedly tilt in four directions.
- Detect cycles to fast-forward many iterations.

---

### Day 15: Lens Library

A custom hash function drives a lens system.

**Part 1 – Hash sum**
- Compute the hash value of each instruction and sum them.

**Part 2 – Lens boxes**
- Simulate adding/removing lenses in boxes.
- Compute total focusing power.

---

### Day 16: The Floor Will Be Lava

Lasers travel through mirrors and splitters.

**Part 1 – Fixed entry**
- Trace a beam from a starting edge.
- Count energized tiles.

**Part 2 – Best entry**
- Try all possible starting edges.
- Find the maximum energized tiles.

---

### Day 17: Clumsy Crucible

You move through a grid with heat costs.

**Part 1 – Normal crucible**
- Limit how long you can go straight.
- Find the minimum heat-loss path.

**Part 2 – Ultra crucible**
- Enforce minimum straight movement before turning.
- Recompute the minimum heat loss.

---

### Day 18: Lavaduct Lagoon

Dig instructions trace out a trench.

**Part 1 – Direct digging**
- Follow directions and compute the enclosed area.

**Part 2 – Encoded plan**
- Directions are encoded in hexadecimal.
- Use geometry (shoelace + Pick’s theorem) for massive inputs.

---

### Day 19: Aplenty

Parts are routed through conditional workflows.

**Part 1 – Simulated parts**
- Process each part through rules.
- Sum ratings of accepted parts.

**Part 2 – All possible parts**
- Treat ratings as ranges.
- Count how many combinations would be accepted.

---

### Day 20: Pulse Propagation

A network of logic modules sends pulses.

**Part 1 – Pulse counting**
- Simulate 1000 button presses.
- Multiply total low and high pulses.

**Part 2 – Synchronization**
- Find when key modules align.
- Use cycle detection / LCM reasoning.

---

### Day 21: Step Counter

You walk a grid in exactly N steps.

**Part 1 – Finite grid**
- Count reachable positions after a fixed number of steps.

**Part 2 – Infinite grid**
- The grid repeats infinitely.
- Detect growth patterns and extrapolate.

---

### Day 22: Sand Slabs

3D bricks fall under gravity.

**Part 1 – Safe removals**
- Determine which bricks can be removed without causing others to fall.

**Part 2 – Chain reactions**
- For each brick, count how many bricks would fall if it were removed.
- Sum all resulting fall counts.

---

### Day 23:

---

### Day 24:

---

### Day 25:

---

✨ Happy coding, and merry Advent of Code 2023!
