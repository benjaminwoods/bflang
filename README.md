# BFLang
## What is this project?

This is project is designed to attempt to build a fully functioning programming language on top of Brainf**k (BF) using Python >=3.7.

### Okay, but why?

BF is in turn based on P", the first GOTO less language that was shown to be Turing-complete. You can pretty much write any program using BF, but it is a complete 
mess to read.

This project has three main goals:
 - To create a Python module which wraps the BF language
   - Class with methods which access virtual file streams
   - Direct integration with 
   - Use operator overloading to allow BF processes to interact with one another
   - Implement parallel programming paradigms
 - To recreate some of the basic aspects of C/Python
 - Experiment with creating functions/objects using deep learning

The last one I'm pretty excited about. In principle, BF has only 8 commands -- I'm going to play around with base 8 representations of programming objects in 
brainfuck, and see if I can train a neural net to construct these based on desired outputs. Should be fun!

## Yeah, real fun. Why don't you just use C/Python?

Mostly? I'm bored. Plus I want to see whether it is possible.

> Written with [StackEdit](https://stackedit.io/).
