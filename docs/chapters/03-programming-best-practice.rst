Programming best practice
=========================

Objectives
----------

Understand purpose and practicalities:

- of modular code;
- of correctly documented code;
- of automated test

Plan
----

1. Open the `find_primes_v1.py`. Invite a discussion in the class asking them
   first of all if they know what the code does?
2. Capture discussion on the board, asking how this could be improved. Aim to
   get to comments.
3. Invite students to improve this based on discussion.
4. Open `find_primes_v2.py`. Invite the discussion again. Who thinks this is
   better? Is it clearer what the code does? Note that one of the comments is
   incorrect: hopefully someone notices this. Discuss if there are better ways
   to signpost code? Continue to capture on white board. Aim to get to more
   meaningful variable names.
5. Invite students to improve this based on discussion.
6. Open `find_primes_v3.py`. Invite discussion: is this now clearer? How would
   you be able to find errors? Do we still
   need the comments? Continue to capture on white board and aim to get to
   modularity.
7. Invite students to improve this based on discussion.
8. Open the `prime_factors.py`. Invite discussion. Then open
   `integer_division.py` and `is_prime.py`. Invite
   discussion, aim to get to "how do we know it's correct?"
9. Show tests and show how to run. Discuss `assert` and how this exists in other
   languages (but that it's not necessary). Demonstrate, breaking code and tests
   failing.
10. Discuss summary and triangle of docs/tests/modules.

Optional
--------

Solution files to optional question:

- :download:`partition.py <../_static/03-programming-best-practice/partition.py>`
- :download:`test_partition.py <../_static/03-programming-best-practice/test_partition.py>`
- :download:`integration.py
  <../_static/03-programming-best-practice/integration.py>`
- :download:`test_integration.py
  <../_static/03-programming-best-practice/test_integration.py>`

FAQ
---

- **Question:** How to work with testing random functions?
  **Answer:** Discuss seeding tests and discuss testing for meta behaviour.
- **Question:** If I only do one of the three which one should I do?
  **Answer:** I have a personal preference as to what I enjoy doing but it's
  like going on a road trip: you don't go if you have to choose which 3/4 tires
  you take.
- **Question:** What is the difference between a python docstring :code:`"""`
  and a comments :code:`#`?
  **Answer:** There is a technical reason for how they differ under the hood
  (and there might be similar differentiations in other types of languages) but
  the main difference is the audience: a docstring is meant to be read by the
  user of the code and a comment is meant to be read by someone reading your
  code.
