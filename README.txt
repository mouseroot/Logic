Gates

Gates are the building blocks for all componets.

Componets are basicly many gates that take a number of inputs and outputs
and do work on those inputs to give you the desired outputs.

A very basic example is an inverse gate its not important how this gate works right
now all thats important is what the input is and what the output will be, you can
assume that this gate will inverse whatever the input is and spit it out from the
output.

So if we have an input of 1 and we feed that input into our inverse gate the result
will be 0 because in the world of gates all inputs/outputs are either 1 or 0 also known
as binary.

So lets take a step forward imagine the chip inside your computer known as the CPU (Central Processing Unit)
now that chip has lots of inputs and outputs way too many to even bother with but the same principle applies
the chip is made up of millions of gates that all function together to run your computer and its not just a bunch 
of gates scattered around they are actually made up of smaller componets that make up the entire chip

Now lets return to our gates, imagine you have a few gates wired up that takes a few inputs and spits out 1 output.
so you could for example have the inputs 1,0,1 and do some work on these inputs. lets take another look at how this may work

[
	Warning: The following is code but its known as pseudo code...or code that only explains how something should work
	none of this code is actually valid
]

function someGate(inputA,inputB,inputC) {
	if inputC is 1
		output = add_gate(inputA,inputB)
	else
		output = subtract_gate(inputA,inputB)
}

So here we are describing a function that takes three inputs the first two
are the inputs that will be either added or subtracted the third input will 
tell the function what operation will be used (addiction or subtraction)